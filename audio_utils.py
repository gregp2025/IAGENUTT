from pydub import AudioSegment
import os


def merge_audios(wav_files, output_mp3):
    combined = AudioSegment.empty()

    for wav in wav_files:
        if os.path.exists(wav):
            audio = AudioSegment.from_wav(wav)
            combined += audio

    combined.export(output_mp3, format="mp3")
