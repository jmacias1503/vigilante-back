from fastapi import FastAPI
from routes.alerts import alert

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}