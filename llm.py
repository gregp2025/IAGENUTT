import requests

def generate_dialogue(text, lang_code):
    # Choix du prompt selon la langue
    if lang_code == "fr":
        system_prompt = "Tu es un scénariste de podcast français. Crée un dialogue naturel entre un animateur et un invité." # pas besoin de précision pour le langage 
    elif lang_code == "en":
        system_prompt = "You are a podcast script writer. Create a natural dialogue between a host and a guest."# pas besoin de précision pour le langage 
    elif lang_code == "es":
        system_prompt = "Eres un guionista de podcast. Crea un diálogo natural entre un presentador y un invitado."# pas besoin de précision pour le langage 
    elif lang_code == "zh-CN":
        system_prompt = "您是一位中国播客主持人。请用中文创作一段自然流畅的对话，让主持人与嘉宾进行交流。"
    elif lang_code == "ko":
        system_prompt = "당신은 한국인 팟캐스트 작가입니다. 진행자와 게스트 간에 자연스러운 한국어 대화를 만들어 주세요." # Vous êtes un auteur de podcast korean . Veuillez créer un dialogue naturel en japonais  entre l'animateur et l'invité.
    elif lang_code == "ja":
        system_prompt = "あなたは日本のポッドキャスト作家です。司会者とゲストの間の自然な日本語の対話を作成してください。"# Vous êtes un auteur de podcast japonais . Veuillez créer un dialogue naturel en japonais  entre l'animateur et l'invité.
    elif lang_code == "ru":
        system_prompt = "Вы — автор подкаста из России. Пожалуйста, создайте естественный диалог на русском языке между ведущим и гостем." # Vous êtes un auteur de podcast russe . Veuillez créer un dialogue naturel en russe entre l'animateur et l'invité.
    else:
        system_prompt = "Create a podcast dialogue."

    prompt = f"""
{system_prompt}

Sujet :
{text}

Format:
Host: ...
Guest: ...
"""

    # 🔹 Debug : afficher le prompt
    print("Prompt envoyé au LLM:", prompt)

    try:
        response = requests.post(
            "http://localhost:11434/api/generate", #modifier si autre  API
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        data = response.json()
        # 🔹 Debug : afficher la réponse brute
        print("Réponse brute:", data)

        if "response" not in data or not data["response"]:
            return None

        output = data["response"]

        # Transformer le texte en liste de tuples (speaker, sentence)
        dialogue = []
        for line in output.split("\n"):
            if ":" in line:
                speaker, sentence = line.split(":", 1)
                dialogue.append((speaker.strip(), sentence.strip()))

        # Retourner le dialogue sous forme de texte prêt pour TTS
        return "\n".join(f"{sp}: {sen}" for sp, sen in dialogue)

    except Exception as e:
        print("❌ Erreur LLM:", e)
        return None

