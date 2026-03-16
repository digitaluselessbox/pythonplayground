""" this file should read all bird images from the birds folder
and run them through the API, getting the names of the birds.
The results should be saved in a CSV file. """

import os
import csv
import base64
import requests


# OLLAMA API URLs
OLLAMA_URL = "http://localhost:11434/api/generate"

# LLM model to use
# MODEL = "gemma3:1b"
MODEL = "llava"

def read_image_as_base64(image_path: str) -> str:
    """Read an image file and return its content as a base64-encoded string."""
    with open(image_path, "rb") as f:
        image_data = f.read()
        image_data_string_base64 = base64.b64encode(image_data).decode("utf-8")

    return image_data_string_base64

def run_api_call(api_url: str, image_base64_string: str, model_name:str, timeout: int = 300) -> tuple:
    """ Run an API call to the specified URL with the given data and return the response as a string."""

    data = {
        'model' : model_name,
        'stream' : False,
        'prompt' : 'Act as a bird cataloguing AI. Output ONLY the name of the bird in the image and nothing else. Just one word!!!!!',
        'images' : [ image_base64_string ]
    }

    response = requests.post(api_url, json=data, timeout=timeout)

    return_string = ""
    token_per_second = 0

    if response.status_code == 200:
        response_data = response.json()

        token_per_second = response_data["eval_count"] / response_data["eval_duration"] * 10**9
        return_string = response_data['response']

    else:
        return_string = f"Error: {response.status_code} - {response.text}"

    return return_string, token_per_second


# steps

# 1. read all bird images from the birds folder
images = []

working_folder = os.path.dirname(__file__)
image_folder = os.path.join(working_folder, "birds")

for file in os.listdir(image_folder):
    file_path = os.path.join(image_folder, file)

    if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        images.append(
            {
                "name": file,
                "path": file_path,
                "description": "",
                "speed": 0
            }
        )

# 2. run them through the API, getting the names of the birds.

for image in images:
    image_string = read_image_as_base64(image["path"])
    api_answer = run_api_call(OLLAMA_URL, image_string, MODEL)

    print(f"API Answer for '{image['name']}': {api_answer[0]} (Speed: {api_answer[1]:.2f} T/s)")

    # image["description"], image["speed T/s"] = api_answer
    image["description"] = api_answer[0]
    image["speed"] = f"{api_answer[1]:.2f}"


# 3. The results should be saved in a CSV file.

with open(os.path.join(image_folder, "birds.csv"), 'w', newline='', encoding="utf-8") as csvfile:
    column_names = ['id', 'name', 'description', 'speed T/s']

    # article_writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    image_writer = csv.writer(csvfile, delimiter=';', quotechar='"', dialect='excel')
    image_writer.writerow(column_names)

    for image_index,image in enumerate(images, 1):
        image_writer.writerow(
            [image_index] +
            [image["name"]] +
            [image["description"]] +
            [image["speed"]]
        )

print("-"*40)
print("Birds saved to: " + os.path.abspath(csvfile.name))
