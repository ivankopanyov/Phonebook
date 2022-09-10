from abc import ABC, abstractmethod

# Абстрактный класс, описывающий сериалайзер
class Serializer(ABC):

    # Имя файла для чтения и записи
    _file_name: str = None

    # Инициализация объекта сериалайзера
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    # Абстрактный метод серализации объекта
    @abstractmethod
    def serialize(self, objs_list: list[object]) -> None:
        pass

    # Абстрактный метод десерализации объекта
    @abstractmethod
    def deserialize(self) -> list[object]:
        pass