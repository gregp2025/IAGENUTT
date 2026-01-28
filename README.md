
# IAGENUTT — Générateur de Podcast IA (Texte → Voix)



IAGENUTT est une application Python qui transforme un texte en épisode de podcast audio avec un animateur et un invité en utilisant un LLM  pour la génération du texte du podcast et un TTS ( text to speach ) pour l'audio . 



##  Fonctionnalités

- Saisie libre de texte ou sujet
- Génération automatique de dialogue (animateur / invité)
- Support multilingue :
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

## Installer et exécuter le projet en local

###  Prérequis pour le projet 
- Installation de ollama (https://ollama.com/download) puis installation de mistral
- intallation de ffmeg sur https://www.gyan.dev/ffmpeg/builds/ Puis il doit etre configuré en temps que chemin : 
windows+R  puis remplir avec "sysdm.cpl" choisir "variables d'environnement" puis "path" puis "nouvelle" rajouter le chemin du  dossier "bin" de ffmpeg 
###  Structure du projet
- podcast-generator-ia/
 - app.py              # Interface Gradio (UI)
 - llm.py              # Gestion du LLM (Mistral/Llama)
 - tts.py              # Synthèse vocale (Coqui/Bark)
- audio_utils.py      # Fusion / traitement audio
 - config.py           # Config (modèles, chemins…)
- requirements.txt    # Dépendances
- README.md           # Description du projet
### Exécution du projet
-  Lancer ollama 
-  Utiliser l'invite de commande
-  Aller dans le dossier du projet puis faire -python app.py
-  cliquer sur l'url dans la commande (  http://127.0.0.1:7860)
-  Choisir la langue dans l'interface gradio ainsi que remplir le sujet du podcast
-  cliquer sur "générer podcast"
-  appuyer sur "▶️" pour écouter le podcast  
  ---
 ## Les choix techniques et les éventuelles limitations
###  Technologies utilisées

- **LLM** : Ollama (Mistral)
- **TTS** : gTTS (Google Text-to-Speech)
- **Audio** : FFmpeg + Pydub
- **UI** : Gradio
- **Backend** : Python
### Les limitations : 
- Il n'y a que 7 langages qui sont supportés par le TTS
- Il n'y a qu'une seul voix ( donc pas de différence entre l'invité et l'animateur)   



