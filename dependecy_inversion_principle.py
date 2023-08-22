import random
from abc import ABC, abstractmethod

memory = {}

class InterfaceUser(ABC):

    @classmethod
    @abstractmethod
    def save_user(username: str):
        """save user"""

    @classmethod
    @abstractmethod
    def list_user() -> list[dict[int, str]]:
        """list users"""


class PostgreSQLUser(InterfaceUser):
    def save_user(self, username: str):
        memory[random.randint(1, 100)] = username

    def list_user(self) -> list[dict[int, str]]:
        return [{y,x} for y,x in memory.items()]


class ServiceUser(object):

    def __init__(self, drive: InterfaceUser) -> None:
        self.drive = drive

    def service_save_user(self, username: str):
        return self.drive.save_user(username)

    def service_list_user(self):
        return self.drive.list_user()


if __name__ == '__main__':
    driver = PostgreSQLUser()

    svc = ServiceUser(drive=driver)
    svc.service_save_user("david")
    svc.service_save_user("lucas")
    print(svc.service_list_user())
