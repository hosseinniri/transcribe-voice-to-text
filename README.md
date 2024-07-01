# Transcribe Voice to Text for TOEFL Learners

This project provides a Python script that converts an MP3 audio file to WAV format and then transcribes the audio using Google's Web Speech API. The script is packaged into a single executable file using PyInstaller.

## Requirements

- Python 3.x
- `pydub` library
- `speechrecognition` library
- `ffmpeg` installed and added to system PATH

## Installation

1. Install necessary libraries:
   ```sh
   pip install pydub speechrecognition pyinstaller
    ```
   
2. Ensure ffmpeg is installed and added to the system PATH. You can download ffmpeg from here.


## Usage
Running the Script
   ```sh
    python transcribe.py <input_mp3_file>
   ```
## Creating an Executable
```sh
pyinstaller --onefile transcribe.py
```
## Running the Executable
```sh
transcribe.exe <input_mp3_file>
```

## Example
```sh
transcribe.exe example.mp3
```
This will generate a text file with the same base name as the input MP3 file containing the transcription.

## File Structure

transcribe.py: The main script for converting and transcribing audio files.

README.md: This file, providing an overview and usage instructions.
