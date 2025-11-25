import json

def packetize(text: str):
    pack = {
            "text": text 
        }
    json_pack = json.dumps(pack)
    return json_pack

