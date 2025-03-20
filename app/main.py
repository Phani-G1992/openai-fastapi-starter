from fastapi import FastAPI
from app.api.v1 import endpoints

app = FastAPI(title="OpenAI FastAPI Starter")

# Register routes
app.include_router(endpoints.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "OpenAI FastAPI service is running!"}
