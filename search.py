import requests

from configure import Configuration


class Searching:
    @staticmethod
    def get_friend(user_id: int):
        user = {
            "user_id": user_id,
            "order": "name",
            "fields": "online"
        }
        res = requests.get(Configuration.ROOT + "friends.get",
                           params={**Configuration().config, **user})
        response_body = res.json()['response']
        friends = []
        for info in response_body['items']:
            friends.append(f"{info['first_name']} {info['last_name']}")
        return Searching.to_string(friends)

    @staticmethod
    def get_albums(user_id: int):
        user = {"owner_id": user_id}
        res = requests.get(Configuration.ROOT + "photos.getAlbums",
                           params={**Configuration().config, **user})
        response_body = res.json()['response']
        albums = []
        for info in response_body['items']:
            albums.append(info['title'])
        return Searching.to_string(albums)

    @staticmethod
    def get_music(user_id: int) -> str:
        user = {
            "user_id": user_id,
            "fields": "music"
        }
        res = requests.get(Configuration.ROOT + "users.get",
                           params={**Configuration().config, **user})
        response_body = res.json()['response']
        music = []
        for info in response_body:
            music.append(info['music'])
        return Searching.to_string(music)

    @staticmethod
    def to_string(data: list) -> str:
        res = ""
        for line in data:
            res += f"{line}\n"
        return res
