class Person:
    def __init__(self, name = '', surname = '', telephone = '', year=1):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.__year = year
        if year < 18:
            print(self.__repr__())

    def __repr__(self):
        return(self.name + ", ваш возраст должен быть 18, а не " + str(self.__year))

    def printPerson(self):
        print(self.__str__)

    def __str__(self):
        return "{} \t  {} \t{} \t{}".format(self.name, self.surname, self.telephone, self.__year)
