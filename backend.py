import json
from dumper import dumper
from __visualizer import visualize
from lenapostaralas import get

def visualise(api_url):
    dumper(api_url)
    file = open("dump.txt").readlines()
    for x in range(16):
        e = json.loads(file[x])
        visualize(e["message"]["data"], f"{x}")

def do_map():
    data = []
    file = open("dump.txt").readlines()
    for x in range(16):
        e = json.loads(file[x])
        data.append(e["message"]["data"])
    print(get(data))


visualise('https://olimp.miet.ru/ppo_it/api')
do_map()