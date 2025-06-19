from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="To Do List")

app.include_router(router)

@app.get("/")
async def root():
	return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
	return {"message": f"Hello {name}"}
