import requests

def get_tile(api_url):
    resp = requests.get(api_url).json()
    if resp['status'] != "ok":
        raise RuntimeError(f"Api return non-ok status `{resp['status']}` on /")
    return resp['message']


def get_coords(api_url):
    resp = requests.get(f"{api_url}/coords").json()
    if resp['status'] != "ok":
        raise RuntimeError(f"Api return non-ok status `{resp['status']}` on /coords")
    return resp['message']
