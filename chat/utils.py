import uuid


def generate_roomname():
    code =str(uuid.uuid4()).replace('-','')[:12]
    return code