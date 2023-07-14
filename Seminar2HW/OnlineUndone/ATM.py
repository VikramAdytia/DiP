userinfo = {
    "money": 0,
    "oper_count": 0
}

while True:
    menu_choise = input("""Пожалуйста, введите номер выбора, который вы хотите сделать   
         1 пополнить
         2 снять
         3 выйти
     Пожалуйста, введите ваш выбор :  """)
    user_money = userinfo["money"]
    user_oper_count = userinfo["oper_count"]
    match menu_choise:
        case "1":
            if userinfo["money"] > 5000000:
                user_money = user_money - (user_money * 0.1)
            value_str = input("Сумма пополнения и снятия кратны 50 у.е : ")
            try:
                value = int(value_str)
            except ValueError:
                print("Please, type a valid integer number!")
                continue
            if value < 1:
                print("Please type a strictly positive number!")
                continue
            elif value % 50 != 0:
                print("Please type a strictly кратны 50 у.е number!")
                continue
            else:
                user_money += value
            if user_oper_count > 3:
                user_money *= 1.03  # "начисляются проценты" интерпретировал как бонус, а не списывание
            userinfo["money"] = user_money
            userinfo["oper_count"] = user_oper_count + 1
            print(user_money)
        case "2":

            if user_money > 5000000:
                user_money = user_money - (user_money * 0.1)

            value_str = input("Сумма пополнения и снятия кратны 50 у.е : ")
            try:
                value = int(value_str)
            except ValueError:
                print("Please, type a valid integer number!")
                continue
            if value < 1:
                print("Please type a strictly positive number!")
                continue
            elif value % 50 != 0:
                print("Please type a strictly кратны 50 у.е number!")
                continue
            elif value > user_money != 0 :
                print("Нельзя снять больше, чем на счёте!")
                continue
            elif user_money == 0 :
                print("на счёте 0")
                continue
            else:
                user_money -= value

            withdrawl_persent = user_money - (user_money * 0.985)
            if withdrawl_persent < 30:
                withdrawl_persent = 30
            if withdrawl_persent > 600:
                withdrawl_persent = 600
            user_money = user_money - withdrawl_persent

            if user_oper_count > 3:
                user_money *= 1.03

            userinfo["money"] = user_money
            userinfo["oper_count"] = user_oper_count + 1
            print(user_money)
        case "3":
            print(user_money)
            break
