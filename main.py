from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

#landing page for https://linushorn.dev/

@app.get("/")
async def root() -> FileResponse:
    return FileResponse("./index.html")

@app.get("/favicon.ico")
async def favicon() -> FileResponse:
    return FileResponse("./favicon.ico")

@app.get("/robots.txt")
async def robots() -> FileResponse:
    return FileResponse("./robots.txt")

@app.get("/sitemap.xml")
async def sitemap() -> FileResponse:
    return FileResponse("./sitemap.xml")

@app.get("/humans.txt")
async def humans() -> FileResponse:
    return FileResponse("./humans.txt")

uvicorn.run(app, host="0.0.0.0", port=8228)