import os
import shutil
from tabula import read_pdf
import pandas as pd
from PyPDF2 import PdfFileReader

def pre_process_pdf(pdf_path):
    reader = PdfFileReader(pdf_path)
    num_pages = reader.numPages
    if num_pages < 3:
        raise RuntimeError("Failed to pre-process the PDF: the format was not recognized!")
    return num_pages

def extract_tables(pdf_path, num_pages):
    table = pd.DataFrame()
    for page in range(3, num_pages + 1):
        page_table = read_pdf(pdf_path, pages=page)[0]
        table = pd.concat([table, page_table])
    return table


if __name__ == "__main__":
    PDF_FILE_NAME = "copy2_of_Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.pdf"
    TEMP_DIR_PATH = ".temp"
    CSV_OUT_NAME = "Rol de Procedimentos e Eventos em Saúde - Teste 2.csv"
    ZIP_OUT_NAME = "Teste_Pedro_Dias_Pires"
    num_pages = pre_process_pdf(PDF_FILE_NAME)
    full_table = extract_tables(PDF_FILE_NAME, num_pages)
    if not os.path.exists(TEMP_DIR_PATH):
        os.mkdir(TEMP_DIR_PATH)
    full_table.to_csv(os.path.join(TEMP_DIR_PATH, CSV_OUT_NAME))
    shutil.make_archive(ZIP_OUT_NAME, "zip", TEMP_DIR_PATH)
    shutil.rmtree(TEMP_DIR_PATH, ignore_errors=True)
