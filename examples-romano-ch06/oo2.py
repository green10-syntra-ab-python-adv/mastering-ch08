class Person:
    def __init__(self, age):
        # in python this attribute is not "really" private
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')


hans = Person(55)
print("Age of Hans (1): ", hans.age)

# elegant, pythonic, but setter is used
hans.age = 45
print("Age of Hans (2): ", hans.age)
hans.age = 135
print("Age of Hans (3): ", hans.age)




