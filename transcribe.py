import sys
from pydub import AudioSegment
import speech_recognition as sr
import os

# Set the path to ffmpeg if not in system PATH
os.environ["PATH"] += os.pathsep + r"C:\path\to\ffmpeg\bin"  # Adjust this path as needed

def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    # Load MP3 file
    audio = AudioSegment.from_mp3(mp3_file_path)
    # Export as WAV
    audio.export(wav_file_path, format="wav")

def transcribe_audio(wav_file_path):
    recognizer = sr.Recognizer()
    # Load the WAV audio file
    with sr.AudioFile(wav_file_path) as source:
        audio = recognizer.record(source)
    # Recognize speech using Google Web Speech API
    transcription = recognizer.recognize_google(audio)
    return transcription

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: transcribe.exe <input_mp3_file>")
        sys.exit(1)

    mp3_file_path = sys.argv[1]
    wav_file_path = mp3_file_path.replace(".mp3", ".wav")
    txt_file_path = mp3_file_path.replace(".mp3", ".txt")

    try:
        # Step 1: Convert MP3 to WAV
        convert_mp3_to_wav(mp3_file_path, wav_file_path)

        # Step 2: Transcribe the WAV file
        transcription = transcribe_audio(wav_file_path)

        # Step 3: Write the transcription to a text file
        with open(txt_file_path, "w") as txt_file:
            txt_file.write(transcription)

        print(f"Transcription saved to {txt_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
