import streamlit as st
import os
from PIL import Image
from streamlit_option_menu import option_menu

# Set Streamlit Page Configuration (Must be at the very top)
st.set_page_config(
    page_title="SmartCampusAI",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import Utilities and Pages
from utils.auth import init_session_state, logout_user
from utils.styles import inject_styles
from pages import login, register, dashboard, profile, settings

def load_logo():
    """Tries to load the logo image from assets. Returns None if it fails."""
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "logo.png")
    if os.path.exists(logo_path):
        try:
            return Image.open(logo_path)
        except Exception:
            return None
    return None

def main():
    # 1. Initialize session variables (auth, page selection, theme)
    init_session_state()
    
    # 2. Inject responsive glassmorphism styles based on active theme
    inject_styles(st.session_state.theme)
    
    # Load Logo
    logo = load_logo()
    
    # 3. Sidebar Header branding
    with st.sidebar:
        if logo:
            st.image(logo, use_container_width=True)
        else:
            st.markdown(
                """
                <div style="text-align: center; margin: 15px 0;">
                    <span style="font-size: 2.2rem;">🏫</span>
                    <h2 style="margin: 5px 0 0 0; background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                        SmartCampus
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
        st.markdown('<hr style="border-color: rgba(255,255,255,0.08); margin: 10px 0 20px 0;"/>', unsafe_allow_html=True)

    # 4. Routing logic based on authentication status
    if not st.session_state.authenticated:
        # Prevent access to dashboard, profile, settings if unauthenticated
        if st.session_state.page not in ["Login", "Register"]:
            st.session_state.page = "Login"
            
        unauth_options = ["Login", "Register"]
        default_idx = unauth_options.index(st.session_state.page)
        
        with st.sidebar:
            selected_option = option_menu(
                menu_title="Gateway Portal",
                options=unauth_options,
                icons=["box-arrow-in-right", "person-plus"],
                menu_icon="shield-lock",
                default_index=default_idx,
                styles={
                    "container": {"background-color": "transparent"},
                    "nav-link": {"font-size": "0.95rem", "color": "#94a3b8", "font-family": "'Outfit', sans-serif"},
                    "nav-link-selected": {"background": "linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%)", "color": "white", "font-weight": "500"},
                }
            )
            
        # Update routing page state if sidebar item was clicked
        if selected_option != st.session_state.page:
            st.session_state.page = selected_option
            st.rerun()
            
        # Render page
        if st.session_state.page == "Login":
            login.show()
        elif st.session_state.page == "Register":
            register.show()
            
    else:
        # Logged-in navigation
        auth_options = ["Dashboard", "Profile", "Settings"]
        if st.session_state.page not in auth_options:
            st.session_state.page = "Dashboard"
            
        default_idx = auth_options.index(st.session_state.page)
        
        with st.sidebar:
            # Display mini profile card in sidebar
            user = st.session_state.user
            st.markdown(
                f"""
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 12px; margin-bottom: 20px; text-align: center;">
                    <div style="font-size: 2.2rem; margin-bottom: 5px;">{user.get('avatar', '🎓')}</div>
                    <div style="font-weight: 600; font-size: 0.95rem;">{user['name']}</div>
                    <div style="font-size: 0.75rem; color: #94a3b8;">{user['email']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Sidebar menu
            selected_option = option_menu(
                menu_title="Main Menu",
                options=auth_options,
                icons=["grid-1x2", "person-badge", "gear"],
                menu_icon="menu-button-wide",
                default_index=default_idx,
                styles={
                    "container": {"background-color": "transparent"},
                    "nav-link": {"font-size": "0.95rem", "color": "#94a3b8", "font-family": "'Outfit', sans-serif"},
                    "nav-link-selected": {"background": "linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%)", "color": "white", "font-weight": "500"},
                }
            )
            
            st.markdown('<hr style="border-color: rgba(255,255,255,0.08); margin: 20px 0 10px 0;"/>', unsafe_allow_html=True)
            
            # Sign Out Button
            if st.button("🚪 Logout & Exit", key="logout_sidebar_btn", help="Securely terminate session"):
                logout_user()
                
        # Update routing page state if sidebar item was clicked
        if selected_option != st.session_state.page:
            st.session_state.page = selected_option
            st.rerun()
            
        # Render selected page
        if st.session_state.page == "Dashboard":
            dashboard.show()
        elif st.session_state.page == "Profile":
            profile.show()
        elif st.session_state.page == "Settings":
            settings.show()

if __name__ == "__main__":
    main()
