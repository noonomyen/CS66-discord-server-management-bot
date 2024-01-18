from sys import argv

import yaml

class Config:
    class Channel:
        def __init__(self, data: dict) -> None:
            self.ROLE: int = data["role"]
            self.DELETE_LOG: int = data["delete-log"]
            self.COMMAND: int = data["command"]

    class Role:
        def __init__(self, data: dict) -> None:
            self.SECTION_01: int = data["section-01"]
            self.SECTION_02: int = data["section-02"]
            self.SECTION_03: int = data["section-03"]
            self.CS66: int = data["cs66"]
            self.SS661: int = data["ss661"]
            self.SS662: int = data["ss662"]

    class Database:
        def __init__(self, data: dict) -> None:
            self.HOST: str = data["host"]
            self.PORT: int = data["port"]
            self.USER: str = data["user"]
            self.PASSWORD: str = data["password"]
            self.TLS: bool = data["tls"]
            self.DB: str = data["db"]

    def __init__(self, data: dict) -> None:
        self.TOKEN: str = data["token"]
        self.GUILD_ID: int = data["guild-id"]
        self.CHANNEL = self.Channel(data["channel"])
        self.ROLE = self.Role(data["role"])
        self.DATABASE = self.Database(data["database"])
        self.AUTO_SEND_MEESAGE_BUTTON_GIVE_ROLE = data["auto-send-message-button-give-role"]
        self.VERSION: str = data["version"]

config_file = "config.yaml"
if len(argv) == 2:
    config_file = argv[1]

CONFIG = Config(yaml.safe_load(open("config.yaml", "r", encoding="utf-8").read()))
