from fastapi import FastAPI, Request, Query
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from routers.well_known import well_known, get_ai_plugin, get_host
from hashlib import md5
from io import BytesIO

from services.qr import generate_qr_code_from_string

ai_plugin = get_ai_plugin()

app = FastAPI(
    title=ai_plugin["name_for_human"],
    description=ai_plugin["description_for_human"],
    version="0.1.0",
)

app.include_router(well_known)

# Add your endpoints here


def start():
    import uvicorn

    uvicorn.run("server.main:app", host="localhost", port=8000, reload=True)
