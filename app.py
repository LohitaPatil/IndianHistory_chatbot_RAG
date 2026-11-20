import streamlit as st
from rag_engine import load_base, ask_rag

st.set_page_config(page_title="Heritage AI", layout="centered")


# =========================================================
# COLOUR STYLING
# =========================================================

st.markdown("""
<style>

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #fff7ed 0%,
        #fef3c7 35%,
        #fce7f3 70%,
        #ede9fe 100%
    );
}

[data-testid="stSidebar"] p {
    color: #374151;
}

[data-testid="stSidebar"] h1 {
    color: #7c2d12;
}

[data-testid="stSidebar"] h2 {
    color: #2563eb;
}

[data-testid="stSidebar"] h3 {
    color: #db2777;
}

.stButton > button {
    border-radius: 12px;
    border: 2px solid #c084fc;
    background: linear-gradient(90deg, #dbeafe, #fce7f3);
    color: #6b21a8;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #bfdbfe, #fbcfe8);
    border-color: #9333ea;
}

[data-testid="stChatMessage"] {
    border-radius: 15px;
}

[data-testid="stChatMessage"] p {
    font-size: 16px;
}

[data-testid="stChatInput"] {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("📜 Heritage AI")

    st.markdown("---")

    # Two buttons
    if st.button("🔄 Pipeline", use_container_width=True):
        st.session_state["sidebar_page"] = "pipeline"

    if st.button("ℹ️ Info", use_container_width=True):
        st.session_state["sidebar_page"] = "info"

    st.markdown("---")

    # Default sidebar
    if "sidebar_page" not in st.session_state:
        st.session_state["sidebar_page"] = "none"

    # ---------------- PIPELINE ----------------

    if st.session_state["sidebar_page"] == "pipeline":

        st.subheader("🔄 RAG Flow")

        st.write("📚 **History Files**")
        st.caption("**Multiple history documents**")

        st.write("⬇️")

        st.write("📄 **Load Documents**")
        st.caption("**Extract text from files**")

        st.write("⬇️")

        st.write("✂️ **Chunking**")
        st.caption("**Split text into smaller chunks**")

        st.write("⬇️")

        st.write("🔢 **Embeddings**")
        st.caption("**Convert text into vectors**")

        st.write("⬇️")

        st.write("🗄️ **Vector Index**")
        st.caption("**Store and search vectors**")

        st.write("⬇️")

        st.write("🔍 **Retrieval**")
        st.caption("**Find relevant history**")

        st.write("⬇️")

        st.write("🧠 **LLM**")
        st.caption("**Generate the answer**")

        st.write("⬇️")

        st.write("💬 **Final Answer**")

    # ---------------- INFO ----------------

    elif st.session_state["sidebar_page"] == "info":

        st.subheader("ℹ️ Heritage AI")

        st.write("### 🤖 Model")

        st.caption(
            "Heritage AI is a RAG-based history chatbot. "
            "It retrieves relevant information from historical "
            "documents and uses an LLM to generate contextual answers."
        )

        st.write("### 🛠️ Technologies")

        st.write("🐍 **Python**")
        st.caption("**Backend and RAG implementation**")

        st.write("🎈 **Streamlit**")
        st.caption("**Interactive user interface**")

        st.write("🔎 **RAG**")
        st.caption("**Retrieval-Augmented Generation**")

        st.write("🔢 **Embeddings**")
        st.caption("**Converts text into vector representations**")

        st.write("🗄️ **Vector Index**")
        st.caption("**Stores and retrieves relevant vectors**")

        st.write("🧠 **Groq LLM**")
        st.caption("**Generates natural-language responses**")

        st.write("### 👥 Group Members")

        st.write("👤 Lohita R Patil")
        st.write("👤 Harshitha")
        st.write("👤 Kavya M P")
        st.write("👤 Anita")
        st.write("👤 Lithin")


# =========================================================
# MAIN CHATBOT
# =========================================================

st.title("Heritage AI")

st.caption(
    "Learn from the past, understand the present, and explore history "
    "through an interactive AI-powered chatbot."
)

st.caption("RAG pipeline with mutiple files")
st.caption("Created by ")

my_key = st.secrets["GROQ_API_KEY"]


@st.cache_resource
def initiate_rag():
    return load_base("history")


index, embed_model, chunks = initiate_rag()


if "chat_hist" not in st.session_state:
    st.session_state.chat_hist = []


for qa in st.session_state.chat_hist:

    with st.chat_message(qa["role"]):
        st.write(qa["content"])


question = st.chat_input(
    "Ask anything about history and archaeology..."
)


if question:

    st.session_state.chat_hist.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("asking RAG for answer"):

            answer = ask_rag(
                question,
                embed_model,
                chunks,
                index,
                api_key=my_key
            )

            st.write(answer)

            st.session_state.chat_hist.append(
                {"role": "assistant", "content": answer}
            )


if st.button("Clear chat"):

    st.session_state.chat_hist = []
    st.rerun()
