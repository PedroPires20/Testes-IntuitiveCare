import os
import shutil
import urllib3
from http.client import HTTP_PORT, responses as status_messages
from bs4 import BeautifulSoup

# This function receives an integer, representing a HTTP status code and returns
# a boolean, indicating if the status code is a success code or not
def success_status(status_code):
    return status_code >= 200 and status_code < 300

# This function makes a http request to the given "url" string and, if the
# response is successful, it returns the bytes of the body of the response. If
# an error occurs, the function raises an RuntimeError exception, informing the
# status code and message of the fail response
def fetch_url(url):
    http_client = urllib3.PoolManager()
    response = http_client.request("GET", url)
    if not success_status(response.status):
        raise RuntimeError('HTTP request failed with status code {}: "{}"'
            .format(response.status, status_messages[response.status]))
    return response.data

# This functions receives the bytes of a HTTP response data that contains an
# HTML documents, decodes it's contentes and parses the HTML using the
# BeautifulSoup library and then locates and returns the links of the files to
# be downloaded
def get_file_urls(response_bytes):
    LINK_CSS_SELECTOR = ".callout a"
    DESIRED_FILE_NAMES = [
        "Anexo I - Lista completa de procedimentos (.pdf)",
        "Anexo I - Lista completa de procedimentos (.xlsx)",
        "Anexo II - Diretrizes de utilização (.pdf)",
        "Anexo III - Diretrizes clínicas (.pdf)",
        "Anexo IV - Protocolo de utilização (.pdf)"
    ]
    html_document = BeautifulSoup(response_bytes.decode(), 'html.parser')
    page_links = html_document.select(LINK_CSS_SELECTOR)
    file_urls = []
    for link in page_links:
        if link.get_text() in DESIRED_FILE_NAMES:
            file_urls.append(link['href'])
    return file_urls

# This function downloads the file found on a given URL and saves the download
# file on the given directory's path. If the directory doesn't exist, it is
# created by the function. The name of the file to save is deduced from the
# URL's path, grabbing the last path entry as the file name
def download_file(url, output_path):
    # Getting the name of the file from it's URL
    file_name = urllib3.util.url.parse_url(url).path.split('/')[-1]
    try:
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        http_client = urllib3.PoolManager()
        response = http_client.request("GET", url)
        if not success_status(response.status):
            raise RuntimeError('HTTP request failed with status code {}: "{}"'
            .format(response.status, status_messages[response.status]))
        with open(os.path.join(output_path, file_name), "wb") as output_file:
            output_file.write(response.data)
    except Exception as e:
        raise e

if __name__ == "__main__":
    TARGET_URL = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
    TEMPORARY_DIRECTORY = ".temp"
    OUTPUT_ZIP_NAME = "Anexos - Teste 1"
    response_data = fetch_url(TARGET_URL)
    file_urls = get_file_urls(response_data)
    for file_url in file_urls:
        download_file(file_url, TEMPORARY_DIRECTORY)
    # Creating the zip file with the downloaded files
    shutil.make_archive(OUTPUT_ZIP_NAME, "zip", TEMPORARY_DIRECTORY)
    # Cleanup: removing the temporary directory (any errors in this operation are ignored)
    shutil.rmtree(TEMPORARY_DIRECTORY, ignore_errors=True)
    