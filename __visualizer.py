import numpy as np
from PIL import Image
def visualize(arr: list[list[int]], name: str) -> str:
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
    image.show()
if __name__ == "__main__":
    YOUR_MOTHER = []
    visualize(YOUR_MOTHER, "your_mother")