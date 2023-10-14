import tkinter as tk
from tkinter import filedialog
import os
import moviepy.editor as mp


def convert_video_audio():
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    
    if not video_path:
        return
    
    output_folder = "audio_convertido"
    os.makedirs(output_folder, exist_ok=True)
    
    file_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_folder, f"{file_name}.wav")
    
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    
    result_label.config(text=f"Audio convertido: {audio_path}")
    reset_button.config(state=tk.NORMAL)

def reset():
    result_label.config(text="")
    reset_button.config(state=tk.DISABLED)

def quit():
    window.quit()

window = tk.Tk()
window.title("Convertir Video a Audio")

window.iconbitmap("img/icono.ico")

window.geometry("400x250")

bg_image = tk.PhotoImage(file="img/background_image.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1) 

convert_button = tk.Button(window, text="Cargar Video y Convertir", command=convert_video_audio)
convert_button.pack(pady=10)


result_label = tk.Label(window, text="", wraplength=350)
result_label.pack()

reset_button = tk.Button(window, text="Reiniciar", command=reset, state=tk.DISABLED)  # Inicialmente deshabilitado
reset_button.pack(pady=10)

quit_button = tk.Button(window, text="Salir", command=quit)
quit_button.pack(pady=10)

window.mainloop()
