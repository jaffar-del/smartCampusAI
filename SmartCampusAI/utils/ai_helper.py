import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load dotenv to read the API key
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if the API key is set and is not a placeholder
HAS_REAL_KEY = (
    OPENAI_API_KEY is not None 
    and len(OPENAI_API_KEY) > 20 
    and not OPENAI_API_KEY.startswith("your_api_key")
)

def get_openai_client():
    """Initializes and returns the OpenAI client if key is configured, else None."""
    if HAS_REAL_KEY:
        try:
            return OpenAI(api_key=OPENAI_API_KEY)
        except Exception:
            return None
    return None

def get_offline_response(prompt: str) -> str:
    """
    Returns a high-quality local mock response for testing when 
    the OpenAI API Key is missing or invalid.
    """
    p = prompt.lower()
    
    if "library" in p or "hours" in p:
        return (
            "📚 **Campus Library Hours & Info:**\n\n"
            "The Campus Main Library is open:\n"
            "- **Monday - Friday:** 8:00 AM - 10:00 PM\n"
            "- **Saturday & Sunday:** 10:00 AM - 6:00 PM\n\n"
            "Study rooms can be reserved on the second floor via the SmartCampus Portal. "
            "Need quiet space? The 3rd and 4th floors are designated silent study zones."
        )
    elif "wifi" in p or "internet" in p or "connect" in p:
        return (
            "📶 **Wi-Fi Connectivity Guide:**\n\n"
            "To connect to the high-speed campus internet:\n"
            "1. Select the Wi-Fi network named **'SmartCampus-Secure'**.\n"
            "2. Log in using your campus email address and password.\n"
            "3. Accept the security certificate if prompted.\n\n"
            "For visitors, **'SmartCampus-Guest'** is available with basic web browsing capabilities (no password required)."
        )
    elif "cafeteria" in p or "food" in p or "dining" in p or "eat" in p:
        return (
            "🍔 **Campus Dining & Cafeterias:**\n\n"
            "- **Student Union Dining Hall:** Open 7:30 AM - 8:00 PM. Serving hot meals, salad bar, and vegan specialties.\n"
            "- **ByteSized Cafe (Library Lobby):** Open 24/7. Perfect for late-night coffee, snacks, and fresh sandwiches.\n"
            "- **Greenhouse Bistro:** Open 11:00 AM - 4:00 PM. Focused on organic salads and local farm-to-table cuisine."
        )
    elif "parking" in p or "permit" in p or "car" in p:
        return (
            "🚗 **Parking & Permit Rules:**\n\n"
            "All vehicles parked on campus must display a valid permit. \n"
            "- **Student Permits:** Valid for Zones A, B, and C ($45 per semester).\n"
            "- **Day Passes:** Available for $5 at the entry kiosks.\n"
            "Apply online through the Student Portal or visit the Campus Security office located in Building D (Room 102)."
        )
    elif "exam" in p or "schedule" in p or "midterm" in p or "final" in p:
        return (
            "📅 **Academic Exam Information:**\n\n"
            "The examination schedule for Summer 2026 is as follows:\n"
            "- **Midterms:** August 3 - August 8, 2026\n"
            "- **Final Exams:** September 14 - September 19, 2026\n\n"
            "Individual room assignments and time slots are sent via email by your department. Make sure to bring your Student ID card to all examinations."
        )
    elif "contact" in p or "help" in p or "support" in p or "phone" in p or "email" in p:
        return (
            "📞 **Important Campus Contacts:**\n\n"
            "- **Campus Registrar:** registrar@smartcampus.edu | (555) 019-9230 (Admin building, room 201)\n"
            "- **Student Health Center:** health@smartcampus.edu | (555) 019-9400 (Student Center, room 105)\n"
            "- **IT Helpdesk:** support@smartcampus.edu | (555) 019-9911 (Science Center, room 310)\n"
            "- **Campus Security (Emergencies):** (555) 019-9111"
        )
    else:
        return (
            "🤖 **SmartCampus AI Assistant (Offline Mode)**\n\n"
            "Hello! I am your AI campus assistant. Currently, I am running in **Offline Mode** "
            "because a valid `OPENAI_API_KEY` was not detected in the `.env` configuration file.\n\n"
            "However, I can still assist you with general campus inquiries! Try asking me about:\n"
            "- **Library hours**\n"
            "- **How to connect to the Wi-Fi**\n"
            "- **Cafeteria and food options**\n"
            "- **Parking permits**\n"
            "- **Exam schedules and academic calendars**\n"
            "- **Campus contact numbers**\n\n"
            "To activate my full generative intelligence, add your OpenAI API key to the `.env` file and restart the application."
        )

def ask_campus_ai(prompt: str, history: list = None) -> str:
    """
    Sends the user's prompt to OpenAI GPT, maintaining campus persona.
    If API key is missing or an error occurs, falls back to the offline response.
    """
    if history is None:
        history = []
        
    client = get_openai_client()
    if not client:
        return get_offline_response(prompt)
        
    try:
        # Build chat messages
        system_message = {
            "role": "system",
            "content": (
                "You are SmartCampusAI, a premium administrative and support chatbot for students "
                "and faculty at SmartCampus. Keep your tone professional, friendly, helpful, and concise. "
                "You have access to information regarding library hours, wifi configurations, dining options, "
                "parking details, exam structures, and contact information. Answer based on this persona."
            )
        }
        
        messages = [system_message]
        # Append history if any (history should be list of dicts with role and content)
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})
            
        messages.append({"role": "user", "content": prompt})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API Exception: {e}")
        # Fall back to local database mapping
        return f"*(Fallback Offline Answer due to connection error: {str(e)})*\n\n" + get_offline_response(prompt)
