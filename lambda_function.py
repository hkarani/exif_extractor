import sys,json
import base64
from PIL import Image
from PIL import ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
from io import BytesIO
def handler(event, context):
    if event['image']:
        image_bytes = event['image'].encode('utf-8')
        img_b64dec = base64.b64decode(image_bytes)
        filename = event['file_name']
            
        with open(filename, "wb") as image_file:
            image_file.write(img_b64dec)
            image = Image.open(filename)
            exif_data = image.getexif()
            gps_ifd = exif_data.get_ifd(ExifTags.IFD.GPSInfo)
            exif_ifd = exif_data.get_ifd(ExifTags.IFD.Exif)
            makernote_ifd = exif_data.get_ifd(ExifTags.IFD.Makernote)
            interop_ifd = exif_data.get_ifd(ExifTags.IFD.Interop)
            ifd1_ifd = exif_data.get_ifd(ExifTags.IFD.IFD1)
            
            image_info = {
                "Filename": filename,
                "Image Size": image.size,
                "Image Height": image.height,
                "Image Width": image.width,
                "Image Format": image.format,
                "Image Mode": image.mode,
                "Image is Animated": getattr(image, "is_animated", False),
                "Frames in Image": getattr(image, "n_frames", 1)                
            }
            
            gps_info = {}
            exif_info = {}
            makernote_info = {}
            interop_info = {}
            ifd1_info = {}

            for key, value in gps_ifd.items():
                tagname = GPSTAGS.get(key, key)
                gps_info[tagname] = str(value)

            for key, value in exif_ifd.items():
                tagname = TAGS.get(key, key)
                exif_info[tagname] = str(value)
                
            for key, value in makernote_ifd.items():
                tagname = TAGS.get(key, key)
                makernote_info[tagname] = str(value)
    
            for key, value in interop_ifd.items():
                tagname = TAGS.get(key, key)
                interop_info[tagname] = str(value)
                
            for key, value in ifd1_ifd.items():
                tagname = TAGS.get(key, key)
                ifd1_info[tagname] = str(value)
            
            metadata_dict = {
                "ImageDetails": image_info,
                "ExifData": exif_info,
                "GPSInfo": gps_info,
                "InteropData": interop_info,
                "IFD1Data": ifd1_info,
                "MakernoteData": makernote_info
            }

        exif_json = json.dumps(metadata_dict, default=str)
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


        
def base64_to_file(base64_data, output_file_path):
    
    with open(output_file_path, 'wb') as output_file:
        output_file_path.write()
    