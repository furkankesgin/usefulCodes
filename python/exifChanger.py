# import datetime
# def replace_exif(file, datetime_object):
#     from PIL import Image
#     import piexif
#     img = Image.open(file)
#     try:
#         exif_dict = piexif.load(img.info['exif'])
#         print(f"Exif load for file '{file}'' successful")
#     except KeyError:
#         print(f"No Exif data for file '{file}', creating Exif data instead...")
#         exif_dict = {}
#         exif_dict["0th"] = {}
#         exif_dict["Exif"] = {}
#     d = datetime_object.strftime("%Y:%m:%d %H:%M:%S")
#     exif_dict["Exif"][36868] = d.encode("utf-8")
#     exif_dict["Exif"][36867] = d.encode("utf-8")
#     exif_dict["0th"][306] = d.encode("utf-8")
#     exif_bytes = piexif.dump(exif_dict)
#     piexif.insert(exif_bytes, file)
#     print(f"Exif data replacement for file '{file}' successful")
# x = datetime.datetime(2019,11,19,15,10,35)
# replace_exif("C:\\Users\\Furkan\Desktop\\yedekle\\sandiskssd\\macDesktop\\Bakilacak\\dene\\WhatsApp Image 2019-11-19 at 3.10.35 PM.jpeg",x)

from datetime import datetime
import piexif

filename = 'C:\\Users\\Furkan\Desktop\\yedekle\\sandiskssd\\macDesktop\\Bakilacak\\dene\\WhatsApp Image 2019-11-19 at 3.10.35 PM.jpeg'
exif_dict = piexif.load(filename)
new_date = datetime(2018, 1, 1, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
exif_bytes = piexif.dump(exif_dict)
piexif.insert(exif_bytes, filename)