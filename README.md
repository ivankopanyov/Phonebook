# Phonebook  
#### Телефонный справочник
Десктопное приложение для работы с контактами.
##### Содержание:
- [Внешние зависимости](#Внешние)
- [Запуск приложения](#Запуск)
- [Создание контакта](#Создание)
- [Просмотр и редактирование контакта](#Просмотр)
- [Удаление контакта](#Удаление)
- [Импорт контактов](#Импорт)
- [Поиск контакта](#Поиск)
- [Сортировка контактов](#Сортировка)
- [Экспорт контактов](#Экспорт)

# Внешние зависимости
Для работы приложения необходимо установить библиотеку TKinter.
```sh
pip install tk 
```

# Запуск приложения
Запуск приложения произаодится из файла main.py
```sh
python Путь_к_приложению\Phonebook\main.py
```

# Создание контакта
Для создания нового контакта нажмите кнопку "Создать контакт". В открывшемся диалоговом окне введите необходимую информацию о контатке и нажмите "ОК"
![Создание контакта](images/add_contact.png)

# Просмотр и редактирование контакта
Для просотра полной информации о контакте и ее изменения нажмите кнопку "Инфо" напротив необходимого контакта. В открывшемся диалоговом окне измените необходимую информацию и нажмите кнопку "ОК".
![Просмотр и редактирование контакта](images/info_contact.png)

# Удаление контакта
Для удаления контакта нажмите кнопку "Удалить" напротив необходимого контакта. В открывшемся диалоговом окне подтвердите действие.
![Удаление контакта](images/remove_contact.png)

# Импорт контактов
Для импорта контактов из файла нажмите кнопку "Импорт". В открывшемся диалоговом окне выберите необходимый файл в формате json или xml и нажмите кнопку "Открыть".
Для тестирования в каталоге приложения представлен файл "test_contacts.xml"
![Импорт контактов](images/import_contacts.png)

Если в приложении уже содержатся контакты, будет предложено их удалить. Выберите необходимое действие.
![Удаление контактов](images/old_contacts.png)

# Поиск контакта
Для поиска контакта в поле "Поиск" введите любую известную информацию о контакте. На экран будут выведены контакты, содержащие введенную информацию. Для вывода всех контактов очистите поле поиск.
![Поиск контакта](images/find_contact.png)

# Сортировка контактов
Для сортировки контактов нажмите на заголовок соответствующего столбца. Для обратной сортировки нажмите на него повторно.
![Сортировка контактов](images/sort_contacts.png)

# Экспорт контактов
Для экспорта контактов в файл нажмите кнопку "Экспорт". В открывшемся диалоговом окне перейдите в каталог для сохранения, выберите необходимый формат (json или xml), укажите имя файла и нажмите кнопку "Сохранить".
![Экспорт контактов](images/export_contacts.png)