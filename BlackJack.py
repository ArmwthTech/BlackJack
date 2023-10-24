import random

koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

# каждая карта обладает ценность. в колоде 4 масти и всего 36 карт. [6, 7, 8, 9, 10, 2, 3, 4, 11] все карты одной масти.

random.shuffle(koloda)

print("Поиграем в очко?")
count = 0

while True:
    choise = input("Будете брать карту? y/n \n")
    if choise == 'y':
        current = koloda.pop()
        print('Вам попалась карта : %d' % current)
        count += current
        if count > 21:
            print("У вас %d очков" % count)
            print("Вы проиграли")
            break
        elif count == 21:
            print("У вас %d очков" % count)
            print("Вы выйграли")
            break
        else:
            print("У вас %d очков" %count)
    elif choise == 'n':
        print('У вас %d очков и вы закончили игру.' %count)
        break


print("До новых встреч!")
