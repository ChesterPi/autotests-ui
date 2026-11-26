# class Person: # это класс
#     pass

# tom = Person() # это объект класса
# bob = Person() # это объект класса

class Person():
    # это конструктор объекта
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

tom = Person("Tom", 22)
bob = Person("Bob", 43)
 
print(tom.name)         # Tom
print(bob.name)         # Bob



