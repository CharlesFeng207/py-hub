import json


class Settings:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
    socks_proxy = None
    http_proxy = None
    https_proxy = None
    cookies = None

    @staticmethod
    def load_json_cookies(path):
        with open(path, 'r') as f:
            Settings.cookies = json.load(f)

    @staticmethod
    def get_full_socks_proxy():
        return "socks5://" + Settings.socks_proxy

