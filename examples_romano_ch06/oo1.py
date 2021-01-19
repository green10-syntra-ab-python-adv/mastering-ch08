class Person:
    def __init__(self, age):
        # in python this attribute is not "really" private
        self._age = age

    # Java style approach
    def get_age(self):
        return self._age

    # Java style approach
    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')


hans = Person(55)
print("Age of Hans, the proper way: ", hans.get_age())
hans.set_age(45)

# not forbidden though
print("Age of Hans, don't do this at home: ", hans._age)
hans._age = 135




