from fastapi import FastAPI
from service_utils.utils import example_util

app = FastAPI()

@app.get("/")
async def root():
    return {"message": await example_util()}
