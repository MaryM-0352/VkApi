from parsing import ParserArguments
from search import Searching


def run():
    args = ParserArguments.ARGS
    id = args.user_id
    match args.command:
        case "friends":
            print(Searching.get_friend(id))
        case "liked_music":
            print(Searching.get_music(id))
        case "albums":
            print(Searching.get_albums(id))


if __name__ == '__main__':
    run()
