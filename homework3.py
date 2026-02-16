from abc import ABC, abstractmethod

class UserAccount:
    def __init__(self, username, balance, password):
        self.username = username
        self._balance = balance
        self.__password = password

    def login(self, password):
        if self.__password == password:
            print(f"Добро пожаловать, {self.username}!")
            return True
        else:
            print("Неверный пароль!")
            return False

    @property
    def balance_info(self):
        return f"Ваш баланс: {self._balance} сом"

class NotificationService(ABC):
    @abstractmethod
    def send_to_phone(self, phone, text):
        pass

    @abstractmethod
    def send_to_email(self, email, text):
        pass

class XMLNotification(NotificationService):
    def send_to_phone(self, phone, text):
        xml_data = f"<message><to>{phone}</to><text>{text}</text></message>"
        print(f"Отправка XML на телефон:\n{xml_data}")

    def send_to_email(self, email, text):
        print(f"Отправка XML на почту {email}: {text}")

class JSONNotification(NotificationService):
    def send_to_phone(self, phone, text):
        print(f"Отправка JSON на телефон {phone}: {{'text': '{text}'}}")

    def send_to_email(self, email, text):
        print(f"Отправка JSON на почту {email}")

# user = UserAccount("Akylbek", 5000, "qase1004")
# user.login("qase1004")
# print(user.balance_info)

notify = XMLNotification()
notify.send_to_phone("+996552980410", "Ваш код: 1004")

