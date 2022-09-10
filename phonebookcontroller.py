from repositorycontroller import RepositoryController
from phonebook import Phonebook
from view import View
from contactsserializer import ContactsSerializer
from logger import Logger
from contact import Contact

# Класс, описывающий контроллер для работы с телефонным справочником
class PhonebookController(RepositoryController):

    # Инициализация объекта контроллера
    def __init__(self, model: Phonebook, view: View, serializer: ContactsSerializer = None, logger: Logger = None) -> None:
        super().__init__(model, view, serializer, logger)

        if self._serializer != None:
            contacts = self._serializer.deserialize()
            for contact in contacts:
                self._model.add(contact)

    # Метод отображения стартово экрана
    def get_start_menu(self) -> None:
        while True:
            self._view.new_screen()
            menu_items = [
                'Список контактов',
                'Поиск контакта',
                'Добавить контакт'
            ]
            num = self._view.output_menu(menu_items, back_name='Выход')

            if num == -1:
                return

            if num == 0:
                self.get_contacts(self._model.get_all())
            elif num == 1:
                self.find_contact()
            elif num == 2:
                self.add_contact()

    # Метод вывода списка всех котактов телефонного справочника
    def get_contacts(self, contacts: list[Contact]) -> None:
        self._view.new_screen()
        contacts_list = [f'{i.get_name()} {i.get_surname()} - {i.get_phone_number()}' for i in contacts]
        if len(contacts_list) == 0:
            self._view.output_message('Список контактов пуст!')
            self._view.output_menu([])
            return
        
        num = self._view.output_menu(contacts_list)

        if num == -1:
            return

        self.get_contact_info(contacts[num])
    
    # Метод вывода полной информации о контакте
    def get_contact_info(self, contact: Contact) -> None:
        self._view.new_screen()
        contact_dict = {
            'Имя' : contact.get_name(),
            'Фамилия' : contact.get_surname(),
            'Телефон' : contact.get_phone_number(),
            'Адрес' : contact.get_address()
        }

        self._view.output_dict(contact_dict)
        num = self._view.output_menu(['Удалить контакт'])

        if num == -1:
            return

        self.remove_contact(contact)

    # Метод добавления контакта в телефонный справочник
    def add_contact(self) -> None:
        self._view.new_screen()
        name = self._view.input_str('Укажите имя: ')
        surname = self._view.input_str('Укажите фамилию: ')
        phone_number = self._view.input_str('Укажите телефон: ')
        address = self._view.input_str('Укажите адрес: ')

        contact = Contact(name, surname, phone_number, address)
        self._model.add(contact)

        if self._logger != None:
            self._logger.write_log(f'Доавлен контакт {contact.to_str()}')
        self.__save()
        self._view.new_screen()
        self._view.output_message(f'Контакт {name} {surname} успешно добавлен!')
        self._view.output_menu([])

    # Метод удаления контакта из телефонного справочника
    def remove_contact(self, contact: Contact) -> None:
        self._view.new_screen()
        title = f'Вы уверены, что хотите удалить контакт {contact.get_name()} {contact.get_surname()}?'
        num = self._view.output_menu(['Удалить'], title, 'Отмена')

        if num == -1:
            return

        self._model.remove(contact)
        if self._logger != None:
            self._logger.write_log(f'Удален контакт {contact.to_str()}')
        self.__save()
        self._view.new_screen()
        self._view.output_message(f'Контакт {contact.get_name()} {contact.get_surname()} успешно удален!')
        self._view.output_menu([])

    # Метод поиска контакта в телефонном справочнике
    def find_contact(self) -> None:
        self._view.new_screen()
        pattern = self._view.input_str('Укажите строку для поиска (минимум 3 символа): ', 3)
        contacts = self._model.find(pattern)
        if len(contacts) == 0:
            self._view.output_message('Контакт не найден!')
            self._view.output_menu([])
            return
        self.get_contacts(contacts)

    # Метод сохранения списка контаков телефонного справочника в файл
    def __save(self) -> None:
        if self._serializer != None:
            self._serializer.serialize(self._model.get_all())