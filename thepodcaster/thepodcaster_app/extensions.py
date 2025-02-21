import uuid 

def check_if_photo(filename) -> bool:
    ext = filename.lower().split('.')[-1]
    if ext not in ["jpg","png","jpeg","gif","webp"]:
        return False
    return True

def generate_uuid_namefile(filename) -> str:
    ext = filename.split('.')[-1]
    new_name = f"{uuid.uuid4()}.{ext}"
    return new_name