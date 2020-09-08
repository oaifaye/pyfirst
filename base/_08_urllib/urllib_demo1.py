# request:GET
import urllib.request
response = urllib.request.urlopen('https://www.jsdaima.com/Uploads/js/201902/1550716089/index.html')
print(response.read().decode('utf-8'))