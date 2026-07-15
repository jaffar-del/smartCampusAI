import streamlit as st
import time
from utils.database import update_profile

def show():
    """Renders the user profile section to view and update student details."""
    user = st.session_state.user
    
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h1 style="margin: 0; font-size: 2.2rem; background: linear-gradient(135deg, #10b981 0%, #3b82f6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Student Profile 👤
            </h1>
            <p style="color: #94a3b8; margin: 4px 0 0 0;">Manage your campus identity details</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
        # Giant avatar preview
        st.markdown(f'<div style="font-size: 5rem; margin-bottom: 10px;">{user.get("avatar", "👤")}</div>', unsafe_allow_html=True)
        st.markdown(f'<h3 style="margin: 5px 0;">{user["name"]}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: #94a3b8; font-size: 0.85rem; margin-top:0;">{user["email"]}</p>', unsafe_allow_html=True)
        st.markdown('<hr style="border-color: rgba(255,255,255,0.08); margin: 15px 0;"/>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="text-align: left; font-size: 0.85rem; color: #94a3b8;">
                <div>📅 <strong>Joined:</strong> {user.get('created_at', '2026-01-01')}</div>
                <div style="margin-top: 5px;">🎓 <strong>Status:</strong> Enrolled</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-top:0; color: #10b981;">Edit Profile Settings</h3>', unsafe_allow_html=True)
        
        with st.form("profile_edit_form", clear_on_submit=False):
            # Input fields initialized with current values
            name_input = st.text_input("Full Name", value=user["name"])
            
            # Read-only Email display
            st.text_input("Campus Email (Cannot be changed)", value=user["email"], disabled=True)
            
            # Major list
            majors = ["Computer Science", "Data Science", "Artificial Intelligence", "Mechanical Engineering", "Electrical Engineering", "Business Administration", "Other"]
            current_major = user.get("major", "Computer Science")
            if current_major not in majors:
                majors.append(current_major)
            major_input = st.selectbox("Academic Major", options=majors, index=majors.index(current_major))
            
            # Avatar Emoji select box
            avatars = ["🎓", "👨‍🎓", "👩‍🎓", "👤", "🚀", "💻", "🎨", "🔬", "⚽", "🎵"]
            current_avatar = user.get("avatar", "🎓")
            if current_avatar not in avatars:
                avatars.append(current_avatar)
            avatar_input = st.selectbox("Profile Avatar Icon", options=avatars, index=avatars.index(current_avatar))
            
            # Bio text area
            bio_input = st.text_area("About Me / Biography", value=user.get("bio", ""), max_chars=250, placeholder="Tell us about yourself...")
            
            submit_btn = st.form_submit_button("Save Profile Changes")
            
            if submit_btn:
                if not name_input.strip():
                    st.error("Full Name cannot be empty.")
                else:
                    with st.spinner("Updating profile info..."):
                        time.sleep(0.8)
                        
                        updated_data = {
                            "name": name_input.strip(),
                            "major": major_input,
                            "avatar": avatar_input,
                            "bio": bio_input.strip()
                        }
                        
                        success = update_profile(user["email"], updated_data)
                        if success:
                            # Update session state user
                            for key, val in updated_data.items():
                                st.session_state.user[key] = val
                            st.success("Your profile has been updated successfully!")
                            time.sleep(0.5)
                            st.rerun()
                        else:
                            st.error("Failed to update database record.")
                            
        st.markdown('</div>', unsafe_allow_html=True)
