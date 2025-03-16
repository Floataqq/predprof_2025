import requests

def get_tile():
    resp = requests.get("https://olimp.miet.ru/ppo_it/api").json()
    if resp['status'] != "ok":
        raise RuntimeError(f"Api return non-ok status `{resp['status']}` on /")
    return resp['message']


def get_coords():
    resp = requests.get("https://olimp.miet.ru/ppo_it/api/coords").json()
    if resp['status'] != "ok":
        raise RuntimeError(f"Api return non-ok status `{resp['status']}` on /coords")
    return resp['message']
