class Person:

    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def print_person(self):
        print('Name: ',self.__name)
        print('Addr: ',self.__address)
        print('Phone: ',self.__phone_number)

class Customer(Person):

    def __init__(self, c_name, mailing_list):
        self.__customer_name = c_name
        self.__mailing_list = mailing_list

    def print_person(self):
        print('METHOD #1')
        print('Name: ',Person.get_name(self))
        print('Addr: ',Person.get_address(self))
        print('Phone: ',Person.get_phone_number(self))

        print()
        print()

        print('METHOD #2')
        Person.print_person(self)

        print('Customer Number: ')