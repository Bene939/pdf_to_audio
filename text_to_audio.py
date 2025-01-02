from TTS.api import TTS
import torch
def text_to_audio(text):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    tts.tts_to_file(text=text, speaker_wav="Morgan_Freeman CC3.wav", language="en", file_path="output.wav")