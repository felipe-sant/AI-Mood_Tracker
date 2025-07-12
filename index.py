from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Modelo com vocabulário reduzido para português (mais leve)
classificador = pipeline(
    "sentiment-analysis", 
    model="vocabtrimmer/xlm-roberta-base-trimmed-pt-5000-tweet-sentiment-pt"
)

@app.get("/mood")
async def moodTracker(text: str):
    result = classificador(text)[0]
    print(result['label'])
    return {
        "feeling": result['label'],
        "score": round(result['score'], 4)
    }

@app.get("/")
async def root():
    return {"message": "API está funcionando com modelo trimmed!"}
