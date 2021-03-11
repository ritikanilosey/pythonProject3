import datetime


class Pet(object):
    def __init__(self):
        self.age = 0

    def set_name(self, name):
        self.name = name

    def set_species(self, species):
        self.species = species

    def set_breed(self, breed):
        self.breed = breed

    def set_color(self, color):
        self.color = color

    def set_gender(self, gender):
        self.gender = gender

    def set_owner(self, owner):
        self.owner = owner

    def set_address(self, address):
        self.address = address

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_breed(self):
        return self.breed

    def get_color(self):
        return self.color

    def get_gender(self):
        return self.gender

    def get_owner(self):
        return self.owner

    def get_address(self):
        return self.name

    def get_birthdate(self):
        return self.birthdate

    def getAge(self):
        if (self.age == 0):
            self.age = datetime.date.today() - self.birthdate
        return self.age

    def __str__(self):
        return "%s is a %s,%s,%s,%s,%s,%s,%s" % (
        self.name, self.species, self.breed, self.color, self.gender, self.owner, self.address, self.birthdate)


class Dog(Pet):
    def __init__(self, breed, name, color, gender, species='canis familiaris'):
        super().__init__()
        self.set_breed(breed)
        self.set_name(name)
        self.set_color(color)
        self.set_gender(gender)
        self.set_species(species)


class Puppy(Dog):
    def getAge(self):
        return f"{Pet.getAge(self) * 12} months old"

    def play(self):
        return (" (___()'`;\n /, /`\n \\\\\"--\\\\")


def main():
    name = "Sheru"
    breed = "Golden Retriever"
    color = "golden"
    gender = "female"
    owner = "Ritika"
    address = "Mountainview, CA"
    birthdate = datetime.date(2010, 4, 14)

    puppy = Puppy(breed, name, color, gender)
    puppy.set_owner(owner)
    puppy.set_address(address)
    puppy.set_birthdate(birthdate)

    print(puppy.get_name())
    print(puppy.get_species())
    print(puppy.get_birthdate())
    print(puppy.play())
    print(puppy.getAge())


main()






