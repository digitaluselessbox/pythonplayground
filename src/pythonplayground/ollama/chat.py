import requests

# OLLAMA API URLs
OLLAMA_URL = "http://localhost:11434/api/chat"

# LLM model to use
MODEL = "gemma3:1b"
# MODEL = "llava"

data = {
    'model' : MODEL,
    'stream' : False,
    'messages' : []
}

# example message:
data['messages'].append({
    "role": "user",
    "content": "What is the name of the witch in the Hansel and Gretel fairy tale?"
})

response = requests.post(OLLAMA_URL, json=data, timeout=180)

if response.status_code == 200:
    response_data = response.json()

    token_per_second = response_data["eval_count"] / response_data["eval_duration"] * 10**9
    print(f"Tokens per second: {token_per_second:.2f}")
    print("-" * 40)
    print(f"Answer: {response_data['message']['content']}")

else:
    print(f"Error: {response.status_code} - {response.text}")
