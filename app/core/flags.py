from app.core.config import settings

def get_feature_flags() -> dict:
    return {
        "credit_reporting": settings.enable_credit_reporting,
        "payments": settings.enable_payments,
        "notifications": settings.enable_notifications,
    }
