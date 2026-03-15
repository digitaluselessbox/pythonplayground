import requests

# OLLAMA API URLs
OLLAMA_URL = "http://localhost:11434/api/chat"

# LLM model to use
# MODEL = "gemma3:1b"
MODEL = "llama3.1:8b-instruct-q4_K_M"

data = {
    'model' : MODEL,
    'stream' : False,
    'messages' : []
}

# system:       chatbot behavior, System Prompt
# user:         user input, user message
# assistant:    assistant response, assistant message

# system prompt
data['messages'].append({
    "role": "system",
    "content": "You are a specialist for Grimm fairy tales. Answer questions about the Grimm fairy tales and their characters."
})


while True:
    user_input = input("User: ")
    if user_input.lower() in {"exit", "quit"}:
        break

    data['messages'].append({
        "role": "user",
        "content": user_input
    })

    response = requests.post(OLLAMA_URL, json=data, timeout=180)

    if response.status_code == 200:
        response_data = response.json()

        data['messages'].append(response_data['message'])

        token_per_second = response_data["eval_count"] / response_data["eval_duration"] * 10**9
        print(f"Tokens per second: {token_per_second:.2f}")
        print("-" * 40)
        print(f"Answer: {response_data['message']['content']}")
        print("-" * 40)


    else:
        print(f"Error: {response.status_code} - {response.text}")
        break
