from view import ConsoleView
from phonebook import Phonebook
from phonebookcontroller import PhonebookController
from contactsxmlserializer import ContactsXmlSerializer
from contactsjsonserializer import ContactsJsonSerializer
from logger import Logger
from traceback import format_exc

# Точка входа в приложение
def main() -> None:
    logger = Logger('phonebook.log')
    logger.write_log('Запуск приложения')
    try:
        phonebook = Phonebook()
        view = ConsoleView()
        jsonserializer = ContactsJsonSerializer('contacts.json')
        xmlserializer = ContactsXmlSerializer('contacts.xml')
        controller = PhonebookController(phonebook, view, jsonserializer, logger)
        controller.get_start_menu()
    except Exception:
        logger.write_log(format_exc())
    logger.write_log('Выход из приложения')

if __name__ == '__main__':
    main()