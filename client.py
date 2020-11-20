from __future__ import print_function
import requests
import base64
import json

url = "http://localhost:8080"
test_url = url + '/resize_image'

file = {'image': open('sample.jpeg', 'rb')}

with open('sample.jpeg', 'rb') as f:
    im_b64 = base64.b64encode(f.read())

payload = {'input_jpeg': im_b64, 'desired_width':'200', 'desired_height':'100'}
r = requests.post(test_url, files=file, data=payload)
print(json.loads(r.text))