import { Map, View } from "ol";
import OSM from "ol/source/OSM";
import TileLayer from "ol/layer/Tile";
import { fromLonLat } from "ol/proj";

let coords;

async function init() {
    const res = await fetch("/api/get_coords");
    coords = await res.json();
    startApp();
}

function startApp() {
    // Создаём экземпляр карты
    const map = new Map({
        // HTML-элемент, в который будет инициализирована карта
        target: document.getElementById("map"),
        
        // Список слоёв на карте
        layers: [
        // Создадим тайловый слой. Источником тайлов будет OpenStreetMap
            new TileLayer({ source: new OSM() }),
        ],
        
        // Параметры отображения карты по умолчанию: координата центра и зум
        view: new View({
            center: fromLonLat([coords.lon, coords.lat]),
            zoom: 12,
        }),
    });
}

init();