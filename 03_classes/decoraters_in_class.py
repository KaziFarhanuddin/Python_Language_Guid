class Robot(object):
    def __init__(self, name, by):
        self.name = name
        # self.build_year = by

    @property
    def name(self):
        print("Hear I am")
        return self._name

    @name.setter
    def name(self, newname):
        if type(newname) == str:
            self._name = newname
        else:
            raise ValueError('In valide type, name should be a string')

    @property
    def build_year(self):
        return self._build_year

    # @build_year.setter
    # def build_year(self, newby):
    #     if newby.isdecimal():
    #         self._build_year = newby
    #     else:
    #         raise ValueError("It must be a year (e.g: 2019)")

somePerson = Robot('Name', '2019')
# somePerson.name = 12
print(somePerson.name)