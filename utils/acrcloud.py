import hmac
import hashlib
import base64
import time
import os
import requests

from dotenv import load_dotenv
load_dotenv()

ACR_HOST = os.getenv("ACR_HOST")
ACR_KEY = os.getenv("ACR_KEY")
ACR_SECRET = os.getenv("ACR_SECRET")

def recognize_acrcloud(audio_file_path):
    http_method = "POST"
    http_uri = "/v1/identify"
    data_type = "audio"
    signature_version = "1"
    timestamp = str(int(time.time()))

    string_to_sign = f"{http_method}\n{http_uri}\n{ACR_KEY}\n{data_type}\n{signature_version}\n{timestamp}"
    sign = base64.b64encode(hmac.new(ACR_SECRET.encode('ascii'), string_to_sign.encode('ascii'), digestmod=hashlib.sha1).digest()).decode('ascii')

    files = {
        'sample': open(audio_file_path, 'rb'),
        'access_key': ACR_KEY,
        'data_type': data_type,
        'signature': sign,
        'signature_version': signature_version,
        'timestamp': timestamp,
    }

    url = f"http://{ACR_HOST}/v1/identify"
    response = requests.post(url, files=files)
    return response.json()
