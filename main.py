from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import requests
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
import json


app = FastAPI()


# Hello
@app.get("/")
async def root():
    return {"message": "Hello Grandmetric"}


# Task 1
@app.get("/status", status_code=200)
async def status():
    return "ok"


# Tests
client = TestClient(app)


# Task 2
# Request data model
class DateModelForApiRequest(BaseModel):
    date: str


@app.post("/day")
async def newday(incoming_request_with_date: DateModelForApiRequest):
    # Zmienne dla przyszlej walidacji 
    date_validation_day = False;
    date_validation_month = False;
    date_validation_year = False;
    date_validation_length = False;

    # Serializacja do str
    # serialized_dictionary_with_date = '{"date": "28.10.2022"}'                       # Przyklad danych
    serialized_dictionary_with_date = incoming_request_with_date.json()

    # Pobranie liczb dla przyszlego requestu do numbersapi
    day = serialized_dictionary_with_date[10:12]
    month = serialized_dictionary_with_date[13:15]
    year = serialized_dictionary_with_date[16:20]

    # Walidacja na dlugosc str, czyli rok w formacie "22" nie przejdzie 
    if (len(serialized_dictionary_with_date) == 22):
        date_validation_length = True

    # Walidacja danych (sprawdzenie czy cyferki mamy)
    if ((day[0] >= '0' and day[0] <= '9') and (day[1] >= '0' and day[1] <= '9')):
        print("day OK")
        date_validation_day = True
    if ((month[0] >= '0' and month[0] <= '9') and (month[1] >= '0' and month[1] <= '9')):
        print("month OK")
        date_validation_month = True
    if ((year[0] >= '0' and year[0] <= '9') and (year[1] >= '0' and year[1] <= '9') and 
        (year[2] >= '0' and year[2] <= '9') and (year[3] >= '0' and year[3] <= '9')  ):
        print("year OK")
        date_validation_month = True
    

    # Calkowita walidacja (literki + dlugosc)
    # Teoretycznie mozna zrobic walidacje na prawdziwa date, czyli month >= 1 and month <= 12, day >= 1 nad day <= 31
    if (date_validation_length != True or date_validation_day != True or date_validation_month != True or date_validation_year):
        dict_error = {
            "error": "Incorrect request format"
        }
        return JSONResponse(content=dict_error)
    
    # Zapytanie do api 
    day_response = requests.get("http://numbersapi.com/" + day)
    month_response = requests.get("http://numbersapi.com/" + month)
    year_response = requests.get("http://numbersapi.com/" + year)

    # Generacja slownika dla odpowiedzi zwrotnej
    date = {
        day: day_response.text,
        month: month_response.text,
        year: year_response.text
    }

    # print(date)
    return JSONResponse(content=date)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
