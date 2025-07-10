from transformers import pipeline
from src.traduzir import traduzir

classificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

while True:
    frase = str(input("Digite uma frase: "))
    resultado = classificador(frase)[0]
    sentimento = traduzir(resultado["label"])
    estrelas = int(resultado["label"].split()[0])
    print(f"\nFrase: {frase}")
    print(f"Sentimento: {sentimento} (Estrelas: {estrelas})")
