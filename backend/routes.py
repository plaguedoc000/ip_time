from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/api/get_client_ip")
def get_client_ip():
    url = "https://api.ipify.org"
    responce = {"ip": requests.get(url).text}
    return responce

@router.get("/api/get_coords_by_ip")
def get_coords(ip: str):
    url = f"http://ip-api.com/json/{ip}"
    responce = requests.get(url).json()
    return {
        "lat": responce["lat"], 
        "lon": responce["lon"],
    }