import requests

class Post():
    def __init__(self) -> None:
        pass

    def get_post(self):
        self.response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
        self.response.raise_for_status()
        self.all_posts = self.response.json()
        return self.all_posts