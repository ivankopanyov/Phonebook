from phonebook import Contact
from serializer import Serializer
from os.path import exists

# Класс, описывающий объект сериализации контактов
class ContactsSerializer(Serializer):

    # Метод сериализации контактов в xml
    def serialize(self, objs_list: list[Contact]) -> None:

        with open(self._file_name, 'w') as file:
            file.write('')

        with open(self._file_name, 'a', encoding='utf8') as file:
            for contact in objs_list:
                data = f'''<Contact>
    <name>{contact.get_name()}</name>
    <surname>{contact.get_surname()}</surname>
    <phone_number>{contact.get_phone_number()}</phone_number>
    <address>{contact.get_address()}</address>
</Contact>\n'''
                file.write(data)

    # Метод десериализации контактов из xml
    def deserialize(self) -> list[Contact]:

        if not exists(self._file_name):
            return []
        
        is_write = False
        contacts = []
        name, surname, phone_number, address = None, None, None, None
        with open(self._file_name, 'r', encoding='utf8') as file:
            for line in file:
                if line.find(f'</Contact>') != -1:
                    is_write = False
                    if name == None or surname == None or phone_number == None or address == None:
                        continue
                    contact = Contact(name, surname, phone_number, address)
                    contacts.append(contact)
                if is_write:
                    if line.find('<name>') != -1:
                        name = line.replace('<name>', '').replace('</name>', '').strip()
                    if line.find('<surname>') != -1:
                        surname = line.replace('<surname>', '').replace('</surname>', '').strip()
                    if line.find('<phone_number>') != -1:
                        phone_number = line.replace('<phone_number>', '').replace('</phone_number>', '').strip()
                    if line.find('<address>') != -1:
                        address = line.replace('<address>', '').replace('</address>', '').strip()
                if line.find(f'<Contact>') != -1:
                    name, surname, phone_number, address = None, None, None, None
                    is_write = True
        return contacts
