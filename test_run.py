import base64
import requests

image_file = open('/DSCN0010.jpg','rb').read()
base64data = base64.b64encode(image_file).decode("utf8")
payload = {'image': base64data}
r = requests.post("http://localhost:9000/2015-03-31/functions/function/invocations",json=payload)
print(r.json())