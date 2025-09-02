import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(query, chunks):
    context = "\n".join(chunks)
    prompt = f"""You are an assistant. Always reply in the following format:

Answer: <short answer>
Justification: <detailed reasoning>

Context:
{context}

Question: {query}
"""

    try:
        response = model.generate_content(prompt)
        text = response.text if hasattr(response, "text") else str(response)
    except Exception as e:
        return "Error: Could not get response from Gemini", str(e)

    # Extract answer + justification safely
    answer, justification = "Not provided", "Not provided"
    if "Answer:" in text:
        parts = text.split("Answer:", 1)[1].split("Justification:")
        answer = parts[0].strip()
        if len(parts) > 1:
            justification = parts[1].strip()

    return answer, justification
