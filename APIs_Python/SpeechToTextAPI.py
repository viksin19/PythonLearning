from ibm_watson import SpeechToTextV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url = 'url' 
key = IAMAuthenticator('key')

resultObj = SpeechToTextV1(key)
resultObj.set_service_url(url)
path = '/Users/VikramSingh/Pictures/PythonLearning/APIs_Python/SpeechToText.mp3'
with open(path,'rb') as wav:
    response = resultObj.recognize(audio=wav,content_type='audio/mp3')

    text = response.result['results'][0]['alternatives'][0]['transcript']
    with open('/Users/VikramSingh/Pictures/PythonLearning/APIs_Python/SpeechToText.txt','w') as textFile:
        textFile.write(text)