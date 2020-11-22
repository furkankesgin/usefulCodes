import speech_recognition as sr
r = sr.Recognizer()
import os
import datetime

inputFile = "/Users/furkan/Downloads/WhatsApp Audio 2020-11-11 at 11.23.59 AM.ogg"
outputFile = "/Users/furkan/Downloads/whatsappNewProj.WAV"
p = os.popen("ffmpeg -i \""+inputFile+"\" \""+outputFile+"\"")
p.read()

# import ffmpeg
# stream = ffmpeg.input('/Users/furkan/Downloads/whatsapp.ogg')
# stream = ffmpeg.hflip(stream)
# stream = ffmpeg.output(stream, '/Users/furkan/Downloads/WhatsApp.wav')
# ffmpeg.run(stream)


datetime_object = datetime.datetime.now()
print(datetime_object)
with sr.AudioFile(outputFile) as source:
    print("Say Something")
    print(source)
    audio = r.listen(source)
    print("time over, thanks")

try:
    print("TEXT : " + r.recognize_google(audio, language="tr-TR"))
except:
    pass
print(datetime_object)
datetime_object2 = datetime.datetime.now()
result=datetime_object2-datetime_object
print(result)
os.remove(outputFile)

# def explicit():
#     from google.cloud import storage

#     # Explicitly use service account credentials by specifying the private key
#     # file.
#     storage_client = storage.Client.from_service_account_json(
#         '/Users/furkan/Downloads/speechToText-2f998dfba26a.json')

#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)

# explicit()