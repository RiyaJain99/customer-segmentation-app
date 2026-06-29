import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(
    page_title="Customer Segmentation AI",
    page_icon="🛍️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background-color: #0e1117; }
    
    .header-box {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid #e94560;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #0f3460;
        margin-bottom: 1rem;
    }
    
    .segment-card {
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 1rem;
    }
    
    .premium { 
        background: linear-gradient(135deg, #1a1a2e, #2d1b69);
        border: 2px solid #7c3aed;
    }
    .average { 
        background: linear-gradient(135deg, #1a1a2e, #064e3b);
        border: 2px solid #10b981;
    }
    .discount { 
        background: linear-gradient(135deg, #1a1a2e, #7c2d12);
        border: 2px solid #f97316;
    }
    .personal { 
        background: linear-gradient(135deg, #1a1a2e, #7f1d1d);
        border: 2px solid #ef4444;
    }
    .budget { 
        background: linear-gradient(135deg, #1a1a2e, #713f12);
        border: 2px solid #eab308;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #e94560, #0f3460);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: bold;
        margin-top: 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0f3460, #e94560);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <h1 style='color: #e94560;'>🛍️ RetailAI</h1>
            <p style='color: #888;'>Customer Intelligence Platform</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🤖 Model Info")
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0;'>Algorithm</p>
            <h3 style='color: #e94560; margin:0;'>KMeans Clustering</h3>
        </div>
        <div class='metric-card'>
            <p style='color: #888; margin:0;'>Type</p>
            <h3 style='color: #10b981; margin:0;'>Unsupervised ML</h3>
        </div>
        <div class='metric-card'>
            <p style='color: #888; margin:0;'>Segments</p>
            <h3 style='color: #7c3aed; margin:0;'>5 Customer Groups</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 Segment Guide")
    st.markdown("""
        - 💎 **Premium** — High Income, High Spend
        - 🟢 **Average** — Balanced Customers  
        - 🟠 **Discount** — Low Income, High Spend
        - 🔴 **Potential** — High Income, Low Spend
        - 🟡 **Budget** — Low Income, Low Spend
    """)

# Header
st.markdown("""
    <div class='header-box'>
        <h1 style='color: white; font-size: 2.5rem; margin:0;'>
            🛍️ AI Customer Segmentation Dashboard
        </h1>
        <p style='color: #888; margin-top: 0.5rem; font-size: 1.1rem;'>
            Identify customer groups using Machine Learning
        </p>
    </div>
""", unsafe_allow_html=True)

# Stats Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0; font-size:0.9rem;'>Dataset</p>
            <h3 style='color: white; margin:0;'>Mall Customers</h3>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0; font-size:0.9rem;'>Total Customers</p>
            <h3 style='color: #e94560; margin:0;'>200</h3>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0; font-size:0.9rem;'>Segments Found</p>
            <h3 style='color: #10b981; margin:0;'>5 Groups</h3>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0; font-size:0.9rem;'>Algorithm</p>
            <h3 style='color: #7c3aed; margin:0;'>KMeans</h3>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Input Section
st.markdown("### 🎯 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 💰 Annual Income")
    income = st.number_input(
        "Annual Income (k$)",
        min_value=0,
        max_value=150,
        value=60,
        help="Enter customer's annual income in thousands"
    )
    st.markdown(f"""
        <div class='metric-card'>
            <p style='color: #888; margin:0;'>Selected Income</p>
            <h2 style='color: #e94560; margin:0;'>${income}k</h2>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### 🛒 Spending Score")
    spending = st.slider(
        "Spending Score (1-100)",
        1, 100, 50,
        help="Customer's spending score assigned by the mall"
    )
    st.markdown(f"""
        <div class='metric-card'>
            <p style='color: #888; margin:0;'>Selected Score</p>
            <h2 style='color: #10b981; margin:0;'>{spending}/100</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Predict Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_btn = st.button("🚀 Predict Customer Segment")

if predict_btn:
    data = np.array([[income, spending]])
    scaled = scaler.transform(data)
    cluster = model.predict(scaled)[0]

    segments = {
        0: {
            "title": "🟢 Average Customer",
            "subtitle": "Balanced Income & Spending",
            "strategy": "Maintain regular engagement through newsletters and standard loyalty points.",
            "tactics": ["Monthly newsletters", "Standard loyalty program", "Regular promotions"],
            "color": "#10b981",
            "class": "average"
        },
        1: {
            "title": "💎 Premium Customer",
            "subtitle": "High Income • High Spending",
            "strategy": "Focus on exclusive premium experiences and VIP membership programs.",
            "tactics": ["VIP membership", "Exclusive early access", "Personal shopping assistant"],
            "color": "#7c3aed",
            "class": "premium"
        },
        2: {
            "title": "🟠 Deal Seeker",
            "subtitle": "Low Income • High Spending",
            "strategy": "Target with coupons, flash sales and discount campaigns.",
            "tactics": ["Flash sales", "Coupon campaigns", "Buy 1 Get 1 offers"],
            "color": "#f97316",
            "class": "discount"
        },
        3: {
            "title": "🔴 Potential Premium",
            "subtitle": "High Income • Low Spending",
            "strategy": "Use personalized marketing to convert high earners into active spenders.",
            "tactics": ["Personalized recommendations", "Exclusive previews", "Premium trial offers"],
            "color": "#ef4444",
            "class": "personal"
        },
        4: {
            "title": "🟡 Budget Customer",
            "subtitle": "Low Income • Low Spending",
            "strategy": "Engage with budget-friendly offers and value-for-money promotions.",
            "tactics": ["Budget bundles", "Cashback offers", "Affordable loyalty rewards"],
            "color": "#eab308",
            "class": "budget"
        }
    }

    seg = segments[cluster]

    st.markdown(f"""
        <div class='segment-card {seg["class"]}'>
            <h1 style='color: {seg["color"]}; font-size: 2.5rem;'>{seg["title"]}</h1>
            <p style='color: #888; font-size: 1.2rem;'>{seg["subtitle"]}</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📋 Business Strategy")
        st.markdown(f"""
            <div class='metric-card'>
                <p style='color: white; font-size: 1rem;'>{seg["strategy"]}</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 🎯 Action Items")
        for tactic in seg["tactics"]:
            st.markdown(f"""
                <div class='metric-card' style='margin-bottom: 0.5rem;'>
                    <p style='color: {seg["color"]}; margin:0;'>✓ {tactic}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
        <div style='text-align: center; padding: 1rem;'>
            <p style='color: #888;'>Customer classified into 
            <span style='color: {seg["color"]}; font-weight: bold;'>
            Segment {cluster}</span> out of 5 total segments</p>
        </div>
    """, unsafe_allow_html=True)