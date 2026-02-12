# Silent Speech Recognition System

Silent Speech Recognition (SSR) is a cutting-edge system designed to empower individuals who cannot speak by enabling communication through visual lip movements. This project showcases an intelligent interface for uploading and processing silent speech videos using a deep learning-based recognition model built with CNN + BiLSTM + CTC decoding.

## 🚀 Features

- **Hero Section**: Bold introduction to Silent Speech Recognition with a call-to-action button.
- **About & Technology**: Overview of the deep learning pipeline and visual speech recognition architecture.
- **AI-Powered Prediction**: CNN + BiLSTM + CTC model for silent speech decoding.
- **Video Upload Interface**: Dedicated page for users to upload silent speech videos.
- **Automatic Lip Detection**: MediaPipe-based mouth region extraction for precise preprocessing.
- **Responsive Design**: Fully optimized for desktop and mobile devices.

## 🛠 Tech Stack

- **React** (with Hooks)
- **Tailwind CSS** for styling
- **Flask** for backend API
- **PyTorch** for deep learning model implementation
- **MediaPipe & OpenCV** for video preprocessing
- **Git & GitHub** for version control
- **VS Code** as the development environment

## 📁 Project Structure


## 🔧 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Geevar12/SSR.git
   cd SSR
2. Install frontend dependencies:
   ```bash
   npm install
3. Install backend dependencies:
   ```bash
   pip install -r src/backend/requirements.txt
4. Run backend locally:
    ```bash
    cd src/backend
   python app.py
5. Run frontend:
    ```bash
    npm run dev
