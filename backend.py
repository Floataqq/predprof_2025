import json
from dumper import dumper
from __visualizer import visualize, visualizze
from lenapostaralas import get
from api import get_coords
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
    __temp = get(data)
    order = [__temp[i // 4][i % 4] for i in range(16)]
    returnformax = [data[order[_]] for _ in range(16)]
    arr = [[0 for _ in range(256)] for __ in range(256)]
    for ind in range(16):
        for i in range(64):
            for j in range(64):
                arr[64 * (ind // 4) + i][64 * (ind % 4) + j] = data[order[ind]][i][j]
    arr[53][202] = -1
    arr[199][5] = -1
    visualizze(arr, "goida")
    return returnformax


visualise('https://olimp.miet.ru/ppo_it/api')
do_map()