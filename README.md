
# Emotion Detection Mobile App

This Python script is part of a mobile app developed using the Kivy framework for recording and analyzing users' voices to determine their emotional state. The app utilizes the `python_speech_features` library for extracting Mel-Frequency Cepstral Coefficients (MFCC) and Log Filter Bank energies from recorded audio signals.

## Prerequisites

Before running the script, make sure you have the following installed:

- **Python:** The script is written in Python. You can download it from [python.org](https://www.python.org/).
- **Kivy:** The Kivy framework is used for developing multi-touch applications. Install it using:

  ```bash
  pip install kivy
  ```

- **NumPy, Matplotlib, SciPy:** These libraries are used for numerical operations, plotting, and reading audio files. Install them using:

  ```bash
  pip install numpy matplotlib scipy
  ```

- **python_speech_features:** Install this library for extracting MFCC and Log Filter Bank features:

  ```bash
  pip install python_speech_features
  ```

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/emotion-detection-app.git
   cd emotion-detection-app
   ```

2. Ensure that you have the required audio dataset in the 'Dataset/' directory. The dataset should contain subdirectories for different emotion categories.

3. Run the script:

   ```bash
   python emotion_detection_app.py
   ```

   This script iterates through the audio files, extracts MFCC features, and generates corresponding visualizations saved in the 'figs/' directory.

## Script Structure

- **emotion_detection_app.py:** The main script that reads audio files, extracts MFCC features, and generates visualizations.

- **Dataset/:** The directory containing audio files categorized by emotions.

- **figs/:** The directory where the generated MFCC visualizations are saved.

## Important Note

- This script is a part of a larger mobile app. Ensure you have the complete mobile app setup, including the user interface for recording and processing audio.

- The accuracy of emotion detection depends on the quality and diversity of the training dataset.

---