from fastapi import FastAPI
from transformers import pipeline
from src.translate import translate

app = FastAPI()
classificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

@app.get("/mood")
async def moodTracker(text: str):
    result = classificador(text)[0]
    feeling = translate(result['label'])
    stars = int(result["label"].split()[0])
    return {
        "feeling": feeling,
        "stars": stars
    }

@app.get("/")
async def test():
    return {"message": "AI Service is working!"}