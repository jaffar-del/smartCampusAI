# SmartCampusAI 🏫🤖

**SmartCampusAI** is a premium, deployment-ready Streamlit application that serves as an AI-powered hub for student administration and campus support. It features a modern visual design system implementing glassmorphism, clean responsive layouts, and interactive dark/light theme switching.

---

## Key Features

1. **Secure Session Authentication System**:
   - Register Page with inputs for Full Name, Email, Password, and Password Confirmation.
   - Live validation check for email formats, duplicate accounts, missing fields, and password strength (min. 6 characters).
   - Secure server-side hashing using `bcrypt`.
   - Robust persistent login state via Streamlit Session State.
2. **Glassmorphic Interactive Dashboard**:
   - Welcome banner with customized student name, active date, and student major.
   - Multi-metric visual grid tracking: Total Registered Users, Campus Safety Level, and Live Library Capacities.
   - Auto-updating interactive Plotly chart depicting predicted hourly library occupancy rates.
   - Badged Feed showing the latest Campus Announcements.
3. **Smart Campus AI Chatbot**:
   - Interactive chat window utilizing modern `openai` Python SDK.
   - Dedicated campus administration persona mapping hours, dining menus, Wi-Fi connections, and parking regulations.
   - Graceful **Offline Fallback Engine** that analyzes user queries locally using keywords if no OpenAI API Key is configured.
4. **Student Profile Editor**:
   - View student joining dates and enrollment status.
   - Update full name, edit major details, submit biographical profiles, and select customizable emoji avatars.
5. **Security & Preferences Control**:
   - Real-time Light & Dark mode toggle updates.
   - Email notifications and system alerts preference controls.
   - Complete password changes verifying historical hash correctness.

---

## File Structure

```text
SmartCampusAI/
│
├── app.py                     # Main application routing and entrypoint
├── database.json              # Local JSON database stores
├── .env                       # Local secrets configuration (API keys)
├── requirements.txt           # Main python dependency file
├── .streamlit/
│   └── config.toml            # Disables default routing sidebar
│
├── pages/
│   ├── __init__.py
│   ├── login.py               # Login components
│   ├── register.py            # User registration components
│   ├── dashboard.py           # Core admin dashboard
│   ├── profile.py             # User details editor
│   └── settings.py            # Security & system preferences
│
├── utils/
│   ├── __init__.py
│   ├── auth.py                # Password hashing, validation, session utilities
│   ├── database.py            # JSON CRUD file helpers
│   ├── ai_helper.py           # OpenAI SDK chat completion wrappers
│   └── styles.py              # CSS injector with Glassmorphic styles
│
├── assets/
│   └── logo.png               # AI generated logo icon
│
└── README.md                  # System instruction and documentation
```

---

## Installation & Running

Follow these steps to run the application locally:

### 1. Prerequisite
Ensure you have Python 3.9+ installed on your system.

### 2. Install Packages
Open your terminal in the `SmartCampusAI` directory and run:
```bash
pip install -r requirements.txt
```

### 3. Setup Secrets
Open the `.env` file and replace the placeholder API key with your actual OpenAI key:
```env
OPENAI_API_KEY=sk-proj-YourActualKeyHere...
```
*(Note: If left as is or empty, the AI chatbot will run in a smart offline rule-based mode).*

### 4. Run Application
Run the Streamlit server:
```bash
streamlit run app.py
```
The app will automatically open in a new tab at `http://localhost:8501`.

---

## JSON Database Schema

The users schema inside `database.json` maintains the following structure:
```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "password": "$2b$12$...",
      "created_at": "2026-07-14",
      "major": "Computer Science",
      "bio": "AI Research Student at SmartCampus",
      "avatar": "🎓"
    }
  ]
}
```
All details are updated securely in-place through transaction blocks.
