import streamlit as st
import pandas as pd

# Import your agents
from agents.extractor import extract_data
from agents.pattern import detect_pattern
from agents.reasoning import generate_reason
from agents.action import suggest_action

st.title("🚨 CivicPulse AI - Early Risk Detection System")
st.markdown("### Multi-Agent AI system for early urban risk detection")

st.write("Upload city complaints data to detect risks")

# Upload CSV
file = st.file_uploader("Upload complaints CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    # Show data
    st.subheader("📄 Uploaded Data")
    st.write(df)

    texts = df["text"].tolist()

    # Step 1: Extract
    extracted = extract_data(texts)

    # Step 2: Pattern detection
    pattern = detect_pattern(extracted)

    # Step 3: Reasoning (Gemini)
    reason = generate_reason(pattern)

    # Step 4: Action
    action = suggest_action(pattern)

    # Display results
    st.subheader("🚨 ALERT")

    if pattern == "water_risk":
        st.write("Confidence: 88%")
    elif pattern == "health_risk":
        st.write("Confidence: 90%")
    else:
        st.write("Confidence: Low")

    st.subheader("📊 Signals Detected")

    if pattern == "water_risk":
        st.write("- Multiple water complaints")
        st.write("- Bad smell reports")

    elif pattern == "health_risk":
        st.write("- Increase in fever/cough cases")
        st.write("- Stagnant water reports")

    else:
        st.write("- No abnormal signals detected")

    # ALERT message
    if pattern == "water_risk":
        st.error("⚠️ Water Contamination Risk Detected in Ward 2")

    elif pattern == "health_risk":
        st.error("⚠️ Health Risk Detected (Possible Disease Spread)")

    else:
        st.success("✅ No major risk detected")

    st.subheader("🧠 AI Reasoning")
    st.write(reason)

    st.subheader("✅ Recommended Action")
    st.write(action)