from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.supervisor import SupervisorAgent

router = APIRouter()

supervisor = SupervisorAgent()


class AnalyzeRequest(BaseModel):
    pair: str


@router.post("/analyze")
async def analyze(request: AnalyzeRequest):

    result = supervisor.analyze(request.pair)

    return result