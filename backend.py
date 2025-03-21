import json
from dumper import dumper
from __visualizer import visualize, visualizze
from lenapostaralas import get, getversh
from api import get_coords
from db_functions import add_tile1, add_base_point
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
    print(order)
    returnformax = [data[order[_]] for _ in range(16)]
    qqqq = [len(xxxx) for xxxx in returnformax]
    print(qqqq)
    arr = [[0 for _ in range(256)] for __ in range(256)]
    for ind in range(16):
        for i in range(64):
            for j in range(64):
                arr[64 * (ind // 4) + i][64 * (ind % 4) + j] = data[order[ind]][i][j]
    for q, _ in getversh(53,202,199,5,1,1,arr):
        xx,yy = q
        arr[xx][yy] = -1
    arr[53][202] = -1
    arr[199][5] = -1
    visualizze(arr, "2dd")
    return [returnformax, order]

def add_all_tiles_to_bd():
    file = open("dump.txt").readlines()
    order = do_map()[1]
    for i in order:
        add_tile1(file[i], i)

def add_science_points(api_url):
    data = get_coords(api_url)
    add_base_point(data["listener"][0], data["listener"][1], 0)
    add_base_point(data["sender"][0], data["sender"][1], 1)

def get_stations(api_url):
    data = get_coords(api_url)
    response = getversh(data["listener"][0], data["listener"][1], data["sender"][0], data["sender"][1], 0, 1)
    return response
visualise("https://olimp.miet.ru/ppo_it/api")
do_map()
add_all_tiles_to_bd()