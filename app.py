# =========================================================
# VIBRANT COLOUR STYLING
# =========================================================

st.markdown("""
<style>

/* ================= SIDEBAR ================= */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #4f46e5 0%,
        #7c3aed 25%,
        #db2777 55%,
        #f97316 80%,
        #facc15 100%
    );
}

/* Sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: white !important;
}

/* Sidebar main title */
[data-testid="stSidebar"] h1 {
    color: #ffffff !important;
    text-align: center;
    font-size: 30px;
    font-weight: 900;
    text-shadow: 2px 2px 8px #4c1d95;
}

/* Sidebar headings */
[data-testid="stSidebar"] h2 {
    color: #ffffff !important;
    font-weight: 900;
    text-shadow: 1px 1px 5px #581c87;
}

[data-testid="stSidebar"] h3 {
    color: #fff7ed !important;
    font-weight: 900;
}


/* ================= SIDEBAR BUTTONS ================= */

[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    border-radius: 15px;
    border: 2px solid white;

    background: linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6,
        #8b5cf6
    );

    color: white !important;
    font-size: 16px;
    font-weight: 900;

    box-shadow: 0px 5px 15px rgba(0,0,0,0.25);

    transition: all 0.3s ease;
}

/* Button hover */
[data-testid="stSidebar"] .stButton > button:hover {
    background: linear-gradient(
        90deg,
        #facc15,
        #f97316,
        #ec4899
    );

    transform: scale(1.04);

    border-color: white;

    box-shadow: 0px 8px 20px rgba(0,0,0,0.35);
}


/* ================= SIDEBAR DIVIDER ================= */

[data-testid="stSidebar"] hr {
    border: none;
    height: 3px;

    background: linear-gradient(
        90deg,
        #22d3ee,
        #facc15,
        #f472b6
    );

    border-radius: 10px;
}


/* ================= PIPELINE CONTENT ================= */

/* Make pipeline text colorful */
[data-testid="stSidebar"] .stMarkdown {
    color: white;
}

/* Captions */
[data-testid="stSidebar"] small {
    color: #fff7ed !important;
    font-weight: 600;
}


/* ================= MAIN PAGE ================= */

/* Main background */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(
            135deg,
            #eef2ff 0%,
            #fdf2f8 45%,
            #fff7ed 100%
        );
}

/* Main title */
h1 {
    color: #6d28d9 !important;
    font-weight: 900 !important;
    text-shadow: 2px 2px 8px rgba(124,58,237,0.25);
}

/* Main captions */
.stCaption {
    color: #7c3aed !important;
    font-weight: 600;
}


/* ================= CHAT ================= */

[data-testid="stChatMessage"] {
    border-radius: 20px;
    padding: 12px;
    margin: 10px 0;

    box-shadow: 0px 5px 15px rgba(0,0,0,0.12);
}

/* User message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(
        135deg,
        #dbeafe,
        #c4b5fd,
        #fbcfe8
    );

    border-left: 6px solid #7c3aed;
}

/* Assistant message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(
        135deg,
        #dcfce7,
        #cffafe,
        #dbeafe
    );

    border-left: 6px solid #06b6d4;
}


/* ================= CHAT INPUT ================= */

[data-testid="stChatInput"] {
    border: 3px solid #8b5cf6;
    border-radius: 20px;

    box-shadow:
        0px 0px 15px rgba(139,92,246,0.35);
}

[data-testid="stChatInput"] textarea {
    font-weight: 600;
}


/* ================= CLEAR CHAT BUTTON ================= */

.stButton > button {
    border-radius: 12px;
    border: 2px solid #ec4899;

    background: linear-gradient(
        90deg,
        #fce7f3,
        #e9d5ff
    );

    color: #9d174d;
    font-weight: 900;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #f472b6,
        #a78bfa
    );

    color: white;
    border-color: #7c3aed;
}

</style>
""", unsafe_allow_html=True)
