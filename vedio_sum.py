from transformers import pipeline
import speech_recognition as sr
import moviepy.editor as mp

def transcribe_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source) 
            text = recognizer.recognize_google(audio)
            return text
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return "error"

def summarize_video(video_file):
    clip = mp.VideoFileClip(video_file)
    audio_path = 'output_audio.wav'
    clip.audio.write_audiofile(audio_path)
    #clip.close()
    text = transcribe_audio_to_text(audio_path)
    return text
       
