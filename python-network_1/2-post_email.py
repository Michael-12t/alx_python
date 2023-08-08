import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

print("Your email is:", email)
print(response.text)