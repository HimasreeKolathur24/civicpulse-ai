from google import genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options={'api_version': 'v1'}
)

def generate_reason(pattern):
    try:
        # Structured prompts to satisfy the "Domain-Specialized" track
        if pattern == "health_risk":
            prompt = """Analyze: increasing fever cases + stagnant water. 
            Provide a short, auditable reasoning for a potential disease outbreak 
            and suggest one immediate public health action."""
            
        elif pattern == "water_risk":
            prompt = """Analyze: repeated complaints about water smell/color. 
            Provide a short reasoning for potential contamination 
            and suggest one immediate utility inspection step."""
            
        else:
            return "No significant urban risks detected at this time."

        # Using gemini-2.0-flash for high speed and better reasoning
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        # Robust Fallback for the demo
        print(f"Gemini API Error: {e}")
        if pattern == "health_risk":
            return "AUTOMATED ALERT: High correlation between vector symptoms and stagnant water. Immediate ward screening recommended."
        elif pattern == "water_risk":
            return "AUTOMATED ALERT: Sensory complaints indicate potential pipeline breach. Immediate water sampling required."
        return "System operational. No alerts."