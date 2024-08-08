class UserManager:
    def __init__(self):
        self.users = {}  # Словарь для хранения пользователей с идентификаторами
        self.name_to_ids = {}  # Словарь для быстрого поиска идентификаторов по имени
        self.next_id = 1  # Счетчик для уникальных идентификаторов

    def addUser(self, name):
        user_id = self.next_id
        self.users[user_id] = name
        if name not in self.name_to_ids:
            self.name_to_ids[name] = []
        self.name_to_ids[name].append(user_id)
        self.next_id += 1
        return user_id

    def getUser(self, user_id):
        return self.users.get(user_id, None)

    def deleteUser(self, user_id):
        if user_id in self.users:
            name = self.users[user_id]
            del self.users[user_id]
            self.name_to_ids[name].remove(user_id)
            if not self.name_to_ids[name]:
                del self.name_to_ids[name]
            return True
        return False

    def findUserByName(self, name):
        return self.name_to_ids.get(name, [])

def main():
    userManager = UserManager()
    while True:
        print("\nВыберите действие:")
        print("1. Добавить пользователя")
        print("2. Найти пользователя по ID")
        print("3. Удалить пользователя по ID")
        print("4. Найти пользователей по имени")
        print("5. Выход")
        
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            name = input("Введите имя пользователя: ")
            user_id = userManager.addUser(name)
            print(f"Пользователь '{name}' добавлен. Его ID: {user_id}.")
        
        elif choice == '2':
            user_id = int(input("Введите ID пользователя: "))
            name = userManager.getUser(user_id)
            if name:
                print(f"Пользователь с ID {user_id} имеет имя '{name}'.")
            else:
                print("Пользователь с таким ID не найден.")
        
        elif choice == '3':
            user_id = int(input("Введите ID пользователя для удаления: "))
            if userManager.deleteUser(user_id):
                print(f"Пользователь с ID {user_id} был удален.")
            else:
                print("Пользователь с таким ID не найден.")
        
        elif choice == '4':
            name = input("Введите имя пользователя для поиска: ")
            ids = userManager.findUserByName(name)
            if ids:
                print(f"ID пользователей с именем '{name}': {ids}")
            else:
                print("Пользователи с таким именем не найдены.")
        
        elif choice == '5':
            print("Выход из программы.")
            break
        
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
