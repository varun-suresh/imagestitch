from typing import List, Dict
from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
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
        img = Image.open(io.BytesIO(img_bytes))
        print(img.size)
        print(f"Gets here!")
    print(f"Gets here!")
    # stitcher = Stitcher(imgs[0], imgs[1])
    # stitched_image = stitcher.stitch()
    # Image.save("static/stitched.jpg")
    return {"images": len(files)}
    # return {"status": 200}
