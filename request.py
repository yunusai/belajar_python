import requests
# mengambil source code dari suatu url

req = requests.get('https://api.github.com/events')
print ('\nResponses:\n' +req.text)