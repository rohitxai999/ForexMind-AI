from app.risk.position_sizing import PositionSizingEngine
from app.risk.risk_validator import RiskValidator
from app.risk.exposure import ExposureManager
from app.risk.scoring import TradeQualityScorer
from app.risk.engine import RiskEngine


def test_position_sizing():
    engine = PositionSizingEngine()

    result = engine.calculate_position_size(
        account_balance=10000,
        risk_percent=1,
        entry_price=1.1000,
        stop_loss=1.0950,
    )

    assert result["risk_amount"] == 100
    assert result["stop_distance_pips"] == 50
    assert result["position_size_lots"] == 0.2


def test_valid_trade():
    engine = RiskEngine()

    result = engine.evaluate_trade(
        account_balance=10000,
        risk_percent=1,
        entry_price=1.1000,
        stop_loss=1.0950,
        take_profit=1.1100,
        open_trades=[
            {"risk_percent": 1}
        ],
        smc_score=85,
        ict_score=78,
        liquidity_score=91,
        ai_probability=84,
        risk_quality=88,
        risk_reward_score=90,
    )

    assert result["decision"] == "APPROVE"
    assert result["position"]["position_size_lots"] == 0.2
    assert result["quality"]["score"] == 85.4


def test_excessive_trade_risk():
    engine = RiskEngine()

    result = engine.evaluate_trade(
        account_balance=10000,
        risk_percent=3,
        entry_price=1.1000,
        stop_loss=1.0950,
        take_profit=1.1100,
        open_trades=[
            {"risk_percent": 1}
        ],
        smc_score=85,
        ict_score=78,
        liquidity_score=91,
        ai_probability=84,
        risk_quality=88,
        risk_reward_score=90,
    )

    assert result["decision"] == "REJECT"
    assert result["risk_validation"]["approved"] is False


def test_excessive_exposure():
    engine = RiskEngine()

    result = engine.evaluate_trade(
        account_balance=10000,
        risk_percent=2,
        entry_price=1.1000,
        stop_loss=1.0950,
        take_profit=1.1100,
        open_trades=[
            {"risk_percent": 2},
            {"risk_percent": 2},
        ],
        smc_score=85,
        ict_score=78,
        liquidity_score=91,
        ai_probability=84,
        risk_quality=88,
        risk_reward_score=90,
    )

    assert result["decision"] == "REJECT"
    assert result["exposure"]["approved"] is False
    assert result["exposure"]["projected_risk_percent"] == 6


def test_low_quality_trade():
    scorer = TradeQualityScorer()

    result = scorer.calculate(
        smc_score=40,
        ict_score=45,
        liquidity_score=35,
        ai_probability=40,
        risk_quality=50,
        risk_reward_score=45,
    )

    assert result["quality"] == "LOW"
    assert result["recommendation"] == "REJECT"


def test_daily_loss_limit():
    validator = RiskValidator()

    result = validator.validate(
        account_balance=10000,
        risk_percent=1,
        entry_price=1.1000,
        stop_loss=1.0950,
        take_profit=1.1100,
        daily_loss_percent=5,
        position_size=0.2,
    )

    assert result["approved"] is False
    assert result["status"] == "REJECTED"
