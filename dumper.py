import requests
import hashlib

def dumper(api_url):
    with open("dump.txt", 'w+', encoding='utf8') as f:
        tiles = set()
        while len(tiles) < 16:
            resp = requests.get(api_url)
            hash = hashlib.md5(resp.text.encode()).hexdigest()
            if hash not in tiles:
                f.write(resp.text)
            tiles.add(hash)
            print(f"Got {len(tiles)} tiles...")


