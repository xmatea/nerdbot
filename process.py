import json
from collections import namedtuple
from json import JSONEncoder


def readjson(file):
    def decoder(dict):
        return namedtuple('JSONobj', dict.keys())(*dict.values())

    try:
        with open(file, encoding='utf8') as f:
            t = json.load(f, object_hook=decoder)
            return t
    except FileNotFoundError:
        raise FileNotFoundError("Could not find JSON file")

def colour_convert(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    rgb = tuple(int(hex[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))
    ival = (rgb[0]<<16) + (rgb[1]<<8) + rgb[2]
    if ival == 16777215:
        ival -= 1
    return ival
