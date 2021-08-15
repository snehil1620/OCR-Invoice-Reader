import requests

url = 'https://app.nanonets.com/api/v2/OCR/Model/4323c454-958f-4b55-8b06-558dbbb2dfdc/LabelFile/'

data = {'file': open('YOUR_IMAGE_PATH', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('mYyXQ5AFq8zGKNrDWVl-f4vmrkcl7d6_', ''), files=data)

print(response.text)

