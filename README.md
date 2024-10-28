# face-recognition-registering-app
This is a face recognition web application built using Streamlit and DeepFace for registering and authenticating user faces. The app captures user images, stores them, and allows users to verify their identity based on previously registered images.

## Initial Features

- **Register Face**: Capture a face image to register it in the system.
- **Authenticate Face**: Capture a new image to verify if it matches the previously registered face.

## Tech Stack

- **Streamlit**: Used for building the interactive web application.
- **DeepFace**: Utilized for face recognition and verification.
- **OpenCV** and **Pillow**: For image processing and handling.

## Setup Instructions

0. **Install Required Libraries**
- pip install -r requirements.txt

1. **Run the App**:
   - git clone <repository-url>
   - cd <repository-name>
   - streamlit run .\camera.py
