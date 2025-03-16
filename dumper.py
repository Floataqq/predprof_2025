import requests
import hashlib

base_url = "https://olimp.miet.ru/ppo_it/api"

with open("dump.txt", 'w+') as f:
    tiles = set()
    while len(tiles) < 16:
        resp = requests.get(base_url)
        hash = hashlib.md5(resp.text.encode()).hexdigest()
        if hash not in tiles:
            f.write(resp.text + '\n')
        tiles.add(hash)
        print(f"Got {len(tiles)} tiles...")


