import csv
from fastapi import FastAPI

app = FastAPI()

def read_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho
        for row in reader:
            data.append(row)
    return data

def calculate_percentage_above_40_with_high_chol(data):
    total_above_40 = 0
    above_40_with_high_chol = 0

    for row in data:
        age = float(row[0])
        chol = float(row[4])

        if age > 40:
            total_above_40 += 1
            if chol > 240:
                above_40_with_high_chol += 1

    return (above_40_with_high_chol / total_above_40) * 100

def calculate_percentage_above_40_with_high_chol_and_high_fbs(data):
    total_above_40 = 0
    above_40_with_high_chol_and_fbs = 0

    for row in data:
        age = float(row[0])
        chol = float(row[4])
        fbs = float(row[5])

        if age > 40:
            total_above_40 += 1
            if chol > 240 and fbs > 120:
                above_40_with_high_chol_and_fbs += 1

    return (above_40_with_high_chol_and_fbs / total_above_40) * 100

# Caminho para o arquivo 'data.csv'
file_path = 'data.csv'

# Ler os dados do arquivo
data = read_data(file_path)

@app.get("/percentage_above_40_with_high_chol")
def get_percentage_above_40_with_high_chol():
    percentage_above_40_with_high_chol = calculate_percentage_above_40_with_high_chol(data)
    return {"percentage": percentage_above_40_with_high_chol}

@app.get("/percentage_above_40_with_high_chol_and_high_fbs")
def get_percentage_above_40_with_high_chol_and_high_fbs():
    percentage_above_40_with_high_chol_and_high_fbs = calculate_percentage_above_40_with_high_chol_and_high_fbs(data)
    return {"percentage": percentage_above_40_with_high_chol_and_high_fbs}
