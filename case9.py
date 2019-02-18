def event():

    a = randint(1, 3)
    money = randint(100, 200)
    if a == 1:
        print("\n ВНИМАНИЕ!\n")
        t = randint(1, 7)
        independent_event = {1: "Мой Король, с прискорбием сообщаем Вам, что этой ночью споткнулся о свою ногу и "
                                "трагически погиб троюродный брат Вашего кузена! \n Надеемся, эта скромненькая сумма "
                                "сгладит горечь утраты! Зачисленно в казну:  ",
                             2: "Ночью неизвестные ворвались в замок, и таинственным образом обойдя охрану, "
                                "украли из казны золотые слитки стоимостью:",
                             3: "Всю неделю дождь лил как из ведра, была затоплена часть земель на юге Королевства."
                                " Никто не защищен от природных катаклизмов, Мой Король! \n Пришлось выделить народу "
                                "компенсацию в размере: ",
                             4: "Арабский шейх в знак уважения Вашему Величеству подарил золотые часы, стоимостью: ",
                             5: "На Королевство напала страшная болезнь! Чума унесла жизни четверти населения!",
                             6: "Бог плодородия дарит Вам 100 мешков зерна. Не благодарите ;)",
                             7: "Бог плодородия погневался на Вас за пренебрежительное отношение к Матушке Земле."
                                "Минус 100 мешков зерна!"}
        if t == 1 or t == 4:
            data["Казна"] += money
            print(independent_event[t], money)
        elif t == 2 or t == 3:
            data["Казна"] -= money
            print(independent_event[t], money)
        elif t == 5:
            data["Народ"] -= int(data["Народ"]/4)
            print(independent_event[t])
        elif t == 6:
            data["Зерно"] += 100
            print(independent_event[t])
        elif t == 7:
            data["Зерно"] -= 100
            print(independent_event[t])
        results()
    elif a == 2:
        print("\n ВНИМАНИЕ!")
        event1 = randint(1, 2)

        dependent_event = {1: "Король Свинландии объявил Вам войну."
                              " Вы можете отдать королю четверть Ваших земель и казны, тогда король "
                              "откажется от нападения, или попытать свои силы и вступить в войну. \n"
                              " Если хотите попытать свои силы и начать войну, введите 'да', иначе, введите 'нет':  ",
                           2: "От Сообщества Придворных алхимиков поступило предложение о разработке нового вида "
                              "удобрений для выращивания зерна.\n Стоимость исследования: 5 золотых, 1 мешок пшеницы. "
                              "Согласны ли Вы? Введите: 'да' или 'нет': ",
                           3: "На главной Площади Нашего Королевства голодные ремесленники устроили забастовку."
                              " Если желаете подавить мятеж силой, введите 'да', если хотите решить конфликт миром,"
                              " отдав часть пшеницы, введите 'нет': ",
                           4: "Ваш Тайный Советник предлагает законопроект об увеличении налогов. Если хотите "
                              "подписать, введите 'да', иначе введите 'нет': "}
        outcome = {1: "К сожалению, Вы проиграли войну! Погибли  люди, казна, земля заметно поубавились..."
                                    "Текущие положение: ",
                   2: "Поздравляю, Мой Король! Мы победили несчастных свинландцев! Королю Свинландии пришлось "
                      "выплатить контрибуцию, заметно прибавилось зерно! Текущее положение: ",
                   3: "Эврика! Ученым удалось вывести новый сорт удобрений, в связи с этим увеличиваются запасы "
                      "пшеницы. Текущее положение: ",
                   4: "О нет! Разработка ученых потерпела крах! Текущее положение: ",
                   5: "Вы решили не поддерживать отечественную науку, что ж, ученые мигрировали в соседнее королево, "
                      "Ваш Авторитет падает на 1 значение. Текущее положение: ",
                   6: "Вы сделали правильный выбор. Оказалось, что ученые совершили ошибку в формуле, из-за чего "
                      "исследование бы провалилось! Вам начисляется 1 балл Авторитета",
                   7: "Вы приняли верное решение. Весть о вашей удачной операции разнеслась по всей стране."
                      " Смута снижается. Текущее положение: ",
                   8: "Весть о кровавой расправе над бедными ремесленниками разнеслась по всему Королевству! "
                      "Авторитет снижается. Текущее положение: ",
                   9: "Народ перестал бастовать. Зерно уменьшается, авторитет растет. Текущее положение: ",
                   10: "Налоговое бремя задавило четверть населения, многие мигрировали из страны. Авторитет снижается. "
                       "Текущее положение: ",
                   11: "Законопроект пошел на пользу, однако Смута увеличивается на 1 значение."
                       " Казна, зерно увеличиваются. Текущее положение: "}

        print(dependent_event.get(event1))
        answer = input()
        if event1 == 1 and answer == 'да':
            out = randint(1, 2)
            print(outcome[out])
            if out == 1:
                data["Казна"] -= int(data["Казна"] / 5)
                data["Народ"] -= int(data["Народ"] / 3)
                data["Земля"] -= int(data["Земля"] / 4)
            elif out == 2:
                data["Казна"] += int(data["Казна"] / 2)
                data["Зерно"] += int(data["Зерно"] / 3)
                data["Земля"] += int(data["Земля"] / 4)
                data["Авторитет"] += 2
        elif event1 == 1 and answer == 'нет':
            data["Казна"] -= int(data["Казна"] / 4)
            data["Земля"] -= int(data["Казна"] / 4)
            print("Что ж, разумное решение. Текущее положение: \n")
        elif event1 == 2 and answer == "да":
            out = randint(3, 4)
            data["Казна"] -= 5
            data["Зерно"] -= 1
            print(outcome[out])
            if out == 3:
                data["Зерно"] += 200
            elif out == 4:
                pass
        elif event1 == 2 and answer == "нет":
            out = randint(5, 6)
            print(outcome[out])
            if out == 5:
                data["Авторитет"] -= 1
            elif out == 6:
                data["Авторитет"] += 1
        elif event1 == 3 and answer == "да":
            out = randint(7, 8)
            print(outcome[out])
            if out == 7:
                data["Смута"] -= 1
            elif out == 8:
                data["Авторитет"] -= 1
        elif event1 == 3 and answer == "нет":
            print(outcome[9])
            data["Авторитет"] += 1
            data["Зерно"] -= 150
        elif event1 == 4 and answer == "да":
            out = randint(10, 11)
            print(outcome[out])
            if out == 10:
                data["Народ"] -= int(data["Народ"] / 4)
                data["Авторитет"] -= 1
            elif out == 11:
                data["Смута"] += 1
                data["Казна"] += int(data["Казна"] / 4)
                data["Зерно"] += int(data["Зерно"] / 3)
        elif event1 == 4 and answer == "нет":
            pass
        results()
    else:
        pass

