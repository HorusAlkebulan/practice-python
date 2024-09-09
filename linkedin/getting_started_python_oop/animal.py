# animal.py


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"Animal {self.name} says '{self.sound}'!")


class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def bark(self):
        self.make_sound()

    def wag_tail(self):
        print(f"{self.name} is wagging her tail.")


class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def purr(self):
        self.make_sound()


if __name__ == "__main__":
    fido = Dog("Fido", "Woof!")
    mittens = Cat("Mittens", "Meow!")

    fido.make_sound()
    fido.bark()
    fido.wag_tail()

    mittens.make_sound()
    mittens.purr()
