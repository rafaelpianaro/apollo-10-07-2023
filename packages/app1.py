from fastapi import FastAPI
import requests
import csv

app = FastAPI()

@app.get("/")

def gerar_arquivo_csv():
    url = "https://pypi.org/pypi/sampleproject/json"

    # Faz a solicitação GET para a API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extrai os dados necessários do JSON recebido
        info = data["info"]
        nome = info["name"]
        versao = info["version"]
        autor = info["author"]
        descricao = info["summary"]

        # Define o nome do arquivo CSV
        nome_arquivo = f"{nome}_{versao}.csv"

        # Cria o arquivo CSV e escreve os dados
        with open(nome_arquivo, "w", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["Nome", "Versão", "Autor", "Descrição"])

            # Escreve os registros limitando a 50
            registros_gravados = 0
            while registros_gravados < 50:
                writer.writerow([nome, versao, autor, descricao])
                registros_gravados += 1

        print(f"Arquivo CSV '{nome_arquivo}' gerado com sucesso.")
    else:
        print("Não foi possível acessar a API.")

# Chamada da função para gerar o arquivo CSV
gerar_arquivo_csv()
