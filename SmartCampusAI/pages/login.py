import streamlit as st
import time
from utils.auth import validate_email, login_user
from utils.database import authenticate_user

def show():
    """Renders the login page form and manages user credentials submission."""
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    
    # Outer glass card for login form
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.markdown(
        '<div class="auth-header">'
        '<div class="auth-logo">🏫</div>'
        '<h2>Welcome to SmartCampusAI</h2>'
        '<p style="color: #94a3b8; font-size: 0.9rem;">Sign in to access your student dashboard</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    # Form wrapper
    with st.form(key="login_form", clear_on_submit=False):
        email = st.text_input("Campus Email Address", placeholder="e.g. john@example.com")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        
        submit_btn = st.form_submit_button(label="Sign In")
        
        if submit_btn:
            # Check empty fields
            if not email.strip() or not password.strip():
                st.error("Please fill in all the fields.")
            # Check email validation
            elif not validate_email(email):
                st.error("Invalid email address format.")
            else:
                with st.spinner("Authenticating credentials..."):
                    # Wait a tiny bit for modern UX feeling
                    time.sleep(0.8)
                    user_data = authenticate_user(email, password)
                    
                    if user_data:
                        st.success("Successfully logged in!")
                        time.sleep(0.5)
                        login_user(user_data)
                        st.rerun()
                    else:
                        st.error("Incorrect email or password. Please try again.")
                        
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer links for navigation
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Don't have an account?")
    with col2:
        if st.button("Register Here", key="nav_to_register_btn"):
            st.session_state.page = "Register"
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)
