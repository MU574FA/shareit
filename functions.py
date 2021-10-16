from uuid import uuid4

def make_unique(file, files):
    while file in files:
        file = f"{str(uuid4())[:9]}{file}"
    return file
