import streamlit as st
import time
from utils.auth import hash_password, verify_password, validate_password_strength
from utils.database import load_users, save_users

def show():
    """Renders the settings configuration view for theme adjustments and security options."""
    user = st.session_state.user
    
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h1 style="margin: 0; font-size: 2.2rem; background: linear-gradient(135deg, #f43f5e 0%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Application Settings ⚙️
            </h1>
            <p style="color: #94a3b8; margin: 4px 0 0 0;">Customize application behavior and security configurations</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # App preferences container
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-top:0; color: #f43f5e;">Preferences</h3>', unsafe_allow_html=True)
        
        # Theme toggle (Light/Dark)
        current_theme = st.session_state.theme
        theme_index = 0 if current_theme == "Dark" else 1
        theme_choice = st.radio("App Visual Theme", ["Dark", "Light"], index=theme_index, horizontal=True)
        
        if theme_choice != current_theme:
            st.session_state.theme = theme_choice
            st.success(f"Theme changed to {theme_choice} mode!")
            time.sleep(0.5)
            st.rerun()
            
        st.markdown('<hr style="border-color: rgba(255,255,255,0.08); margin: 20px 0;"/>', unsafe_allow_html=True)
        
        # Notification toggles
        st.write("**Notification Alerts**")
        email_alerts = st.checkbox("Email alerts for library reservations", value=True)
        campus_announcements = st.checkbox("Notify me about new campus announcements", value=True)
        ai_tips = st.checkbox("Receive weekly personalized AI study recommendations", value=False)
        
        if st.button("Save Preferences", key="save_pref_btn"):
            st.success("App preferences saved successfully!")
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        # Security Password updates
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-top:0; color: #ec4899;">Change Password</h3>', unsafe_allow_html=True)
        
        with st.form("change_password_form", clear_on_submit=True):
            current_pwd = st.text_input("Current Password", type="password")
            new_pwd = st.text_input("New Password", type="password")
            confirm_new_pwd = st.text_input("Confirm New Password", type="password")
            
            submit_btn = st.form_submit_button("Update Password")
            
            if submit_btn:
                # Check empty
                if not current_pwd or not new_pwd or not confirm_new_pwd:
                    st.error("Please fill in all security fields.")
                else:
                    # Retrieve fresh user data to verify password
                    users = load_users()
                    user_record = next((u for u in users if u["email"] == user["email"]), None)
                    
                    if not user_record or not verify_password(current_pwd, user_record["password"]):
                        st.error("Your current password was entered incorrectly.")
                    else:
                        # Verify new password parameters
                        is_valid, err_msg = validate_password_strength(new_pwd, confirm_new_pwd)
                        if not is_valid:
                            st.error(err_msg)
                        elif current_pwd == new_pwd:
                            st.error("New password cannot be the same as your current password.")
                        else:
                            with st.spinner("Encrypting and updating password..."):
                                time.sleep(1.0)
                                # Hash and save password
                                hashed = hash_password(new_pwd)
                                user_record["password"] = hashed
                                
                                # Update users list
                                for idx, u in enumerate(users):
                                    if u["email"] == user["email"]:
                                        users[idx] = user_record
                                        break
                                        
                                if save_users(users):
                                    st.success("Password changed successfully!")
                                else:
                                    st.error("Error writing password to database.")
                                    
        st.markdown('</div>', unsafe_allow_html=True)
