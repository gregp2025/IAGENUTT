# IAGENUTT
FFmpeg and ollama must be installed and available in PATH
pour cela installer FFmpeg sur https://www.gyan.dev/ffmpeg/builds/
Puis il doit etre configuré en temps que chemin : 
windows+R  puis remplir avec "sysdm.cpl" choisir "variables d'environnement" puis "path" puis "nouvelle" rajouter le  dossier "bin" de ffmpeg 

# 🎙️ IAGENUTT — Générateur de Podcast IA (Texte → Voix)

IAGENUTT est une application Python qui transforme un texte en épisode de podcast audio réaliste avec plusieurs voix, en utilisant un LLM et une synthèse vocale automatique.

---

##  Fonctionnalités

- Saisie libre de texte ou sujet
- Génération automatique de dialogue (animateur / invité)
- Support multilingue 🌍 :
  - Français
  - Anglais
  - Espagnol
  - Chinois
  - Coréen
  - Japonais
  - Russe
- Synthèse vocale automatique (TTS)
- Fusion audio automatique
- Export en MP3
- Interface web avec Gradio

---

## 🧠 Technologies utilisées

- **LLM** : Ollama (Mistral)
- **TTS** : gTTS (Google Text-to-Speech)
- **Audio** : FFmpeg + Pydub
- **UI** : Gradio
- **Backend** : Python

---

## 📁 Structure du projet


IAGENUTT/
│
├── app.py
├── llm.py
├── tts.py
├── audio_utils.py
├── requirements.txt
├── outputs/
└── README.md











test
podcast-generator-ia/
 app.py              # Interface Gradio (UI)
 llm.py              # Gestion du LLM (Mistral/Llama)
 tts.py              # Synthèse vocale (Coqui/Bark)
audio_utils.py      # Fusion / traitement audio
 config.py           # Config (modèles, chemins…)
requirements.txt    # Dépendances
README.md           # Description du projet

