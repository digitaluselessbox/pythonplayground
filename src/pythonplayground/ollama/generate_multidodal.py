import base64
import requests

# OLLAMA API URLs
OLLAMA_URL = "http://localhost:11434/api/generate"

# LLM model to use
# MODEL = "gemma3:1b"
MODEL = "llava"

#load image
with open("sample_livingroom.jpg", "rb") as f:
    image_data = f.read()
    image_data_base64 = base64.b64encode(image_data).decode("utf-8")


data = {
    'model' : MODEL,
    'stream' : False,
    'prompt' : 'Describe the image provides',
    'images' : [ image_data_base64 ]

}

response = requests.post(OLLAMA_URL, json=data, timeout=600)

if response.status_code == 200:
    response_data = response.json()

    token_per_second = response_data["eval_count"] / response_data["eval_duration"] * 10**9
    print(f"Tokens per second: {token_per_second:.2f}")
    print("-" * 40)
    print(f"Answer: {response_data['response']}")

else:
    print(f"Error: {response.status_code} - {response.text}")
