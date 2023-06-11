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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_IMAGE_CACHE: dict[str, BytesIO] = dict()


class GenerateQRCodeRequest(BaseModel):
    string: str = Field(
        ...,
        description="The string to encode in the QR code",
    )


@app.get("/image/{img_hash}.png", include_in_schema=False)
def get_image(img_hash: str):
    """Get an image from the cache."""
    img_bytes = _IMAGE_CACHE[img_hash]
    img_bytes.seek(0)  # Reset the buffer to the beginning
    return StreamingResponse(img_bytes, media_type="image/png")


@app.post("/generate")
def generate_qr_code(data: GenerateQRCodeRequest, request: Request):
    """Generate a QR code from a string and return a
    link to the image."""
    img_bytes = generate_qr_code_from_string(data.string)
    img_hash = md5(img_bytes.getvalue()).hexdigest()
    _IMAGE_CACHE[img_hash] = img_bytes
    return {"link": f"{get_host(request)}/image/{img_hash}.png"}


def start():
    import uvicorn

    uvicorn.run("server.main:app", host="localhost", port=8000, reload=True)
