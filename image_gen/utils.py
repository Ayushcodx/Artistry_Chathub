import json
import requests
from PIL import Image
import io
import re
from time import time

API_TOKEN = "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"  # token in case you want to use a private API
HEADERS = {
    # "Authorization": f"Bearer {API_TOKEN}",
    "X-Wait-For-Model": "true",
    "X-Use-Cache": "false"
}
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

def generate_image(prompt):
    data = json.dumps({"inputs": prompt})
    response = requests.request("POST", API_URL, headers=HEADERS, data=data)
    original_image = Image.open(io.BytesIO(response.content))

    # Resize the image to your desired dimensions (e.g., 500x500)
    resized_image = original_image.resize((500, 500))

    # Convert the image to bytes
    image_byte_array = io.BytesIO()
    resized_image.save(image_byte_array, format='PNG')
    image_content = image_byte_array.getvalue()

    return image_content
