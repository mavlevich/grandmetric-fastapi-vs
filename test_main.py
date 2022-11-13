from fastapi.testclient import TestClient
import requests
import datetime
from fastapi.responses import JSONResponse
from main import app


client = TestClient(app)


# Example
def test_status():
    response = client.status("/status")
    assert response.status_code == 200
    assert response.json() == {"ok"}


def test_day():
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

    response = client.day("/day")
    assert response.status_code == 200
    assert response.json() == JSONResponse(content=date)
