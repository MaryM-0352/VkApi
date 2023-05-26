import argparse
from dataclasses import dataclass


@dataclass
class ParserArguments:
    PARSER = argparse.ArgumentParser("Vk API")
    PARSER.add_argument(dest="user_id",
                        type=int,
                        help="user ID you want to know"
                        )
    PARSER.add_argument('command',
                        type=str,
                        choices=['friends', 'liked_music', 'albums'],
                        help="parameters for searching of information"
                        )
    ARGS = PARSER.parse_args()
