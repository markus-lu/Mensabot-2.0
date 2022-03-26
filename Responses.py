from datetime import datetime

def sample_responses(input_text):
    user_massage: str = str(input_text).lower()

    if user_massage in ("Hello there"):
        return "General Kenobi"
    if user_massage in ("time" , "time?"):
        return "haut vor Knochen"