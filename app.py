import gradio as gr
from llm import generate_dialogue
from tts import text_to_audio
from audio_utils import merge_audios
import os
import uuid

OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_podcast(text):
    if not text.strip():
        return None, "⚠️ Veuillez entrer un texte."

    # 1. Générer le dialogue
    dialogue = generate_dialogue(text)

    audio_files = []

    # 2. Générer audio pour chaque réplique
    for i, line in enumerate(dialogue.split("\n")):
        if ":" not in line:
            continue

        speaker, content = line.split(":", 1)
        content = content.strip()

        if not content:
            continue

        filename = f"{OUTPUT_DIR}/{uuid.uuid4()}.wav"

        text_to_audio(content, filename)
        audio_files.append(filename)

    if not audio_files:
        return None, "❌ Erreur lors de la génération du dialogue."

    # 3. Fusion en MP3
    output_mp3 = f"{OUTPUT_DIR}/podcast_{uuid.uuid4()}.mp3"
    merge_audios(audio_files, output_mp3)

    return output_mp3, "✅ Podcast généré avec succès !"


# ================= UI =================

with gr.Blocks(title="Générateur de Podcast IA") as demo:
    gr.Markdown("## 🎙️ Générateur de Podcast IA")
    gr.Markdown("Transformez un texte en podcast audio avec plusieurs voix.")

    input_text = gr.Textbox(
        label="Texte ou sujet du podcast",
        placeholder="Ex: L'intelligence artificielle dans la médecine...",
        lines=6
    )

    generate_btn = gr.Button("🎧 Générer le podcast")

    audio_output = gr.Audio(label="Podcast généré", type="filepath")
    status_output = gr.Textbox(label="Statut")

    generate_btn.click(
        fn=generate_podcast,
        inputs=input_text,
        outputs=[audio_output, status_output]
    )

demo.launch()
