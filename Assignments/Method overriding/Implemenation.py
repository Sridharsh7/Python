class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating instances of Animal, Dog, and Cat classes
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Calling the sound method on each instance
print(generic_animal.sound())  # Output: Some generic animal sound
print(dog.sound())             # Output: Bark
print(cat.sound())             # Output: Meow
