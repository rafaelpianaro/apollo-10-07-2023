### python


## question 2

### urls

 - http://localhost:8002/percentage_above_40_with_high_chol
 - http://localhost:8002/percentage_above_40_with_high_chol_and_high_fbs

## Installation
 - wsl
 - fastApi

cd my_project/project1
python3 -m venv venv1
source venv1/bin/activate

pip install fastapi uvicorn

example app1.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Olá do Projeto 1!"}


 - port
 uvicorn app1:app --port 8001 --reload

