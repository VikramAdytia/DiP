def atm():
    userinfo = {
        "money": 0,
        "oper_count": 0
    }

    def print_money():
        print(user_money)

    def withdrawl_draw():
        global user_money
        withdrawl_persent = user_money * 0.015
        if withdrawl_persent < 30:
            withdrawl_persent = 30
        if withdrawl_persent > 600:
            withdrawl_persent = 600
        user_money = user_money - withdrawl_persent

    def withdrawl_check(value_str):
        try:
            value = int(value_str)
        except ValueError:
            print("Please, type a valid integer number!")
            return False
        if value < 1:
            print("Please type a strictly positive number!")
            return False
        elif value % 50 != 0:
            print("Please type a strictly кратны 50 у.е number!")
            return False
        elif value > user_money:
            print("Нельзя снять больше, чем на счёте!")
            return False
        else:
            return True

    def deposit(value_str):
        try:
            value = int(value_str)
        except ValueError:
            print("Please, type a valid integer number!")
            return False
        if value < 1:
            print("Please type a strictly positive number!")
            return False
        elif value % 50 != 0:
            print("Please type a strictly кратны 50 у.е number!")
            return False
        else:
            return True

    def three_opeartion_bonus(user_oper_count):
        global user_money
        if user_oper_count > 3:
            user_money *= 1.03

    def wealth_tax():
        global user_money
        if user_money > 5000000:
            user_money = user_money * 0.9

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
                wealth_tax()

                value_str = input("Сумма пополнения и снятия кратны 50 у.е : ")
                if deposit(value_str):
                    user_money += int(value_str)

                three_opeartion_bonus(user_oper_count)

                userinfo["money"] = user_money

                userinfo["oper_count"] = user_oper_count + 1
                print_money()

            case "2":

                wealth_tax()
                value_str = input("Сумма пополнения и снятия кратны 50 у.е : ")
                if withdrawl_check(value_str):
                    withdrawl_draw()
                    three_opeartion_bonus(user_oper_count)
                    user_money = user_money - int(value_str)

                userinfo["money"] = user_money
                userinfo["oper_count"] = user_oper_count + 1
                print_money()
            case "3":
                print_money()
                break


atm()
