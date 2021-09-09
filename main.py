import requests
import json
import pandas as pd


def ocr_space_file(filename, overlay=False, api_key='6c069c4d1188957', language='eng'):
   
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'isTable': True
               
               }
    try:
        with open(filename, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                            files={filename: f},
                            data=payload,
                            
                            )
        return r.content.decode()
    except FileNotFoundError:
        print("File name invalid")

try:
    test_file = ocr_space_file(filename='BillScanned.pdf')
    print(type(test_file))
    tf= json.loads(test_file)
    #print(tf)
    print(tf['ParsedResults'][0]['ParsedText'])
except TypeError:
    print("No parsed data,recheck the file name and parameters passed to the request object")
except KeyError:
    print(tf['ErrorMessage'][0])

