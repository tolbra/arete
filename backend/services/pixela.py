import os
import httpx
from dotenv import load_dotenv

from datetime import datetime
load_dotenv()

PIXELA_USER = os.getenv("PIXELA_USER")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

def create_graph():
    url = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs"
    payload = {
        "id": GRAPH_ID,
        "name": "Daily Wins",
        "unit": "win",
        "type": "int",
        "color": "shibafu",  # green
        "timezone": "Asia/Almaty",
        "is_secret": False,
        "self_sufficient": "increment"
    }

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    response = httpx.post(url, headers=headers, json=payload)
    return response.json()




def log_pixel(quantity: int):
    date = datetime.now().strftime("%Y%m%d")
    url = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{GRAPH_ID}"
    payload = {
        "date": date,
        "quantity": str(quantity)
    }
    headers = {"X-USER-TOKEN": PIXELA_TOKEN}
    response = httpx.post(url, headers=headers, json=payload)
    return response.json()