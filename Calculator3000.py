class Calc:
    @staticmethod
    def choose_move(ch1,ch2):
        print("-----Выбор действия-----")
        list_move = ["/","*","+","-","**"]
        for el in list_move:
            print(el)
        move = input("выберите действие:")

        res = 0
        for _ in list_move:
            if move == "/":
                res = ch1 / ch2
            elif move == "*":
                res = ch1*ch2
            else:
                print("такого варианта нет")

        print("result is",res)
        return res



ch1 = int(input("введите число 1:"))
ch2 = int(input("введите число 2:"))
Calc.choose_move(ch1,ch2)

