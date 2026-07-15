import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from utils.database import load_users
from utils.ai_helper import ask_campus_ai

def show():
    """Renders the dashboard metrics, announcements, activities, and AI assistant."""
    user = st.session_state.user
    users_list = load_users()
    total_users = len(users_list)
    
    # Header Welcome Message
    st.markdown(
        f"""
        <div style="margin-bottom: 24px;">
            <h1 style="margin: 0; font-size: 2.2rem; background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Welcome Back, {user['name']}! {user.get('avatar', '🎓')}
            </h1>
            <p style="color: #94a3b8; margin: 4px 0 0 0;">
                Today is {datetime.now().strftime("%A, %B %d, %Y")} | Major: <strong>{user.get('major', 'Undeclared')}</strong>
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # 3 Glassmorphic Metric Cards using our custom CSS
    st.markdown(
        f"""
        <div class="metrics-container">
            <div class="metric-card">
                <div class="metric-label">Total Users</div>
                <div class="metric-value">{total_users}</div>
                <div style="font-size: 0.8rem; color: #10b981;">📈 Active accounts</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Campus Safety</div>
                <div class="metric-value">Normal</div>
                <div style="font-size: 0.8rem; color: #10b981;">🛡️ 100% secure</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Library Capacity</div>
                <div class="metric-value">42%</div>
                <div style="font-size: 0.8rem; color: #fbbf24;">👥 Moderate load</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Left & Right columns layout
    left_col, right_col = st.columns([1.3, 1])
    
    with left_col:
        # AI Assistant Section (Glassmorphic)
        st.markdown(
            """
            <div class="glass-card" style="margin-bottom: 20px;">
                <h3 style="margin-top: 0; color: #60a5fa; display: flex; align-items: center; gap: 8px;">
                    🤖 SmartCampus AI Assistant
                </h3>
                <p style="color: #94a3b8; font-size: 0.85rem; margin-bottom: 12px;">
                    Ask me about library hours, campus dining, network connection protocols, parking permits, and exam dates!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Streamlit Chat Interface inside AI section
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                {"role": "assistant", "content": "Hi! I am SmartCampusAI. How can I help you navigate your campus life today?"}
            ]
            
        # Display chat messages
        chat_container = st.container(height=350)
        with chat_container:
            for message in st.session_state.chat_history:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
                    
        # Chat input
        if prompt := st.chat_input("Ask a question about the campus...", key="dashboard_chat_input"):
            with chat_container:
                with st.chat_message("user"):
                    st.markdown(prompt)
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            
            with chat_container:
                with st.chat_message("assistant"):
                    with st.spinner("AI is thinking..."):
                        # query helper
                        response = ask_campus_ai(prompt, st.session_state.chat_history[:-1])
                        st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            
    with right_col:
        # Campus Announcements Section
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="margin-top: 0; color: #a78bfa; display: flex; align-items: center; gap: 8px;">
                    📢 Campus Announcements
                </h3>
                <hr style="border-color: rgba(255,255,255,0.08); margin-bottom: 15px;"/>
                
                <div class="announcement-item">
                    <div class="announcement-title">Library 24/7 Extended Hours</div>
                    <div class="announcement-meta">Posted today | Student Affairs</div>
                    <div class="announcement-desc">Starting next week, the library lobby and computer lab will be open 24/7 for exam preparation.</div>
                </div>
                
                <div class="announcement-item" style="border-left-color: #3b82f6;">
                    <div class="announcement-title">Annual AI Hackathon Registration</div>
                    <div class="announcement-meta">Posted 2 days ago | Engineering Dept</div>
                    <div class="announcement-desc">Form teams of up to 4 and build innovative campus tools. Prizes exceed $5,000!</div>
                </div>
                
                <div class="announcement-item" style="border-left-color: #10b981;">
                    <div class="announcement-title">New Food Trucks at Student Union</div>
                    <div class="announcement-meta">Posted 4 days ago | Campus Dining</div>
                    <div class="announcement-desc">Say hello to gourmet tacos and healthy salad bowls at the quad dining zone.</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Recent Activity & Library Seat Availability Prediction (Plotly Graph)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(
            """
            <h3 style="margin-top: 0; color: #f43f5e; display: flex; align-items: center; gap: 8px;">
                📊 Library Busy Curve (Today)
            </h3>
            """,
            unsafe_allow_html=True
        )
        
        # Create a mock dataset for hourly library utilization
        hours_list = [f"{h:02d}:00" for h in range(8, 23)]
        occupancy = [15, 30, 45, 60, 80, 85, 70, 75, 90, 85, 60, 40, 25, 15, 10]
        
        df = pd.DataFrame({"Hour": hours_list, "Occupancy (%)": occupancy})
        
        fig = px.line(
            df, 
            x="Hour", 
            y="Occupancy (%)",
            markers=True,
            color_discrete_sequence=["#f43f5e"]
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=10, b=0),
            xaxis=dict(showgrid=False, color="#94a3b8"),
            yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", color="#94a3b8"),
            height=200
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
