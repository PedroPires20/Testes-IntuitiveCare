from flask import Flask, request
import pandas as pd

DATABASE_FILE = "Relatorio_cadop teste 4.csv"

# Creating the Flask APP
app = Flask(__name__)

# Variable to store the Dataframe containing the data
df = None

# Before the server starts receiving requests, loads the CSV's data into a
# Pandas Dataframe to allow the text queries
@app.before_first_request
def setup_data():
    global df
    df = pd.read_csv(DATABASE_FILE, sep=";", encoding="latin1", skiprows=2)

# Auxiliary function to process a Pandas Dataframe containing the search results
# and transform it into the JSON response objet to be returned by the API
def process_response_df(results_table):
    result_entries = []
    for i in range(results_table.shape[0]):
        result_entries.append({
            "name": results_table.iloc[i]["Nome Fantasia"],
            "corporateName": results_table.iloc[i]["Razão Social"],
            "registry": int(results_table.iloc[i]["Registro ANS"]),
            "resgistryDate": results_table.iloc[i]["Data Registro ANS"],
            "responsible": results_table.iloc[i]["Representante"],
            "phone": results_table.iloc[i]["Telefone"],
            "mail": results_table.iloc[i]["Endereço eletrônico"],
            "city": results_table.iloc[i]["Cidade"],
            "uf": results_table.iloc[i]["UF"],
            "cep": int(results_table.iloc[i]["CEP"]),
            "number": results_table.iloc[i]["Número"],
            "complement": results_table.iloc[i]["Complemento"]
        })
    return { "results": result_entries }

# Auxiliary function that performs a search on the data by the commercial name of
# the company, returning a JSON objet containing the results
def query_by_name(query):
    results = df[df["Nome Fantasia"].str.contains(query, case=False, na=False)]
    return process_response_df(results)

# Auxiliary function that performs a search on the data by the corporate name of
# the company, returning a JSON objet containing the results
def query_by_corporate_name(query):
    results = df[df["Razão Social"].str.contains(query, case=False, na=False)]
    return process_response_df(results)


# Auxiliary function that performs a search on the data by the name of the
# company's responsible, returning a JSON objet containing the results
def query_by_responsible(query):
    results = df[df["Representante"].str.contains(query, case=False, na=False)]
    return process_response_df(results)

# Setting up a route to query the data on the "/search" path with a GET request,
# expecting two parameters: "type" and "query". The "type" parameter may assume
# the values "n", indicating a search by name, "c", indicating a search by
# corporate name or "r", indicating a search by responsible name
@app.route("/search")
def handle_search():
    query_type = request.args.get("type")
    query = request.args.get("query")
    if query_type not in ['n', 'c', 'r']:
        raise ValueError("Invalid or missing query parameter on search!")
    if not query:
        raise ValueError("Missing query term!")
    if query_type == 'n':
        return query_by_name(query)
    elif query_type == 'c':
        return query_by_corporate_name(query)
    elif query_type == 'r':
        return query_by_responsible(query)

# Starting the server and listening for requests. The app runs on 
# the localhost on the port 5000
if __name__ == "__main__":
    app.run(port=5000)
