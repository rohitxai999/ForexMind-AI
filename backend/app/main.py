from fastapi import FastAPI

from app.api.routes import router
from app.routes.prediction import router as prediction_router
from app.routes.trading import router as trading_router
from app.routes.risk import router as risk_router

app = FastAPI(
    title="ForexMind AI",
    version="1.0.0"
)

# Existing analysis API
app.include_router(router)

# Day 12 Prediction API
app.include_router(prediction_router)

# Day 14 Trading & Analytics API
app.include_router(trading_router)

# Day 15 Risk Management API
app.include_router(risk_router)


@app.get("/")
def root():
    return {
        "message": "ForexMind AI Backend Running"
    }
