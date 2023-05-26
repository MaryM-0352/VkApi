

class Configuration:
    ROOT = "https://api.vk.com/method/"
    FILENAME = "token.txt"
    API_VERSION = 5.131
    MAX_COUNT = 20

    def __init__(self):
        access_token = self.read_token(self.FILENAME)
        self.config = {
            "v": Configuration.API_VERSION,
            "access_token": access_token,
            "count": Configuration.MAX_COUNT
        }

    @staticmethod
    def read_token(filename):
        with open(filename, 'rb') as f:
            return f.read().decode()
