# 🖐️ Sign Language Recognition System

A real-time sign language recognition and translation system using Computer Vision and Machine Learning. Recognizes hand gestures (A-Z, 0-9, and custom signs), translates them to text, and converts to speech in multiple Indian languages.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Features

- ✅ **Real-time Hand Gesture Recognition** - 30 FPS webcam processing
- ✅ **36+ Gesture Classes** - A-Z, 0-9, plus custom gestures
- ✅ **95% Accuracy** - Using Random Forest Classifier
- ✅ **Multi-Language Translation** - Hindi, Bengali, Telugu, Gujarati
- ✅ **Text-to-Speech** - Audio output in translated language
- ✅ **Easy Dataset Expansion** - Tools to add new gestures
- ✅ **Multiple ML Models** - Random Forest, SVM, KNN implementations

## 🚀 Demo

### Real-Time Recognition
Perform hand gestures in front of your webcam and see instant recognition with audio feedback.

### Translation Feature
Spell out words using sign language, translate to Indian languages, and hear the translation.

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Adding New Gestures](#adding-new-gestures)
- [Model Training](#model-training)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- Webcam
- Windows/Linux/MacOS

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Ashutosh22053585/sign-language-recognition.git
cd sign-language-recognition
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the dataset** (optional - or create your own)
```bash
# Place your dataset in the 'datasets' folder
# Or use the provided scripts to create your own
```

## ⚡ Quick Start

### 1. Real-Time Recognition

```bash
python step5RFC.py
```

Perform gestures in front of your webcam and see instant recognition!

### 2. Translation Demo

```bash
python step6.py
```

Spell out words and translate to Indian languages.

### 3. GUI Application

```bash
python Final.py
```

User-friendly interface with all features.

## 📁 Project Structure

```
sign-language-recognition/
├── step1.py                    # Hand landmark visualization
├── step2.py                    # Feature extraction & dataset creation
├── step3.py                    # Data validation
├── step4RFC.py                 # Random Forest model training
├── step5RFC.py                 # Real-time recognition
├── step6.py                    # Multi-language translation
├── Final.py                    # GUI application
├── add_training_data.py        # Add images to existing gestures
├── add_new_gestures.py         # Add new gesture classes
├── add_downloaded_images.py    # Import downloaded datasets
├── update_labels.py            # Update labels automatically
├── data_padded.pickle          # Preprocessed dataset
├── model.p                     # Trained Random Forest model
├── SVM/                        # SVM implementation
│   ├── SVM.py
│   ├── SVMfinal.py
│   └── SVMmodel.p
├── KNN/                        # KNN implementation
│   ├── KNN.py
│   ├── KNNfinal.py
│   └── KNNmodel.p
├── DataForRecognition/         # Runtime gesture capture
└── requirements.txt            # Python dependencies
```

## 📖 Usage

### Step-by-Step Pipeline

#### 1. **Visualize Hand Detection**
```bash
python step1.py
```
Verify MediaPipe can detect hands in your images.

#### 2. **Create Dataset**
```bash
python step2.py
```
Extract features from images and create training dataset.

#### 3. **Validate Data**
```bash
python step3.py
```
Check dataset integrity.

#### 4. **Train Model**
```bash
python step4RFC.py
```
Train Random Forest classifier and view accuracy metrics.

#### 5. **Real-Time Recognition**
```bash
python step5RFC.py
```
Test the model with live webcam feed.

#### 6. **Translation System**
```bash
python step6.py
```
Capture gesture sequences and translate to Indian languages.

## 🎨 Adding New Gestures

### Add Images to Existing Gestures

```bash
python add_training_data.py
```

Select a gesture (A-Z, 0-9) and capture more images to improve accuracy.

### Add New Gesture Classes

```bash
python add_new_gestures.py
```

Create new gestures like HELLO, PEACE, THANK_YOU, etc.

### Import Downloaded Images

```bash
python add_downloaded_images.py
```

Add images from Kaggle or other datasets.

### After Adding Images

```bash
# Regenerate dataset
python step2.py

# Retrain model
python step4RFC.py

# Test improvements
python step5RFC.py
```

## 🧠 Model Training

### Random Forest (Primary Model)

```bash
python step4RFC.py
```

- **Accuracy:** ~95%
- **Inference Speed:** 30 FPS
- **Model Size:** 25 MB

### SVM (Alternative)

```bash
cd SVM
python SVM.py
```

- **Accuracy:** ~92%
- **Best for:** Smaller datasets

### KNN (Baseline)

```bash
cd KNN
python KNN.py
```

- **Accuracy:** ~88%
- **Best for:** Quick prototyping

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Programming language |
| **OpenCV** | Image processing and webcam capture |
| **MediaPipe** | Hand landmark detection |
| **scikit-learn** | Machine learning (Random Forest, SVM, KNN) |
| **NumPy** | Numerical computations |
| **Matplotlib** | Data visualization |
| **Seaborn** | Confusion matrix heatmaps |
| **Google Translate API** | Text translation |
| **gTTS** | Text-to-speech |
| **pyttsx3** | Real-time speech synthesis |
| **Tkinter** | GUI development |

## 📊 Results

### Model Performance

| Model | Accuracy | Inference Time | Model Size |
|-------|----------|----------------|------------|
| Random Forest | 95% | 33ms | 25 MB |
| SVM | 92% | 45ms | 1.3 MB |
| KNN | 88% | 60ms | 1.8 MB |

### Gesture Recognition

- **Total Gestures:** 36+ (A-Z, 0-9, custom)
- **FPS:** 30 frames per second
- **Languages:** 4 (Hindi, Bengali, Telugu, Gujarati)

### Confusion Matrix

Most gestures are recognized with >95% accuracy. Common confusions:
- M ↔ N (similar hand shapes)
- U ↔ V (similar finger positions)

## 🎓 How It Works

### 1. **Hand Detection**
MediaPipe detects 21 landmarks on each hand (fingertips, knuckles, wrist, palm).

### 2. **Feature Extraction**
Extract (x, y) coordinates of landmarks → 42 features per hand.

### 3. **Normalization**
Subtract minimum x and y values to make features position-independent.

### 4. **Padding**
Pad to 84 features to handle 1-2 hands consistently.

### 5. **Classification**
Random Forest predicts the gesture class.

### 6. **Translation & Speech**
Translate recognized text to target language and generate audio.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- Add more gesture classes
- Improve model accuracy
- Add more languages
- Create mobile app version
- Add dynamic gesture recognition (motion-based signs)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ashutosh Om Pattanaik**
- GitHub: [@Ashutosh22053585](https://github.com/Ashutosh22053585)
- LinkedIn: [Ashutosh Om Pattanaik](https://www.linkedin.com/in/ashutosh-om-pattanaik-557973261)

## 🙏 Acknowledgments

- MediaPipe team for the hand detection model
- scikit-learn for machine learning tools
- Sign language community for gesture references
- Kaggle for datasets

## 📧 Contact

For questions or feedback, please open an issue on GitHub or connect with me on LinkedIn.

---

**⭐ If you find this project useful, please consider giving it a star!**
