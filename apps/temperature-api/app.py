from datetime import datetime, timezone
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/temperature")
def get_temperature(location: str):
    temperature = random.uniform(-20.0, 40.0)

    return {
        "value": round(temperature, 2),
        "unit": "C",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec='seconds'),
        "location": location,
        "status": "active",
        "sensor_id": "4815162342",
        "sensor_type": "temperature",
        "description": "Outdoor temperature sensor"
    }

@app.get("/temperature/{sensor_id}")
def get_temperature_by_id(sensor_id: str):
    temperature = random.uniform(-20.0, 40.0)

    return {
        "value": round(temperature, 2),
        "unit": "C",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec='seconds'),
        "location": "unknown",
        "status": "active",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": "Temperature sensor with ID {}".format(sensor_id)
    }
