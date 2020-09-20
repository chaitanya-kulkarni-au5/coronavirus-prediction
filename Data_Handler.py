import asyncio
import json
from COVID import *
input1= []
@asyncio.coroutine
def Data(websocket, path):

    data = yield from websocket.recv()
    data = json.loads(data)
    for keys,values in data[0].items(): 
        if values == True:
            input1.append(1)
        else:
            input1.append(0)
    out1=Svc_classifier.predict([input1])
    str1 = str(out1[0])
    input1.clear()
    yield from websocket.send(str1)  
    

    



