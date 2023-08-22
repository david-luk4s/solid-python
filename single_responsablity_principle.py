from abc import ABC, abstractmethod

class InterfaceObj(ABC):

    @classmethod
    @abstractmethod
    def list_pages():
        """list pages"""

    @classmethod
    @abstractmethod
    def add_page():
        """add pages"""


class Blog(InterfaceObj):

    def __init__(self) -> None:
        self.pages = []

    def add_page(self, page: str) -> None:
        self.pages.append(page)

    def list_pages(self) -> list[str]:
        return self.pages


class Persistence(object):
    def __init__(self, 
                 obj: InterfaceObj,
                 file_name = 'db.txt') -> None:
        self.obj = obj
        self.file_name = file_name

    def save_pages(self):
        f = open(self.file_name, 'w')
        f.writelines("\n".join(self.obj.list_pages()))
        f.close()

    def load_pages(self):
        f = open(self.file_name, "r")
        for itm in f.read().split("\n"):
            self.obj.add_page(itm)
        f.close()

if __name__ == '__main__':
    blog = Blog()
    blog.add_page("home")
    blog.add_page("about my")

    st = Persistence(blog)
    st.save_pages()
    #st.load_pages()

    print(blog.list_pages())
