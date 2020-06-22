from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

url = 'url' #Get URL From IBM-Service
key = IAMAuthenticator('key')   #Get Token From IBM-Service
version = '2020-04-22'

languageTranslator = LanguageTranslatorV3(version,key) #Creating APi
languageTranslator.set_service_url(url)  #seting url
jsonResponse = languageTranslator.list_identifiable_languages().get_result()  #To get the list of language supported by IBM_WATSON Api

# with open('/Users/VikramSingh/Pictures/PythonLearning/APIs_Python/LanguageJson.json','w') as jsonFile:
#     json.dump(jsonResponse,jsonFile)     #Saving the result into JSON file

with open('/Users/VikramSingh/Pictures/PythonLearning/APIs_Python/SpeechToText.txt','r') as sourceFile:
    with open('/Users/VikramSingh/Pictures/PythonLearning/APIs_Python/translatedFile.txt','w') as destFile:
        text_ = sourceFile.readline()
        print(text_)
        translated_response = languageTranslator.translate(text=text_,model_id='en-es')
        translated_result = translated_response.get_result()
        print(translated_result)
        result = translated_result['translations'][0]['translation']
        destFile.write(result)