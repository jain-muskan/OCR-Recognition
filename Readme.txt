API used: https://api.ocr.space/parse/image

1. Register and obtain a free OCR API key at https://us11.list-manage.com/subscribe?u=ce17e59f5b68a2fd3542801fd&id=252aee70a1
( PDF page limit for free API key is 3) 
2. Send a simple POST request to the ocr.space API (mentioned above).
3. This request also contains either the name of the file to be extracted or it's url along with the payload.
4. API key, language and few optional paramters like filetype, isOverlayRequired, isTable are specified in the payload. 
5. For table like content in the file , set isTable to True. By doing this, the OCR logic makes sure that the parsed text result is always returned line by line.
6. This string returned as a result is converted to a json object for better retrieval and usage of key values. 
7. Entire output can be viewed using the ParsedText attribute of the ParsedResults objects of the resultant json object.
8. This ParsedResult object stores text line-wise and further word-wise. These words have associated features like 'Top','Left','Height','Width'.
9. Columns are differentiated based on the 'Left' attribute value whereas rows can be segragated using 'Top' attribute value.

API documentation : https://ocr.space/ocrapi
