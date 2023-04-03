import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


while True:
    choice = input(
        "Podaj działanie, posługując się odpowiednią liczbą: \n1 Dodawanie, \n2 Odejmowanie, \n3 Mnożenie, \n4 Dzielenie:\n"
    )
    if choice in ("1", "2", "3", "4"):
        try:
            a = float(input("Podaj składnik 1 :"))
            b = float(input("Podaj składnik 2 :"))
        except ValueError:
            logging.error("Błędne dane")
            break
        if choice == "1":
            logging.info("Dodaję %s i %s" % (a, b))
            print("Wynik to", a + b)
        elif choice == "2":
            logging.info("Odejmuję %s i %s" % (b, a))
            print("Wynik to", a - b)
        elif choice == "3":
            logging.info("Mnożę %s i %s" % (a, b))
            print("Wynik to", a * b)
        elif choice == "4":
            if b != 0:
                logging.info("Dzielę %s przez %s" % (a, b))
                print("Wynik to", a / b)
            else:
                logging.error("nie można dzielić przez 0")
    else:
        logging.error("Błędny wybór")
