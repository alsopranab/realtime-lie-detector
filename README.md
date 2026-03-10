# Real-Time Voice Stress Analyzer

A Python project that analyzes **live microphone input** to estimate **voice stress levels** using audio signal processing.

**Disclaimer**  
This project does **not detect lies directly**. It estimates **voice stress patterns** which may correlate with emotional tension.

---

## Features

- Real-time microphone monitoring
- Live voice stress meter
- Audio signal processing
- Voice pitch and energy analysis
- Interactive GUI visualization
- Continuous real-time analysis

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Signal processing |
| Librosa | Audio feature extraction |
| SoundDevice | Microphone input |
| Tkinter | GUI interface |
| Matplotlib | Visualization |

---

## Project Structure

```
realtime-lie-detector
│
├── main.py              # Main application
├── analyzer.py          # Stress analysis logic
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/realtime-lie-detector.git
```

### Navigate into the project folder

```bash
cd realtime-lie-detector
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python main.py
```

After running the script:

- A **GUI window** will appear
- Speak into the microphone
- The **stress meter updates in real time**

---

## How It Works

The system continuously captures audio from the microphone and analyzes it in small frames.

### Processing Pipeline

```
Microphone Input
      ↓
Audio Frame Processing
      ↓
Feature Extraction
      ↓
Stress Score Calculation
      ↓
Real-Time Visualization
```

### Voice Features Analyzed

- Pitch variation
- Energy fluctuations
- RMS amplitude
- Voice instability

Higher variability generally indicates **higher vocal stress**.

---

## Example Output

```
Stress Level: Calm
Stress Level: Nervous
Stress Level: High Stress
```

Example stress meter:

```
[██████████░░░░░░░░░░]
```

| Color | Meaning |
|---|---|
| 🟢 Green | Calm |
| 🟡 Yellow | Nervous |
| 🔴 Red | High Stress |

---

## Limitations

- Stress detection is **not equivalent to lie detection**
- Results depend on microphone quality
- Background noise may affect accuracy
- This is intended for **research / demonstration purposes**

---

## Future Improvements

- Polygraph-style waveform visualization
- Emotion classification (calm / nervous / angry)
- Machine learning based stress prediction
- Interview mode for response analysis
- Dataset-based training

---

## Author

**Pranab Debnath**

---

## Support

If you like this project, consider **starring the repository** on GitHub.
