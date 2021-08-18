import pet


def main():
    name = input('Имя вашего питомца: ')
    animal_type = input('Тип вашего питомца(птица, кот, собака и т.д.): ')
    age = input('Возраст питомца: ')
    my_pet = pet.Pet(name, animal_type, age)
    print()
    print('Карточка вашего питомца\n'
          '_____________________________________________')
    print('Имя', my_pet.get_name())
    print('Тип', my_pet.get_animal_type())
    print('Возраст', my_pet.get_age())


main()