import pyaudio

def list_audio_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    
    print("Available audio devices:")
    for i in range(0, numdevices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        print(f"Device {i}: {device_info.get('name')} (Input Channels: {device_info.get('maxInputChannels')}, Output Channels: {device_info.get('maxOutputChannels')})")

if __name__ == "__main__":
    list_audio_devices()
