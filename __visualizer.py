#import numpy as np
from PIL import Image
import json
def visualize(arr: list[list[int]], name: str) -> str:
    ...
    '''
    """Функция, которая возвращает картинку.

    Args:
        arr (list[list[int]]): Массив данных из api

    Returns:
        str: path до картинки
    """
    color = (219,73,44)
    data = np.zeros((64,64,3), dtype=np.uint8)
    for i in range(64):
        for j in range(64):
            data[i,j] = [color[0] * (arr[i][j]/255), color[1] * (arr[i][j]/255), color[2] * (arr[i][j]/255)]
    image = Image.fromarray(data)      # Create a PIL image
    image.save(f"images/{name}.png")
    # image.show()
    '''
def visualizze(arr: list[list[int]], name: str) -> str:
    ...
    '''
    """Функция, которая возвращает картинку.

    Args:
        arr (list[list[int]]): Массив данных из api

    Returns:
        str: path до картинки
    """
    color = (219,73,44)
    data = np.zeros((256,256,3), dtype=np.uint8)
    for i in range(256):
        for j in range(256):
            if arr[i][j] == -1:
                data[i][j] = [111,232,220]
            else:
                data[i,j] = [color[0] * (arr[i][j]/255), color[1] * (arr[i][j]/255), color[2] * (arr[i][j]/255)]
    image = Image.fromarray(data)      # Create a PIL image
    image.save(f"images/{name}.png")
    image.show()
    '''
'''
if __name__ == "__main__":
    file = open("dump.txt").readlines()
    for x in range(16):
        e = json.loads(file[x])
        visualize(e["message"]["data"], f"{x}")
'''
