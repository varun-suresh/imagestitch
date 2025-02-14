from typing import List, Dict, Union
from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
import numpy as np
from PIL import Image
from stitch import Stitcher
import io
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/stitch")
def stitch_images(files: List[UploadFile]) -> Dict[str,Union[str,int]]:
    imgs = []
    for f in files:
        img_bytes = f.file.read()
        imgs.append(Image.open(io.BytesIO(img_bytes)))
    stitcher = Stitcher(np.array(imgs[0]), np.array(imgs[1]))
    stitched_image = stitcher.stitch()
    stitched_image = Image.fromarray(stitched_image)
    stitched_image.save("static/stitched.jpg")
    return {"status": 200, "imageUrl": "/static/stitched.jpg"}
