import re
import bcrypt
import streamlit as st
from utils.database import load_users

def hash_password(password: str) -> str:
    """Hashes a password string using bcrypt and returns the decoded string."""
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def verify_password(password: str, hashed: str) -> bool:
    """Verifies a plain-text password against a hashed bcrypt password."""
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False

def validate_email(email: str) -> bool:
    """Validates if an email is in a correct structural email format."""
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(email_regex, email.strip()))

def is_duplicate_email(email: str) -> bool:
    """Checks if an email already exists in the JSON database."""
    users = load_users()
    email_clean = email.strip().lower()
    return any(user["email"] == email_clean for user in users)

def validate_password_strength(password: str, confirm_password: str) -> tuple[bool, str]:
    """
    Validates password strength and confirmation match.
    Returns (is_valid, error_message).
    """
    if not password:
        return False, "Password cannot be empty."
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    if password != confirm_password:
        return False, "Passwords do not match."
    return True, ""

def init_session_state():
    """Initializes standard session state keys for user session tracking."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user" not in st.session_state:
        st.session_state.user = None
    if "theme" not in st.session_state:
        st.session_state.theme = "Dark"
    if "page" not in st.session_state:
        st.session_state.page = "Login"

def login_user(user_data):
    """Stores logged-in user info in streamlit session state."""
    st.session_state.authenticated = True
    st.session_state.user = user_data
    st.session_state.page = "Dashboard"

def logout_user():
    """Clears user session details and routes user back to the login page."""
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.page = "Login"
    st.rerun()
