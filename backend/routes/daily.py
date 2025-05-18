from fastapi import APIRouter, Body
from services.pixela import create_graph, log_pixel
from fastapi.responses import RedirectResponse
import os

router = APIRouter()

@router.post("")
def setup_graph():
    result = create_graph()
    return {"status": "created", "response": result}

@router.get("/view")
def view_graph():
    username = os.getenv("PIXELA_USER")
    graph_id = os.getenv("GRAPH_ID")
    graph_url = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"
    return RedirectResponse(graph_url)


@router.post("/log")
def log_daily_wins(quantity: int = Body(..., embed=True)):
    """Log a specific number of wins for today"""
    result = log_pixel(quantity)
    return {"status": "logged", "response": result}
