from fastapi import FastAPI

app = FastAPI(
    title="ForexMind AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "ForexMind AI",
        "status": "Running",
        "day": "Day 1"
    }