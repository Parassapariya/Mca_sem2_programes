import os
import eel
import subprocess
from engine.features import speak, playAssistantSound
from engine.auth import recognize  # Corrected spelling from 'recoganize'

def start():
    eel.init("www")

    playAssistantSound()

    @eel.expose
    def init():
        try:
            # Run device.bat from current directory
            bat_path = os.path.join(os.getcwd(), 'device.bat')
            subprocess.call([bat_path], shell=True)
            
            eel.hideLoader()
            speak("Ready for Face Authentication")
            
            # Authenticate via face recognition
            flag = recognize.AuthenticateFace()  # Use correct spelling
            
            if flag == 1:
                eel.hideFaceAuth()
                speak("Face Authentication Successful")
                eel.hideFaceAuthSuccess()
                speak("Hello, Welcome Sir, How can I Help You")
                eel.hideStart()
                playAssistantSound()
            else:
                speak("Face Authentication Failed")
                eel.showAuthError()  # Add this function in your frontend

        except Exception as e:
            speak(f"An error occurred: {str(e)}")
            print(f"Error: {str(e)}")

    try:
        # Use default browser instead of hardcoding Chrome
        eel.start('index.html', mode='chrome', host='localhost', port=8000, block=True)
    except EnvironmentError:
        # If Chrome isn't found, use default browser
        eel.start('index.html', mode='default', host='localhost', port=8000, block=True)

if __name__ == "__main__":
    start()