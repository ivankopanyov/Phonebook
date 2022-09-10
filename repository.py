from abc import ABC, abstractmethod

# Абстрактный класс, описывающий репозиторий
class Repository(ABC):

    # Абстрактный метод, добавляющий объект в репозиторий
    @abstractmethod
    def add(self, obj: object) -> None:
        pass

    # Абстрактный метод поиска объекта в репозитории
    @abstractmethod
    def find(self, pattern: str) -> list[object]:
        pass
    
    # Абстрактный метод, удаляющий объект из репозитория
    @abstractmethod
    def remove(self, obj: object) -> None:
        pass
    
    # Абстрактный метод, возвращающий все объекты, содержащиеся в репозитории
    @abstractmethod
    def get_all(self) -> list[object]:
        pass