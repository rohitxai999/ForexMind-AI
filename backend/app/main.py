from fastapi import FastAPI

from app.api.routes import router
from app.routes.prediction import router as prediction_router

app = FastAPI(
    title="ForexMind AI",
    version="1.0.0"
)

# Existing API routes
app.include_router(router)

# Day 12 Prediction API
app.include_router(prediction_router)


@app.get("/")
def root():
    return {
        "message": "ForexMind AI Backend Running"
    }