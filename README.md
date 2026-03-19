# 🏛️ CivicPulse Lite: AI Agent for Early Urban Risk Detection

**Selected Problem Statement:** Problem 5 — Domain-Specialized AI Agents with Compliance Guardrails

---

## 📝 Project Overview

CivicPulse Lite is a Multi-Agent AI system that transforms citizen complaints into early warnings for urban risks.
It helps cities detect issues like disease outbreaks and water contamination **before they become serious problems**.

The system acts as a **central intelligence layer**, analyzing multiple signals and generating actionable insights for authorities.

---

## 📺 Demo Highlights

* **Target Domain:** Public Health & Urban Utilities
* **Key Detection:** Identified Water Contamination Risk in **Ward 2**
* **Agent Output:** Generated alert, reasoning, and recommended action

---

## 🏗️ Multi-Agent Architecture

1. **Extraction Agent**
   Extracts keywords like symptoms, water issues, and location from input data

2. **Pattern Agent**
   Detects abnormal increases in complaints and assigns confidence score

3. **Reasoning Agent (Gemini 2.0 Flash)**
   Generates **auditable reasoning** explaining why the issue is occurring

4. **Action Agent**
   Suggests practical steps for authorities (e.g., inspect pipelines, issue alerts)

---

## 📊 Impact Model (Based on Ward 2 Scenario)

* **Early Detection:** 48–72 hours before escalation
* **Population Impact:** ~5,000 people

### Without CivicPulse AI:

* 10% affected → 500 people
* ₹500 treatment cost per person
* **Total Cost:** ₹2,50,000

### With CivicPulse AI:

* 70% cases prevented

👉 **Estimated Savings:** ₹1,75,000
👉 Reduced hospital overload + faster response

---

## 🛠️ Tech Stack

* **Language:** Python
* **LLM:** Google Gemini (google-genai SDK)
* **Frontend:** Streamlit
* **Environment:** python-dotenv

---

## 🚀 Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/civicpulse-ai.git
cd civicpulse-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 🛡️ Compliance & Guardrails

* Uses anonymized citizen data (no personal info stored)
* Provides advisory insights, not medical diagnosis
* Supports decision-making, not replaces authorities
* Threshold-based logic reduces false alerts
* Includes fallback mechanism if API fails

---

## 🎯 Key Features

* Multi-Agent AI pipeline
* Real-time risk detection
* Explainable AI reasoning
* Actionable alerts for authorities
* Reliable fallback mechanism

---

## 💡 Conclusion

CivicPulse AI enables cities to shift from **reactive response → proactive prevention**,
helping save lives, reduce costs, and improve public safety.
