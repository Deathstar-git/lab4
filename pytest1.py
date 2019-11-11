from random import randint


def learn():
    i = randint(1, 12)
    dc = {1: "x^k dx = ?", 2: "dx/x = ?", 3: "a^x dx = ?", 4: "e^x dx = ?",
          5: "cosx dx = ?", 6: "sinx dx = ?", 7: "dx/cos^2x = ?", 8: "dx/sin^2x = ?",
          9: "dx/(x^2 + a^2) = ?", 10: "dx/sqrt(a^2 - x^2) = ?", 11: "dx/sqrt(x^2 - a) = ?",
          12: "dx/(x^2 - a^2) = ?"}
    print(dc[i])
    ans = input("Ответ:")
    if i == 1 and ans == "x^(k+1)/(k+1) + C":
        print("Nice)0)")
    elif i == 2 and ans == "ln|x| + C":
        print("Nice)0)")
    elif i == 3 and ans == "a^x/ln(a) + C":
        print("Nice)0)")
    elif i == 4 and ans == "e^x + C":
        print("Nice)0)")
    elif i == 5 and ans == "sin(x) + C":
        print("Nice)0)")
    elif i == 6 and ans == "-cos(x) + C":
        print("Nice)0)")
    elif i == 7 and ans == "tg(x) + C":
        print("Nice)0)")
    elif i == 8 and ans == "-ctg(x) + C":
        print("Nice)0)")
    elif i == 9 and ans == "1/a arctg x/a + C":
        print("Nice)0)")
    elif i == 10 and ans == "arcsin x/a + C":
        print("Nice)0)")
    elif i == 11 and ans == "ln|x + sqrt(x^2 + a)| + C":
        print("Nice)0)")
    elif i == 12 and ans == "1/2a ln|(x-a)/(x+a)| + C":
        print("Nice)0)")
    else:
        print("fiasko(9(")


learn()
