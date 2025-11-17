# 🧘 Cutie's Focus Room

**An AI-powered focus and productivity companion that helps you stay focused, track your emotions, and build better work habits.**

Cutie's Focus Room combines natural language processing, real-time emotion detection, and distraction monitoring to create a personalized productivity experience. Simply tell it how you want to focus, and it will set up a smart timer, monitor your emotional state via webcam, detect phone distractions, and provide insights to help you improve your focus sessions.

---

## ✨ Features

- **🤖 AI-Powered Timer Configuration**: Use natural language to set up your focus sessions (e.g., "focus for 25 minutes with 5-minute breaks every 5 minutes")
- **😊 Real-Time Emotion Detection**: Tracks your emotional state (angry, stressed, happy, sad, focused) during work sessions using webcam analysis
- **📱 Distraction Detection**: Automatically detects when you're using your phone and tracks distractions
- **⏰ Smart Focus/Rest Timer**: Alternates between focused work periods and rest breaks with intelligent notifications
- **📊 Session Analytics**: View trends and patterns across your focus sessions
- **💡 Personalized Productivity Advice**: Get AI-generated insights based on your session history
- **🔔 Real-Time Notifications**: Receive browser notifications for timer events and break reminders
- **📹 Live Video Streaming**: See your real-time emotion detection and phone detection overlays in the browser

---

## 🛠️ Tech Stack

- **Backend**: Python 3.13
- **Web Framework**: FastAPI
- **AI/ML**:
  - Google Gemini 2.5 Flash (natural language processing)
  - DeepFace (emotion detection)
  - YOLOv8 (object detection for phone distractions)
- **Computer Vision**: OpenCV
- **Database**: SQLite
- **Real-Time Communication**: WebSockets
- **Frontend**: HTML, CSS, JavaScript (vanilla)

---

## 📋 Prerequisites

- Python 3.13+ (or Python 3.8+)
- Webcam/camera access
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- A modern web browser with WebSocket support

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Cutie-sFocusRoom.git
cd Cutie-sFocusRoom
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn websockets
pip install google-generativeai
pip install deepface
pip install ultralytics
pip install opencv-python
pip install pydantic
```

Or install from the requirements file (if available):

```bash
pip install -r venv/requirements.txt
```

**Note**: DeepFace and YOLO will download their model files automatically on first use. This may take a few minutes.

### 4. Download YOLO Model

The YOLOv8 model file (`yolov8n.pt`) should already be in the repository root. If it's missing, it will be downloaded automatically on first run.

### 5. Configure API Key

Open `.backend/main.py` and `.frontend/main.py`, and replace the Gemini API key with your own:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

**Important**: For production use, consider using environment variables instead of hardcoding API keys.

---

## 🎮 Usage

### Starting the Server

1. **Activate your virtual environment** (if not already activated):
   ```bash
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate  # Windows
   ```

2. **Navigate to the frontend directory**:
   ```bash
   cd .frontend
   ```

3. **Start the FastAPI server**:
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000
   ```

4. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000
   ```

### Using the Application

1. **Set Up Your Focus Session**:
   - Type a natural language request in the input field, such as:
     - "Focus for 30 minutes with 5-minute breaks every 10 minutes"
     - "Work for 25 minutes, rest for 5 minutes, repeat every 5 minutes"
     - "I want to focus for 1 hour with 10-minute breaks every 20 minutes"
   - Click "Start Focus Session" or press Enter

2. **Grant Permissions**:
   - Allow camera access when prompted (required for emotion detection)
   - Allow browser notifications (optional but recommended for timer alerts)

3. **Monitor Your Session**:
   - Watch the live video feed showing your detected emotions and phone usage
   - View real-time emotion counts and distraction tracking
   - See timer status and remaining time

4. **Review Your Progress**:
   - After completing sessions, view trends and analytics
   - Get personalized productivity advice based on your session history

---

## 📁 Project Structure

```
Cutie's Focus Room/
├── .backend/                 # Backend Python modules
│   ├── main.py              # Gemini AI integration & timer configuration
│   ├── EmotionDetection.py  # Webcam emotion & phone detection
│   ├── FocusRestReminders.py # Timer logic & notifications
│   ├── NotificationSender.py # WebSocket notification system
│   ├── Memory.db            # SQLite database (session data)
│   ├── SessionSummary.py    # Session analysis utilities
│   └── TrendDashboard.py    # Analytics utilities
├── .frontend/                # Frontend web application
│   ├── main.py              # FastAPI server & API endpoints
│   └── static/
│       └── index.html       # Web UI
├── venv/                     # Virtual environment
├── yolov8n.pt               # YOLO model file
└── README.md                # This file
```

---

## 🔌 API Endpoints

### REST API

- `POST /query` - Process natural language focus request
  - Body: `{"query": "focus for 25 minutes..."}`
  - Returns: Gemini response with parsed timer settings

- `POST /api/timer/start` - Start the focus/rest timer
  - Returns: Timer status and settings

- `GET /api/timer/status` - Get current timer configuration
- `GET /api/timer/state` - Get current timer state (running, phase, time remaining)
- `GET /api/sessions` - Get all session data for analytics
- `POST /api/advice` - Get AI-generated productivity advice
  - Body: `{"sessions": [...]}`
- `GET /api/notifications/status` - Check WebSocket connection status

### WebSocket Endpoints

- `ws://localhost:8000/ws/notifications` - Real-time notifications
- `ws://localhost:8000/ws/video` - Live video stream with emotion/distraction data

---

## 🧠 How It Works

1. **Natural Language Processing**: When you submit a focus request, the backend uses Google Gemini AI to parse your natural language and extract:
   - Total focus duration
   - Break frequency (how often to take breaks)
   - Break duration (length of each break)

2. **Timer System**: The `FocusRestReminders` module manages alternating focus and rest periods, sending notifications at key moments (timer start, break warnings, completion).

3. **Emotion Detection**: The `EmotionDetection` module:
   - Captures frames from your webcam
   - Uses DeepFace to analyze facial expressions and detect emotions
   - Uses YOLOv8 to detect phone usage
   - Streams annotated frames to the browser via WebSocket
   - Tracks emotion counts and distractions in real time

4. **Data Persistence**: Session data (emotion counts, distractions) is saved to SQLite database for trend analysis.

5. **Insights Generation**: Historical session data is analyzed by Gemini AI to provide personalized productivity advice.

---

## 🐛 Troubleshooting

### Camera Not Working

- **Check permissions**: Ensure your browser has camera access permissions
- **Check camera availability**: Make sure no other application is using the camera
- **Try different camera index**: The code tries camera indices 0, 1, and 2 automatically

### Emotion Detection Not Working

- **Ensure good lighting**: Emotion detection works best with adequate lighting
- **Face the camera**: Make sure your face is visible to the camera
- **Check DeepFace installation**: First run will download models (may take time)

### API Key Issues

- **Verify API key**: Ensure your Gemini API key is correct and has quota remaining
- **Check API key location**: Make sure the key is set in both `.backend/main.py` and `.frontend/main.py`

### WebSocket Connection Issues

- **Check browser console**: Look for WebSocket connection errors
- **Verify server is running**: Ensure the FastAPI server is running on port 8000
- **Check firewall**: Ensure port 8000 is not blocked

### Timer Not Starting

- **Check timer configuration**: Ensure focus, rest, and repeat times are set (not 0)
- **Check console logs**: Look for error messages in the terminal

---

## 🔒 Privacy & Security

- **Local Processing**: All emotion detection and video processing happens locally on your machine
- **No Cloud Storage**: Session data is stored locally in SQLite database
- **API Key**: Keep your Gemini API key secure and don't commit it to version control
- **Camera Access**: Camera access is only used for emotion detection and is not recorded or transmitted

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [Google Gemini](https://deepmind.google/technologies/gemini/) for natural language processing
- [DeepFace](https://github.com/serengil/deepface) for emotion detection
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) for object detection
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework

---

## 📧 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Happy Focusing! 🎯✨**

