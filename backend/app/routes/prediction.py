from fastapi import APIRouter
from app.services.signal_service import SignalService

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)

service = SignalService()


@router.get("/")
def get_prediction():
    """
    Generate an AI-powered Forex prediction
    with an explainable report.
    """
    return service.generate_signal()