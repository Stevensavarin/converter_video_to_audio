# converter_video_to_audio
![image](https://github.com/Stevensavarin/converter_video_to_audio/assets/137004357/251c2af1-478d-45ee-b6a9-4f0cf5bb19d1)


Video to Audio Converter with User Interface
This Python program is a standalone video to audio converter with a graphical user interface. It allows users to convert the audio track of a selected MP4 video file to the WAV format.

Main Functionality
Convert Video to Audio: Click the "Load Video and Convert" button to choose an MP4 video file. The program will extract the audio from the video and save it as a WAV file in a folder named "audio_converted." The path to the converted audio file will be displayed.

Reset: Clicking the "Reset" button clears the result message and re-enables the conversion button.

Requirements
The program utilizes the following Python libraries:

tkinter: Used for creating the graphical user interface.
moviepy: Utilized for video and audio processing.
Usage
Run the main.py script.
A window with the graphical user interface will appear.
Click the "Load Video and Convert" button to select an MP4 video file.
The program will carry out the conversion process and provide feedback on the location of the resulting audio file.
Use the "Reset" button to clear the message and restart the conversion or exit the application using the "Exit" button.
Code Structure
The entire code is located within main.py for simplicity, combining both user interface creation and program logic.
Notes
Ensure that you have the image files "img/icono.ico" and "img/background_image.png" in the same folder as main.py. These images are used for the window icon and the user interface background.

This description is adapted to the structure where all code is in the main.py file. Please adjust it further if needed and include additional information as required.
