def predict_health_risk(heart_rate, sleep_hours):
    # Simple rule-based prediction logic
    if heart_rate > 100 or heart_rate < 60:
        return "High"
    if sleep_hours < 5:
        return "High"
    if heart_rate >= 80 and sleep_hours < 7:
        return "Moderate"
    return "Low"