from fastapi import FastAPI
from src.db.database import engine




app = FastAPI()

with engine.connect() as connection:
    print("Connection successful!")

