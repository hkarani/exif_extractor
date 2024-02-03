import base64
import requests
import re

def extract_exif_data(file_path):
    ###
    # The image passed in the file path is converted into base64
    # and sent to the server as a binary payload, the filename is also
    # sent for reconstrution on the server side
    ###
    image_file = open(file_path,'rb').read()
    base64data = base64.b64encode(image_file).decode("utf8")
    file_name = get_file_name(file_path)
    payload = {'image': base64data, 'file_name': file_name}
    r = requests.post("http://localhost:9000/2015-03-31/functions/function/invocations",json=payload)
    print(r.json())
    return r.json()

def get_file_name(file_path):
    # Extract file name from the path
    match = re.search(r'[^\\/]+$', file_path)
    
    if match:
        return match.group(0)
    else:
        #If the file path is just the file name (in the root folder)
        return file_path