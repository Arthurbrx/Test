from sqlalchemy.ext.declarative import declarative_base
import uuid

""" base class from which all mapped classes should inherit """
Base = declarative_base()

def generate_id():
    return str(uuid.uuid4())