def main():
    user_name = input("Добро пожаловать в игру Kingdom Legends. Попробуй себя в роли настоящего Правителя! \n "
                      "Введите Ваш никнейм: ")
    if data["Год"] == 0:
        results()
    else:
        pass
    while data['Земля'] > 202 * 0.25 and data['Казна'] > 251 * 0.25 and data['Народ'] > 2000 * 0.25 and \
            data['Зерно'] > 0 and data['Смута'] < 10:
        seed = data['Зерно']
        price = randint(10, 30)
        question = input("Хотите ли вы продать зерно по цене " + str(price) +
                         "? Если да - введите 'да', если нет - 'нет':")
        if question == "да":
            tosell = int(input("Введите количетво зерна, которое вы хотите продать (в мешках):"))
            while data['Зерно'] - tosell < 0:
                tosell = int(input("Ми лорд, в нашей казне недостаточно средств. Введите количетво зерна,"
                                   " которое вы хотите продать (в мешках):"))
            selling(tosell, price)
            results()
        else:
            pass

        event()

        price1 = randint(25, 40)
        question1 = input("Хотите ли вы купить зерно по цене " + str(price1) +
                          "? Если да - введите 'да', если нет - 'нет':")
        if question1 == "да":
            tobay = int(input("Введите количетво зерна, которое вы хотите купить (в бушелях):"))
            while data['Казна'] - price * tobay < 0:
                tobay = int(input("Ми лорд, в нашей казне недостаточно средств."
                                  " Введите количетво зерна, которое вы хотите купить (в бушелях):"))
            buy(tobay, price1)
            results()
        else:
            pass

        event()

        zem = int(input("Введите сколько гектаров вы хотите отдать под засев:"))
        while data['Земля'] < zem:
            zem = int(input("У вас недостаточно земли. Введите сколько гектаров вы хотите отдать под засев: "))
        while data['Зерно'] < zem * 7:
            zem = int(input("У вас недостаточно зерна. Введите сколько гектаров вы хотите отдать под засев: "))
        zasef(zem)

        ed = int(input("Введите сколько зерна вы отдадите народу:"))
        while ed > data['Зерно']:
            ed = int(input("У вас недостаточно зерна. Введите сколько зерна вы отдадите народу:"))
        nar(ed)
        ura(zem)
        people(seed)
        data['Год'] = data['Год'] + 1
        results()
    print("GAME OVER!")
    with open("total_results.txt", "w") as total:
        print("Результаты игрока:{}".format(user_name), file=total)
        print("Земля:{}\nКазна: {}\nНарод: {}\nЗерно: {}\n Смута: {}\n Авторитет: {}\n Год: {}".format(data["Земля"],
                            data["Казна"], data["Народ"], data["Зерно"], data["Смута"],
                                                                        data["Авторитет"], data["Год"]), file=total)

