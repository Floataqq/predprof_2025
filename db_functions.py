from __init__db import *
import json


def add_station(x: int, y: int, price: int, radius: int) -> None:
    """
    :param x: int
    :param y: int
    :param price: int
    :param radius: int
    :return: None
    """
    session = next(get_db())
    new_station = station(
        x = x,
        y = y,
        price = price,
        radius = radius
    )
    session.add(new_station)
    session.close()

def get_all_stations() -> list:
    """
    :return: list[station]
    """
    session = next(get_db())
    return session.query(station).all()

def add_tile1(string_value: str, num: int) -> int:
    """
    :param string_value: str
    :param num: int
    :return: id_of_current: int
    """
    session = next(get_db())
    new_tile = tile(
        num=num,
        json=string_value
    )
    session.add(new_tile)
    session.commit()
    cur_id = session.query(tile).filter_by(num=num).first().id
    if cur_id == cur_id:
        file = string_value.split('[[')[1].split(']]')[0]
        arr = [[int(j) for j in i[1:-1].split(',') if j != ''] for i in file.split('],[')]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                new_point = point(
                    tile_id=cur_id,
                    num=i * len(arr[i]) + j,
                    mean=arr[i][j]
                )
                session.add(new_point)
        session.commit()
    return cur_id

def get_all_tiles() -> list:
    """
    :return: list[tile]
    """
    session = next(get_db())
    return session.query(tile).order_by(tile.num).all()

def get_tile1(tile_id: int) -> tile:
    """
    :param tile_id: int
    :return: list
    """
    session = next(get_db())
    return session.query(tile).filter_by(id=tile_id).first()

def get_tile2(tile_id: int) -> list:
    """
    :param tile_id: int
    :return: list[User, list[list[int]]]
    """
    session = next(get_db())
    res_tile = session.query(tile).filter_by(id = tile_id).first()
    res_points = session.query(point).filter(point.tile_id == res_tile.id).order_by(point.num).all()
    res = [[0 for _ in range(64)] for _ in range(64)]
    for pt in res_points:
        res[pt.num // 64][pt.num % 64] = pt.mean
    result = [res_tile, res]
    return result

def add_base_point(x: int, y: int, is_listener: bool) -> None:
    """
    :param is_listener: bool
    :param x: int,
    :param y: int,
    :return: None
    """
    session = next(get_db())
    new_base_point = base_point(
        x = x,
        y = y,
        is_lisener = is_listener
    )
    session.add(new_base_point)
    session.commit()

def get_all_base_points() -> list:
    """
    :return: list[base_point]
    """
    session = next(get_db())
    return session.query(base_point).all()