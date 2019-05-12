# This is to show how to encapsulate using class 
# decoraters

class Robot(object):
    def __init__(self, name, by):
        self.name = name

    @property
    def name(self):
        print("We call property name")
        return self.__name

    @name.setter
    def name(self, newname):
        print("This is the setter")
        if type(newname) == str:
            self.__name = newname
        else:
            raise ValueError('In valide type, name should be a string')

somePerson = Robot('Name', '2019')
somePerson.name = "farhan"
print(somePerson.name)