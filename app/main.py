from fastapi import FastAPI

app = FastAPI(title="Forge")


@app.get("/")
def root():
    return {"message": "Welcome to Forge ⚒️"}


@app.get("/health")
def health():
    return {"status": "healthy"}