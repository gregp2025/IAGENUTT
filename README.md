# IAGENUTT
FFmpeg and ollama must be installed and available in PATH
pour cela installer FFmpeg sur https://www.gyan.dev/ffmpeg/builds/
Puis il doit etre configuré en temps que chemin : 
windows+R  puis remplir avec "sysdm.cpl" choisir "variables d'environnement" puis "path" puis "nouvelle" rajouter le  dossier "bin" de ffmpeg 

test
podcast-generator-ia/
│
├── app.py              # Interface Gradio (UI)
├── llm.py              # Gestion du LLM (Mistral/Llama)
├── tts.py              # Synthèse vocale (Coqui/Bark)
├── audio_utils.py      # Fusion / traitement audio
├── config.py           # Config (modèles, chemins…)
├── requirements.txt    # Dépendances
├── README.md           # Description du projet

