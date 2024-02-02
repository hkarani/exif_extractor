import sys,json
import base64
from PIL import Image
from io import BytesIO
def handler(event, context):
    if event['image']:
        image_bytes = event['image'].encode('utf-8')
        img_b64dec = base64.b64decode(image_bytes)
        img_byteIO = BytesIO(img_b64dec)
        image = Image.open(img_byteIO)
        exif_data = image.getexif()
        
        filename = image.filename if image.filename is not None else "Null"
        fileformat = image.format if image.format is not None else "Null"
        imagesize = image.size if image.size is not None else "Null"
        bitspersample = exif_data.get(258) if exif_data.get(258) is not None else "Null"
        datetimeoriginal = exif_data.get(36867) if exif_data.get(36867) is not None else "Null"
        exposuretime = exif_data.get(33434) if exif_data.get(33434) is not None else "Null"
        isanimated = getattr(image, "is_animated", False)
        imageheight = image.height if image.height is not None else "Null"
        imagewidth = image.width if image.width is not None else "Null"
        yresolution = exif_data.get(283) if exif_data.get(283) is not None else "Null"
        xresolution = exif_data.get(282) if exif_data.get(282) is not None else "Null"
        model = exif_data.get(272) if exif_data.get(272) is not None else "Null"
        make = exif_data.get(271) if exif_data.get(271) is not None else "Null"
        datecreated = exif_data.get(306) if exif_data.get(306) is not None else "Null"
        orientation = exif_data.get(274) if exif_data.get(274) is not None else "Null"
        imagedescription = exif_data.get(270) if exif_data.get(270) is not None else "Null"
        ycbcrsubsampling = exif_data.get(530) if exif_data.get(530) is not None else "Null"
        software = exif_data.get(305) if exif_data.get(305) is not None else "Null"
        flash = exif_data.get(37385) if exif_data.get(37385) is not None else "Null"
        gpslatitude = exif_data.get(2) if exif_data.get(2) is not None else "Null"
        gpslatituderef = exif_data.get(1) if exif_data.get(1) is not None else "Null"
        gpslongitude = exif_data.get(4) if exif_data.get(4) is not None else "Null"
        gpslongituderef = exif_data.get(3) if exif_data.get(3) is not None else "Null"
        
        exif_data_dictionary = {
            "filename": filename,
            "fileformat": fileformat,
            "imagesize": str(imagesize),
            "bitspersample": bitspersample,
            "datetimeoriginal": datetimeoriginal,
            "exposuretime": str(exposuretime),
            "isanimated": isanimated,
            "imageheight": imageheight,
            "imagewidth": imagewidth,
            "xresolution": str(xresolution),
            "yresolution": str(yresolution),
            "model": model,
            "make": make,
            "datecreated": datecreated,
            "flash": flash,
            "orientation": orientation,
            "imagedescription": imagedescription,
            "ycbcrsubsampling": ycbcrsubsampling,
            "software": software,
            "gps" : {
                "gpslatituderef": gpslatituderef,
                "gpslatitude": str(gpslatitude),
                "gpslongituderef": gpslongituderef,
                "gpslongitude": str(gpslongitude)        
            }            
        }
        exif_json = json.dumps(exif_data_dictionary)
        return {
        'statusCode': 200,
        'body': exif_json,
        'headers': {
            'Content-Type': 'application/json'
            }
        }

    return {
        'statusCode': 204,
        'body': {'Message': 'No image was sent'},
        'headers': {
            'Content-Type': 'application/json'
            }
        }


        
   
    