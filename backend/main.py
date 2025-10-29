from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Sortwise AI backend is running!"}
