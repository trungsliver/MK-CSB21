# Các tính chất của OOP:
    # 1. Tính đóng gói (Encapsulation)
from abc import abstractmethod


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance                # private attribute

    def get_balance(self):
        return self.__balance
    
ba1 = BankAccount("123456789", 1000)
# print(ba1.__balance) # Lỗi: AttributeError
print(ba1.get_balance())  # Đúng: In ra số dư tài khoản

    # 2. Tính kế thừa (Inheritance)
class Animal:
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    def speak(self):
        return "Animal sound"
    @abstractmethod
    def move(self): # tính trừu tượng
        pass
    
class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self): # tính đa hình
        return "Woof! Woof!"
    def move(self):
        return "The dog is running"

dog1 = Dog("Scooby", 3, "Brown")
print(dog1.speak())
print(dog1.move())

    # 3. Tính đa hình (Polymorphism)
    # 4. Tính trừu tượng (Abstraction)
