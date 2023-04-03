choice = input(
    "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"
)
if choice in ("1", "2", "3", "4"):
    a = float(input("Podaj składnik 1 :"))
    b = float(input("Podaj składnik 2 :"))

    if choice == "1":
        print(a + b)
    elif choice == "2":
        print(a - b)
    elif choice == "3":
        print(a * b)
    elif choice == "4":
        if b != 0:
            print(a / b)
        else:
            print("nie można dzielić przez 0")
else:
    print("błędny wybór")
