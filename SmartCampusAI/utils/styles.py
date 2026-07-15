import streamlit as st

def get_css(theme="Dark"):
    """
    Returns custom CSS code depending on the theme ('Light' or 'Dark').
    Implements a premium glassmorphic visual language.
    """
    is_dark = theme.lower() == "dark"
    
    # Theme color definitions
    bg_gradient = "linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%)" if is_dark else "linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #f1f5f9 100%)"
    card_bg = "rgba(255, 255, 255, 0.03)" if is_dark else "rgba(255, 255, 255, 0.6)"
    card_border = "rgba(255, 255, 255, 0.08)" if is_dark else "rgba(0, 0, 0, 0.08)"
    text_color = "#f8fafc" if is_dark else "#0f172a"
    sub_text_color = "#94a3b8" if is_dark else "#475569"
    shadow_color = "rgba(0, 0, 0, 0.3)" if is_dark else "rgba(148, 163, 184, 0.15)"
    accent_gradient = "linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%)"
    
    css = f"""
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    /* Global Body Overrides */
    .stApp {{
        background: {bg_gradient} !important;
        font-family: 'Outfit', sans-serif !important;
        color: {text_color} !important;
    }}

    /* Title & Text styling overrides */
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        color: {text_color} !important;
    }}

    /* Sidebar overrides */
    section[data-testid="stSidebar"] {{
        background-color: {"rgba(15, 23, 42, 0.95)" if is_dark else "rgba(248, 250, 252, 0.95)"} !important;
        border-right: 1px solid {card_border} !important;
    }}
    
    /* Custom Glassmorphism Card Container */
    .glass-card {{
        background: {card_bg} !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid {card_border} !important;
        border-radius: 16px !important;
        padding: 24px !important;
        margin-bottom: 18px !important;
        box-shadow: 0 8px 32px 0 {shadow_color} !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }}

    .glass-card:hover {{
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 40px 0 {shadow_color} !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }}
    
    /* Metrics Flex Grid */
    .metrics-container {{
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
        width: 100%;
        margin-bottom: 24px;
    }}
    
    .metric-card {{
        flex: 1;
        min-width: 200px;
        background: {card_bg};
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {card_border};
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 20px {shadow_color};
        transition: transform 0.2s ease;
    }}
    
    .metric-card:hover {{
        transform: scale(1.03);
    }}
    
    .metric-value {{
        font-size: 2rem;
        font-weight: 700;
        background: {accent_gradient};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 8px 0;
    }}
    
    .metric-label {{
        font-size: 0.85rem;
        color: {sub_text_color};
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}

    /* Campus Announcement Card */
    .announcement-item {{
        border-left: 4px solid #8b5cf6;
        padding-left: 14px;
        margin-bottom: 16px;
    }}
    
    .announcement-title {{
        font-weight: 600;
        font-size: 1.05rem;
        color: {text_color};
        margin-bottom: 2px;
    }}
    
    .announcement-meta {{
        font-size: 0.75rem;
        color: {sub_text_color};
        margin-bottom: 6px;
    }}

    .announcement-desc {{
        font-size: 0.9rem;
        color: {sub_text_color};
    }}

    /* Custom Buttons styling override */
    div.stButton > button {{
        background: {accent_gradient} !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 8px 24px !important;
        font-weight: 500 !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }}

    div.stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6) !important;
    }}
    
    div.stButton > button:active {{
        transform: translateY(0px) !important;
    }}

    /* Login/Register Card layout */
    .auth-container {{
        max-width: 450px;
        margin: 5% auto;
    }}

    .auth-header {{
        text-align: center;
        margin-bottom: 30px;
    }}

    .auth-logo {{
        font-size: 3.5rem;
        margin-bottom: 10px;
    }}

    /* Alert Boxes overrides */
    div[data-testid="stNotification"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 10px !important;
        border: 1px solid {card_border} !important;
    }}

    /* Hide standard footer */
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {{
        width: 8px;
    }}
    ::-webkit-scrollbar-track {{
        background: rgba(0, 0, 0, 0.1);
    }}
    ::-webkit-scrollbar-thumb {{
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
        background: rgba(255, 255, 255, 0.2);
    }}
    """
    return css

def inject_styles(theme="Dark"):
    """Injects the custom CSS into the Streamlit session."""
    st.markdown(f"<style>{get_css(theme)}</style>", unsafe_allow_html=True)
