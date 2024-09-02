from datetime import datetime
import uuid
from fastapi import HTTPException

def convert_date(date):
    try:
        birthdata_obj = datetime.strptime(date, '%d/%m/%Y').date()
        return birthdata_obj
    except Exception:
        raise HTTPException(status_code=500, detail="Invalid format date.")


def generator_id():
    id = uuid.uuid4()
    return str(id)


def check_date(date):
    if str(date) <= datetime.now().strftime("%Y-%m-%d"):
        raise HTTPException(status_code=400, detail="Expiration date cannot be equal to or less than the current date.")
    