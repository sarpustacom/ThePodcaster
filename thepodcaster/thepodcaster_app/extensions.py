import uuid 
from datetime import datetime
import pytz

def check_if_photo(filename) -> bool:
    ext = filename.lower().split('.')[-1]
    if ext not in ["jpg","png","jpeg","gif","webp"]:
        return False
    return True

def check_if_mp3(filename) -> bool:
    ext = filename.lower().split('.')[-1]
    if ext not in ["mp3"]:
        return False
    return True

def check_if_wav(filename) -> bool:
    ext = filename.lower().split('.')[-1]
    if ext not in ["wav"]:
        return False
    return True

def generate_uuid_namefile(filename) -> str:
    ext = filename.split('.')[-1]
    new_name = f"{uuid.uuid4()}.{ext}"
    return new_name

def correct_date(datetime_str) -> str:
    # Parse the string to a datetime object
    dt = datetime.fromisoformat(datetime_str)

    # Convert it to the desired format
    formatted_dt = dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

    return formatted_dt