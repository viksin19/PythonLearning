from ibm_watson import SpeechToTextV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/396axxxxxxf817-aad4-4fa2-9fee-6481exxxxxxxxx1d1###32f4' 
key = IAMAuthenticator('UpmthTBVLxxxxxxxxxPe2nVWJ7CJwhXTe5axxxxxxxxxxFUYn7dVOZM3xxxXfN3qxxxSS')

resultObj = SpeechToTextV1(key)
resultObj.set_service_url(url)
path = '/Users/VikramSingh/Pictures/PythonLearning/APIs_Python/SpeechToText.mp3'
with open(path,'rb') as wav:
    response = resultObj.recognize(audio=wav,content_type='audio/mp3')

    text = response.result['results'][0]['alternatives'][0]['transcript']
    with open('/Users/VikramSingh/Pictures/PythonLearning/APIs_Python/SpeechToText.txt','w') as textFile:
        textFile.write(text)