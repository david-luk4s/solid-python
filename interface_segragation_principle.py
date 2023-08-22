from abc import ABC, abstractmethod

class Routine(ABC):

    @classmethod
    @abstractmethod
    def start_work():
        """starting work"""
    
    @classmethod
    @abstractmethod
    def pause_work():
        """pause work"""

    @classmethod
    @abstractmethod
    def finaly_work():
        """finaly work"""

class Human(Routine):
    def __init__(self) -> None:
        self.whos = Human.__name__        

    def start_work(self):
        print(f"""{self.whos} - starting work""")

    def pause_work(self):
        print(f"""{self.whos} - pause work""")

    def finaly_work(self):
        print(f"""{self.whos} - finaly work""")

    def take_coffee(self):
        print(f"""{self.whos} - take to coffee""")


class Robot(Routine):
    def __init__(self) -> None:
        self.whos = Robot.__name__

    def start_work(self):
        print(f"""{self.whos} - starting work""")

    def pause_work(self):
        print(f"""{self.whos} - pause work""")

    def finaly_work(self):
        print(f"""{self.whos} - finaly work""")

    def load_battery(self):
        print(f"""{self.whos} - load battery""")

if __name__ == '__main__':
    human = Human()
    human.start_work()
    human.pause_work()
    human.take_coffee()
    human.start_work()
    human.finaly_work()


    robot = Robot()
    robot.start_work()
    robot.pause_work()
    robot.load_battery()
    robot.start_work()
    robot.finaly_work()
