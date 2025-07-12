import gradio as gr
from transformers import pipeline

classificador = pipeline(
    "sentiment-analysis",
    model="vocabtrimmer/xlm-roberta-base-trimmed-pt-5000-tweet-sentiment-pt"
)

def analisar(texto):
    resultado = classificador(texto)[0]
    sentimento = resultado["label"]
    score = round(resultado["score"], 4)
    return f"Sentimento: {sentimento}\nScore: {score}"

gr.Interface(
    fn=analisar,
    inputs=gr.Textbox(label="Digite o texto"),
    outputs=gr.Textbox(label="Resultado"),
    title="Análise de Sentimento em Português",
    description="Este app usa um modelo do Hugging Face para analisar sentimentos de textos em português."
).launch()
