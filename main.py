from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import requests
from fastapi.testclient import TestClient

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


class Task2(BaseModel):
    date: str


@app.post("/day")
async def day(task2: Task2):
    # Actual date (dictionary
    current_datetime = datetime.now()
    day_response = requests.get("http://numbersapi.com/" + str(current_datetime.day))
    month_response = requests.get("http://numbersapi.com/" + str(current_datetime.month))
    year_response = requests.get("http://numbersapi.com/" + str(current_datetime.year))

    # Custom dictionary
    # If day = month, one position is not displayed
    date = {
        current_datetime.day: day_response.text,
        current_datetime.month: month_response.text,
        current_datetime.year: year_response.text
    }

    print(date)
    return JSONResponse(content=date)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
