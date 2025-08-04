from fastapi import FastAPI, HTTPException, Depends, UploadFile
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from src.utils.config import APP_NAME, VERSION, API_SECRET_KEY
from src.utils.models import PredictionResponse
from src.inference import classify_image



#Intializing our APP

app = FastAPI(title=APP_NAME, version=VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

api_key_header = APIKeyHeader(name='X-API-Key')
async def verify_api_key(api_key: str=Depends(api_key_header)):
    if api_key !=API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="You are not authorized ")
    return api_key

@app.get('/',tags=['check'])
async def home(api_key: str=Depends(verify_api_key)):
    return{
        "message" : "up & running"
    }

@app.post("/classify", tags=['NN'], response_model=PredictionResponse)
async def classify(file: UploadFile, api_key: str=Depends(verify_api_key)):
    try:
        if not file.content_type.startswith('image/'):
            raise HTTPException(400, "Upload an Image not File")
        
        contents = await file.read()
        response = classify_image(contents)
        return PredictionResponse(**response)
    except Exception as e:
        raise HTTPException(500, f"Error making predictions:{str(e)}")

