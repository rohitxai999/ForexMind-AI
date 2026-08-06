from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.supervisor import SupervisorAgent
from app.ai.explain import ExplainableAI

router = APIRouter()

supervisor = SupervisorAgent()


class AnalyzeRequest(BaseModel):
    pair: str


@router.post("/analyze")
async def analyze(request: AnalyzeRequest):

    # Existing analysis from Supervisor Agent
    result = supervisor.analyze(request.pair)

    # Demo feature values (these will later come from the AI model)
    features = {
        "trend": "Bullish",
        "rsi": 28,
        "macd": "Bullish",
        "volume": "High",
        "news": "Positive"
    }

    explanation = ExplainableAI.generate_explanation(
        features=features,
        prediction="BUY",
        probability=0.91
    )

    return {
        "analysis": result,
        "explanation": explanation
    }