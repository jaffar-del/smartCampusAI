import json
import os
from datetime import datetime

# Resolve the absolute path to database.json relative to this file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database.json")

def load_users():
    """Loads all users from the JSON database file. Returns a list of user dicts."""
    if not os.path.exists(DB_PATH):
        # Create default empty database if it doesn't exist
        save_users([])
        return []
    try:
        with open(DB_PATH, "r") as f:
            data = json.load(f)
            return data.get("users", [])
    except Exception as e:
        print(f"Error loading database: {e}")
        return []

def save_users(users_list):
    """Saves the users list back to the JSON database."""
    try:
        with open(DB_PATH, "w") as f:
            json.dump({"users": users_list}, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving database: {e}")
        return False

def create_user(name, email, password):
    """Creates a new user record, hashes password, and saves to JSON."""
    from utils.auth import hash_password
    users = load_users()
    
    # Calculate next ID
    next_id = 1
    if users:
        next_id = max(user["id"] for user in users) + 1
        
    hashed_pwd = hash_password(password)
    
    new_user = {
        "id": next_id,
        "name": name,
        "email": email.strip().lower(),
        "password": hashed_pwd,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "major": "Undeclared",
        "bio": "No bio written yet.",
        "avatar": "👤"
    }
    
    users.append(new_user)
    if save_users(users):
        return new_user
    return None

def authenticate_user(email, password):
    """Verifies user credentials. Returns user details if valid, otherwise None."""
    from utils.auth import verify_password
    users = load_users()
    email_clean = email.strip().lower()
    
    for user in users:
        if user["email"] == email_clean:
            if verify_password(password, user["password"]):
                return user
    return None

def update_profile(email, updated_fields):
    """Updates user information in the JSON file based on email."""
    users = load_users()
    email_clean = email.strip().lower()
    updated = False
    
    for user in users:
        if user["email"] == email_clean:
            for key, val in updated_fields.items():
                # Avoid overwriting id and email
                if key not in ["id", "email"]:
                    user[key] = val
            updated = True
            break
            
    if updated:
        save_users(users)
        return True
    return False
