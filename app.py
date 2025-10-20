from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

app.mount("/src", StaticFiles(directory="src"), name="src")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("crossword.html", "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    os.makedirs("src", exist_ok=True)
    uvicorn.run(app, host="0.0.0.0", port=8000)
