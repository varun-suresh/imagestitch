from typing import List, Dict
from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/stitch")
def stitch_images(images: List[UploadFile]) -> Dict[str, int]:
    for f in images:
        img_bytes = f.file.read()
        img = Image.open(io.BytesIO(img_bytes))
        print(img.size)
    return {"images": len(images)}
