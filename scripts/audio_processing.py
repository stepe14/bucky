from pydub import AudioSegment
import speech_recognition as sr
import os
import pyaudio

def list_audio_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print("*******************************************************************************************************************")
    print("Available audio devices:")
    for i in range(0, numdevices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        print(f"Device {i}: {device_info.get('name')} (Input Channels: {device_info.get('maxInputChannels')}, Output Channels: {device_info.get('maxOutputChannels')})")

def convert_audio_to_wav(input_file):
    """Convert audio file to WAV format using pydub."""
    audio = AudioSegment.from_file(input_file)
    output_file = os.path.splitext(input_file)[0] + '.wav'
    audio.export(output_file, format="wav")
    return output_file

def transcribe_audio(audio_file):
    """Transcribe speech from audio file using speech_recognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def record_and_transcribe(mic_index):
    """Record audio from the specified microphone and transcribe it."""
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=mic_index) as source:
        print("Please say something:")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == "__main__":
    # List available audio devices
    list_audio_devices()
    
    # Specify the device index for the microphone
    print("*******************************************************************************************************************")
    mic_index = int(input("Enter the device index for the microphone: "))
    print("*******************************************************************************************************************")
    
    # Option to process existing audio file
    input_file = "path/to/your/audiofile.flac"  # Replace with your audio file path
    if os.path.exists(input_file):
        wav_file = convert_audio_to_wav(input_file)
        transcription = transcribe_audio(wav_file)
        print("Transcription from file:", transcription)
    else:
        print("No audio file found. Recording from microphone instead.")
        transcription = record_and_transcribe(mic_index)
        print("Transcription from microphone:", transcription)
