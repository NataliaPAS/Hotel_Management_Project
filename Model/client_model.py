from os.path import exists
from sqlalchemy import text
from Domain.clients import Client
from utils import engine

class ClientFileModel:
    def __init__(self, filename):
        self.__filename = filename
        self.__all_clients = []
        self.read_clients()