from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
from model import predict


app = FastAPI()

# Add CORS middleware to the FastAPI app to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status":"success", "data":"Provide a number of months and a url to get the data from. for example : /predict?months=12&url=https://mapi-0oml.onrender.com/api/v1/supplies/factory/665b2407152b0a04dd9652b5/product/sugar/months/12"}


@app.get("/predict/")
async def get_random(months:int, url: str):

    request = requests.get(url)
    predectedData = predict(request.json(),months)

    return {"status": "success", "data": predectedData}