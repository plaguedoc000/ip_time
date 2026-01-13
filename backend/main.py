from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

@app.get("/api/get_coords")
def get_coords():
    url = "http://ip-api.com/json/"
    responce = requests.get(url).json()
    return {
        "lat": responce["lat"], 
        "lon": responce["lon"],
    }

app.mount("/", StaticFiles(directory="../frontend/dist", html=True))