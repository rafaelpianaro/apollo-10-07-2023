from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ler_arquivo_dados():
    dados = []
    with open('data.csv', 'r') as arquivo:
        linhas = arquivo.readlines()[1:]  # Ignorar o cabeçalho
        for linha in linhas:
            valores = linha.strip().split(',')
            idade = float(valores[0])
            colesterol = float(valores[4])
            dados.append({'idade': idade, 'colesterol': colesterol})
    return dados

def calcular_porcentagem_colesterol_alto(dados, idade_limite, referencia):
    pessoas_acima_40 = [pessoa for pessoa in dados if pessoa['idade'] > idade_limite]
    pessoas_colesterol_alto = [pessoa for pessoa in pessoas_acima_40 if pessoa['colesterol'] > referencia['colesterol_alto']]
    porcentagem = (len(pessoas_colesterol_alto) / len(pessoas_acima_40)) * 100
    return porcentagem

referencia = {'colesterol_alto': 200}  # Defina o valor de referência para colesterol alto
dados_pessoais = ler_arquivo_dados()
porcentagem = calcular_porcentagem_colesterol_alto(dados_pessoais, 40, referencia)

print(f"A porcentagem de pessoas acima de 40 anos com colesterol alto é de {porcentagem:.2f}%.")

