import json
import requests

API_KEY = "your_api_key"
SYSTEM_PROMPT = "You are an AI assistant who creates entire blog article. The user will enter title by itself and you have to write an excellent blog out of it!"


def send_message(user_message):
    if not user_message.strip():
        return "Error: Empty message."
    
    request_body = {
        "contents": [{
            "parts": [{"text": SYSTEM_PROMPT + "\n" + user_message}]
        }]
    }
    
    try:
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}",
            headers={"Content-Type": "application/json"},
            data=json.dumps(request_body)
        )
        
        data = response.json()
        ai_response = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Error: No response received.")
        return ai_response
    except Exception as e:
        return f"Error: {str(e)}"


def chat():
    print("AI Chat - Type 'exit' to quit.")
    while True:
        user_input = input("Title: ")
        if user_input.lower() == "exit":
            break
        ai_reply = send_message(user_input)
        print(f"Blog: {ai_reply}\n")


if __name__ == "__main__":
    chat()