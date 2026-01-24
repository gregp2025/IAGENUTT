import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"


def generate_dialogue(text: str) -> str:
    prompt = f"""
Transforme le texte suivant en dialogue naturel de podcast entre deux personnes :

Personnages :
- Animateur
- Invité

Format strict :
Animateur: ...
Invité: ...

Texte :
{text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()
    return data["response"].strip()
