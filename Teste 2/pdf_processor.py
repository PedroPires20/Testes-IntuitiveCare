import os
import shutil
from camelot import read_pdf
import pandas as pd
from PyPDF2 import PdfFileReader

# This functions receives the path to a PDF file, opens it with the PyPDF2
# library and returns the number of pages in the PDF
def num_pdf_pages(pdf_path):
    reader = PdfFileReader(pdf_path)
    num_pages = reader.numPages
    if num_pages < 3:
        raise RuntimeError("Failed to pre-process the PDF: the format was not recognized!")
    return num_pages

# This function receives a Pandas Dataframe of a table extracted from one of the
# PDF's pages and applies some treatment on it's data to fix some processing
# errors that occur in the extraction from the PDF
def process_page_table(table_df):
    table_df.columns = table_df.iloc[0]
    table_df.drop(0, inplace=True)

# This function receives the path to the PDF file containing the tables and
# returns a pandas Dataframe that results of the concatenation of the tables
# extractes from each page of the PDF. If a page after the second page doesn't
# contain a table, a RuntimeError is risen by the function
def extract_tables(pdf_path):
    num_pages = num_pdf_pages(pdf_path)
    full_table = pd.DataFrame()
    for page in range(3, num_pages + 1):
        print("Processando página {} de {}...".format(page - 2, num_pages - 2))
        page_tables = read_pdf(pdf_path, pages="{}".format(page), process_background=True)
        if len(page_tables) < 1:
            raise RuntimeError("Failed to process page number {}!\nNo tables were found in the page."
                .format(page))
        table = page_tables[0].df
        process_page_table(table)
        full_table = pd.concat([full_table, table])
    full_table.reset_index(drop=True, inplace=True)
    return full_table

# This function receives the full table extracted from all the pages of the PDF
# file and does some post-processing, replacing sobre abreviattions by their
# meaning. This treatment is done "in-place" on the given table and nothing is
# returned
def post_process_table(full_table):
    full_table["OD"].replace({ "OD": "Seg. Odontológica" }, inplace=True)
    full_table["AMB"].replace({ "AMB": "Seg. Ambulatorial" }, inplace=True)

if __name__ == "__main__":
    PDF_FILE_NAME = "copy2_of_Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.pdf"
    TEMP_DIR_PATH = ".temp"
    CSV_OUT_NAME = "Rol de Procedimentos e Eventos em Saúde - Teste 2.csv"
    ZIP_OUT_NAME = "Teste_Pedro_Dias_Pires"
    try:
        print("Iniciando o processamento do PDF")
        full_table = extract_tables(PDF_FILE_NAME)
        print("Processando a tabela gerada")
        post_process_table(full_table)
        print("Gerando arquivo CSV com as tabelas")
        if not os.path.exists(TEMP_DIR_PATH):
            os.mkdir(TEMP_DIR_PATH)
        full_table.to_csv(os.path.join(TEMP_DIR_PATH, CSV_OUT_NAME), index=False)
        print("Comprimindo o arquivo CSV gerado")
        shutil.make_archive(ZIP_OUT_NAME, "zip", TEMP_DIR_PATH)
        print("Operação concluída com sucesso!")
    except Exception as exception:
        print("Ocorreu um erro no processamento do script de processamento do PDF!\nErro encontrado: {}"
            .format(exception))
    finally:
        print("Limpando arquivos temporários")
        shutil.rmtree(TEMP_DIR_PATH, ignore_errors=True)
