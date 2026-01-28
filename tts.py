from gtts import gTTS
import os


def text_to_audio(text: str, output_file: str, lang_code):
    """
    Génère un fichier WAV à partir du texte avec gTTS
    """
    mp3_temp = output_file.replace(".wav", ".mp3")

    tts = gTTS(text=text, lang=lang_code)
    tts.save(mp3_temp)

    # convertion  mp3 en wav pour compatibilité
    from pydub import AudioSegment
    audio = AudioSegment.from_mp3(mp3_temp)
    audio.export(output_file, format="wav")

    os.remove(mp3_temp)
