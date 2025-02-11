from typing import List, Dict
from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
import numpy as np
import cv2
from PIL import Image
from stitch import Stitcher
import io
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/stitch")
def stitch_images(files: List[UploadFile]) -> Dict[str, int]:
    imgs = []
    for f in files:
        img_bytes = f.file.read()
        imgs.append(Image.open(io.BytesIO(img_bytes)))
    stitcher = Stitcher(np.array(imgs[0]), np.array(imgs[1]))
    stitched_image = stitcher.stitch()
    cv2.imwrite("static/stitched.jpg", stitched_image)
    # return {"images": len(files)}
    return {"status": 200}
