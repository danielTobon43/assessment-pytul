from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
import uvicorn
from starlette.responses import FileResponse
import numpy as np
import os

app = FastAPI()
favicon_path = "favicon.ico"

# load data in server
images = np.load(os.path.join(os.getcwd(), "data", "images.pickle"), allow_pickle=True)
labels = np.load(os.path.join(os.getcwd(), "data", "labels.pickle"), allow_pickle=True)
model = np.load(os.path.join(os.getcwd(), "data", "model.pickle"), allow_pickle=True)

# labelmap
labelmap = np.array(
    [
        "T-shirt/top",
        "Trouser",
        "Pullover",
        "Dress",
        "coat",
        "Sandal",
        "Shirt",
        "Sneaker",
        "Bag",
        "Ankle boot",
    ]
)


@app.get("/")
async def root():
    """
    main endpoint
    """
    return RedirectResponse("/docs")


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse(favicon_path)


@app.get("/predict/image/{image_id}")
async def classification(image_id: int):
    """
    handler prediction requests
    """
    print("running prediction...")
    if image_id not in range(len(images)):
        raise HTTPException(status_code=404, detail="Item not found")
    image = np.array([images[image_id]])
    prediction = np.argmax(model.predict(image))

    return JSONResponse(content={"report": {"id": image_id, "class": labelmap[prediction]}})


@app.exception_handler(404)
async def custom_404_handler(_, __):
    """
    handler endpoint not found
    """
    return JSONResponse(content={"report": "endpoint not found"})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, debug=True)
