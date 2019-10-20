import requests
import image

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/9b629fa2-43e4-4d94-823d-be32fe92e068/LabelUrls/'

headers = {
    'accept': 'application/x-www-form-urlencoded'
}

data = {'urls' : ['https://goo.gl/ICoiHc']}

response = requests.request('POST', url, headers=headers, auth=requests.auth.HTTPBasicAuth('Gfc5-Eh7M9XlJNyBDaSygH0jLx5L2038', ''), data=data)

print(response.text)

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/9b629fa2-43e4-4d94-823d-be32fe92e068/LabelFile/'

data = {'file': image.open('C:\Users\SNEHIL VERMA\Desktop\100775.jpg', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('Gfc5-Eh7M9XlJNyBDaSygH0jLx5L2038', ''), files=data)

print(response.text)

