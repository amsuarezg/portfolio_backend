from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hi, my name is Mateo Suarez!"}
