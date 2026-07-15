import streamlit as st
import time
from utils.auth import validate_email, is_duplicate_email, validate_password_strength
from utils.database import create_user

def show():
    """Renders the registration page and handles new user creation."""
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    
    # Outer glass card container
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.markdown(
        '<div class="auth-header">'
        '<div class="auth-logo">🎓</div>'
        '<h2>Create Student Account</h2>'
        '<p style="color: #94a3b8; font-size: 0.9rem;">Register to access AI features and campus news</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    with st.form(key="register_form", clear_on_submit=False):
        name = st.text_input("Full Name", placeholder="e.g. John Doe")
        email = st.text_input("Campus Email Address", placeholder="e.g. john@example.com")
        password = st.text_input("Password", type="password", placeholder="At least 6 characters")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
        
        submit_btn = st.form_submit_button(label="Create Account")
        
        if submit_btn:
            # Field empty checks
            if not name.strip() or not email.strip() or not password.strip() or not confirm_password.strip():
                st.error("Please fill in all the fields.")
            # Email validation
            elif not validate_email(email):
                st.error("Please enter a valid email format.")
            # Duplicate check
            elif is_duplicate_email(email):
                st.error("An account with this email already exists.")
            else:
                # Password validation (match + length)
                is_valid_pwd, pwd_error = validate_password_strength(password, confirm_password)
                if not is_valid_pwd:
                    st.error(pwd_error)
                else:
                    with st.spinner("Registering your profile..."):
                        time.sleep(1.0)
                        new_user = create_user(name, email, password)
                        if new_user:
                            st.success("Registration successful! Redirecting to login...")
                            time.sleep(1.2)
                            st.session_state.page = "Login"
                            st.rerun()
                        else:
                            st.error("Registration failed. Please contact administrator.")
                            
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer links for navigation
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Already have an account?")
    with col2:
        if st.button("Sign In Here", key="nav_to_login_btn"):
            st.session_state.page = "Login"
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)
