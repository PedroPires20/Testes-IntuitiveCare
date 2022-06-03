import os
import shutil
from camelot import read_pdf
import pandas as pd
from PyPDF2 import PdfFileReader

def pre_process_pdf(pdf_path):
    reader = PdfFileReader(pdf_path)
    num_pages = reader.numPages
    if num_pages < 3:
        raise RuntimeError("Failed to pre-process the PDF: the format was not recognized!")
    return num_pages

def process_table(table_df):
    table_df.columns = table_df.iloc[0]
    table_df.drop(0, inplace=True)

def extract_tables(pdf_path, num_pages):
    full_table = pd.DataFrame()
    for page in range(3, num_pages + 1):
        print("Processando página {} de {}...".format(page - 2, num_pages - 2))
        page_tables = read_pdf(pdf_path, pages="{}".format(page), process_background=True)
        if len(page_tables) < 1:
            raise RuntimeError("Failed to process page number {}!\nNo tables were found in the page."
                .format(page))
        table = page_tables[0].df
        process_table(table)
        full_table = pd.concat([full_table, table])
    full_table.reset_index(drop=True, inplace=True)
    return full_table

def post_process_table(full_table):
    full_table["OD"].replace({ "OD": "Seg. Odontológica" }, inplace=True)
    full_table["AMB"].replace({ "AMB": "Seg. Ambulatorial" }, inplace=True)

if __name__ == "__main__":
    PDF_FILE_NAME = "copy2_of_Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.pdf"
    TEMP_DIR_PATH = ".temp"
    CSV_OUT_NAME = "Rol de Procedimentos e Eventos em Saúde - Teste 2.csv"
    ZIP_OUT_NAME = "Teste_Pedro_Dias_Pires"
    print("Iniciando o processamento do PDF")
    num_pages = pre_process_pdf(PDF_FILE_NAME)
    full_table = extract_tables(PDF_FILE_NAME, num_pages)
    print("Processando a tabela gerada")
    post_process_table(full_table)
    print("Gerando arquivo CSV com as tabelas")
    if not os.path.exists(TEMP_DIR_PATH):
        os.mkdir(TEMP_DIR_PATH)
    full_table.to_csv(os.path.join(TEMP_DIR_PATH, CSV_OUT_NAME), index=False)
    print("Comprimindo o arquivo CSV gerado")
    shutil.make_archive(ZIP_OUT_NAME, "zip", TEMP_DIR_PATH)
    print("Limpando arquivos temporários")
    shutil.rmtree(TEMP_DIR_PATH, ignore_errors=True)
    print("Operação concluída com sucesso!")
