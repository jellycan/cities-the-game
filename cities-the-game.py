file = open ('all_cities.txt', 'r') #open the file with the info
all_cities = file.read().split('\n') #open file as a list and remove \n
file.close() #close the file after reading

used_cities = [ ] #all cities that were used during the game
counter = 0

print ('____________________________________________________________________________________________________________')
print ('Правила игры:')
print ('Введите город, который начинается на последнюю букву города предыдущего. Не забудьте переключиться на русский')
print ('Вы можете покинуть игру в любой момент, если напишите - Я устал, я мухожук')
print ()

''' первый раунд '''
first_city = input('Введите город: ')
letter = first_city[0]
letter.lower()
last_letter = first_city[-1]
used_cities.append(first_city)
if first_city in all_cities:
    all_cities.remove(first_city)
for i in all_cities:
    my_city = str(i)
    letter_1 = my_city[0]
    letter_my = letter_1.lower()
    if last_letter == letter_my:
        print ('мой ответ - '+my_city)
        all_cities.remove(i)
        last_letter_my = my_city[-1]
        if last_letter_my == 'ъ' or last_letter_my == 'ь':
            last_letter_my = my_city[-2]
        break

''' последующие раунды '''
i=0
while i!=-1:
    counter +=1
    print ()
    first_city = input('Введите город: ' )
    if first_city == 'Я устал, я мухожук':
        print ('Буу будет по Вам скучать!')
        print ('Вы продержались -', counter, 'раунда')
        break
    letter = first_city[0]
    letter.lower()
    last_letter = first_city[-1]
    if last_letter_my != letter:
        print ('Ваш город должен был начинаться на букву - '+ last_letter_my)
        print ('Вы продержались -', counter, 'раунда')
        break
    if first_city in used_cities:
        print ('Вы уже называли такой город')
        print ('Вы продержались -', counter, 'раунда')
        break
    if first_city in all_cities:
        all_cities.remove(first_city)
    if last_letter_my == letter:
        used_cities.append(first_city)
        for i in all_cities:
            my_city = str(i)
            letter_1 = my_city[0]
            letter_my = letter_1.lower()
            if last_letter == letter_my:
                print ('мой ответ - '+my_city)
                all_cities.remove(i)
                last_letter_my = my_city[-1]
                if last_letter_my == 'ъ' or last_letter_my == 'ь':
                    last_letter_my = my_city[-2]
                break
