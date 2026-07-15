# 🎓 SmartCampusAI

SmartCampusAI is a modern AI-powered campus management platform built with Streamlit. It provides secure user authentication, an interactive dashboard, student profile management, campus announcements, and AI assistant integration.

---

## 🚀 Features

### 🔐 Authentication

* User Registration
* User Login
* Secure Password Hashing
* Session Management
* Logout Functionality
* Input Validation

### 📊 Dashboard

* Personalized Welcome Screen
* User Statistics
* Recent Activity Overview
* Campus Announcements
* AI Assistant Integration
* Responsive Sidebar Navigation

### 👤 Profile Management

* View Profile
* Update User Information
* Account Settings

### 🤖 AI Integration

* OpenAI API Integration
* Secure API Key Management using `.env`
* AI-powered campus assistance

### 🎨 Modern UI

* Glassmorphism Design
* Responsive Layout
* Dark/Light Theme Support
* Custom CSS Styling
* Interactive Dashboard Components

### 💾 Database

* Lightweight JSON Database
* Easy Data Management
* No External Database Required

---

## 📁 Project Structure

```text
SmartCampusAI/
│
├── app.py
├── database.json
├── .env
├── requirements.txt
│
├── pages/
│   ├── login.py
│   ├── register.py
│   ├── dashboard.py
│   ├── profile.py
│   └── settings.py
│
├── utils/
│   ├── auth.py
│   ├── database.py
│   ├── ai_helper.py
│   └── styles.py
│
├── assets/
│   └── logo.png
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SmartCampusAI.git
cd SmartCampusAI
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

Never commit your `.env` file to GitHub.

---

## 💾 JSON Database

The application uses a JSON file as the database.

Example:

```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "password": "hashed_password",
      "created_at": "2026-01-01"
    }
  ]
}
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 📦 Requirements

```txt
streamlit
python-dotenv
bcrypt
pandas
numpy
requests
streamlit-option-menu
streamlit-extras
plotly
openai
Pillow
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🌐 Deployment

### Streamlit Community Cloud

1. Push project to GitHub.
2. Login to Streamlit Cloud.
3. Create a new app.
4. Connect GitHub repository.
5. Add secrets:

```toml
OPENAI_API_KEY="your_api_key"
```

6. Deploy.

### Render

1. Connect GitHub Repository.
2. Build Command:

```bash
pip install -r requirements.txt
```

3. Start Command:

```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### Railway

1. Connect Repository.
2. Add Environment Variables.
3. Deploy Automatically.

---

## 🔒 Security Features

* Password Hashing using bcrypt
* Secure Session Handling
* Environment Variable Protection
* Input Validation
* Authentication Checks
* Protected Dashboard Access

---

## 🛠️ Tech Stack

* Streamlit
* Python
* OpenAI API
* JSON Database
* bcrypt
* Plotly
* Pandas
* NumPy

---

## 🎯 Future Enhancements

* Student Attendance Tracking
* Faculty Dashboard
* Assignment Management
* Notice Board System
* Role-Based Access Control
* Analytics Dashboard
* PostgreSQL Integration
* Mobile Responsive Improvements

---

## 👨‍💻 Author

Developed as a modern AI-powered campus management solution using Streamlit and OpenAI technologies.

---

## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and development purposes.
