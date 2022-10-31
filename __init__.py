from magic_config import Config


class KVClient:
    """
    Asinchronous implementation of MongoClient
    Singleton instance of storage for accessed to MongoDB
    """
    __instance: "KVClient" = None
    __client = None

    def __new__(cls, *args, **kwargs) -> "KVClient":
        """
        Create singleton instance of MongoClient
        """
        if not cls.__instance:
            cls.__instance = super(KVClient, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        super().__init__(*args, **kwargs)

    def __call__(self, collection):
        return self.__client(collection)

    @property
    def db(self):
        return super().db


# Initiate storage instance singleton
Storage = KVClient(Config.STORAGE_TYPE)
