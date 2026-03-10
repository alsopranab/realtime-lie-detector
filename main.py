import sounddevice as sd
import numpy as np
import queue
import tkinter as tk
from analyzer import compute_stress

SAMPLE_RATE = 22050
BLOCK_SIZE = 2048

audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    audio_queue.put(indata.copy())

root = tk.Tk()
root.title("Real-Time Voice Stress Monitor")

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

bar = canvas.create_rectangle(50, 100, 50, 140, fill="green")

label = tk.Label(root, text="Stress Level: Calm", font=("Arial",14))
label.pack()

def update_meter():

    try:

        audio = audio_queue.get_nowait()

        stress = compute_stress(audio.flatten(), SAMPLE_RATE)

        stress = min(stress,100)

        width = 50 + (stress * 3)

        canvas.coords(bar,50,100,width,140)

        if stress < 30:
            canvas.itemconfig(bar, fill="green")
            label.config(text="Stress Level: Calm")

        elif stress < 60:
            canvas.itemconfig(bar, fill="yellow")
            label.config(text="Stress Level: Nervous")

        else:
            canvas.itemconfig(bar, fill="red")
            label.config(text="Stress Level: High Stress")

    except:
        pass

    root.after(100, update_meter)

stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    blocksize=BLOCK_SIZE,
    channels=1,
    callback=audio_callback
)

stream.start()

update_meter()

root.mainloop()