import sqlite3
from pojistenec import Pojistenec
from pojisteni import Pojisteni
from admin import Admin
connection = sqlite3.connect("databaze.db")


def prihlaseni():
    login = Admin(connection)

    overeni = login.prihlaseni()
    if overeni:
        menu()
    else:
        print("Přihlášení se nezdařilo")
        prihlaseni()


def menu():
    pojistenec = Pojistenec(connection)
    pojisteni = Pojisteni(connection)

    while True:
        vstup = input(f"---------------------------------\n"
                      f"Evidence pojištěných\n"
                      f"---------------------------------\n"
                      f"\n"
                      f"Vyberte si akci:\n"
                      f"1 - Přidat nového pojištěného\n"
                      f"2 - Vyhledat pojištěného\n"
                      f"3 - Upravit pojištěného\n"
                      f"4 - Přidat, upravit nebo odebrat pojištění\n"
                      f"5 - Smazat pojištěného a jeho pojištění\n"
                      f"6 - Vypsat všechny pojištěné\n"
                      f"7 - odhlášení\n"
                      f"8 - ukončení aplikace\n"
                      f"9 - Úprava administrátorů\n")
        if vstup == "1":
            pojistenec.vytvor()

        elif vstup == "2":
            jmeno = input("Zadejte křestní jméno pojištěnce: ")
            prijmeni = input("Zadejte příjmení pojištěnce: ")
            pojistenec = (pojistenec.vyhledej(jmeno, prijmeni))
            if pojistenec is not None:
                print(pojistenec)

        elif vstup == "3":
            pojistenec.uprav_pojistence()
            input("Stiskněte libovolnou klávesu pro pokračování")

        elif vstup == "4":
            """ pridani uprava a smazani pojisteni"""

            def vyber_pojistence():
                jmeno = input("Zadejte křestní jméno pojištěnce: ")
                prijmeni = input("Zadejte příjmení pojištěnce: ")

                def vyber_akce():

                    akce = input(f"---------------------------------\n"
                                 f"Přidání, úprava a smazání pojištění \n"
                                 f"Pojištěnce: {jmeno} {prijmeni}\n"
                                 f"---------------------------------\n"
                                 f"\n"                              
                                 f"Vyberte si akci:\n"
                                 f"1 - Přidat nové pojištění\n"
                                 f"2 - Upravit pojištění\n"
                                 f"3 - Smazat pojištění\n"
                                 f"4 - Vybrat jiného Pojištěnce\n"
                                 f"5 - Zpět do hlavního menu\n")
                    if akce == "1":
                        pojisteni.create(jmeno, prijmeni)
                        vyber_akce()
                    elif akce == "2":
                        pojisteni.update(jmeno, prijmeni)
                        vyber_akce()
                    elif akce == "3":
                        pojisteni.vymaz(jmeno, prijmeni)
                        vyber_akce()
                    elif akce == "4":
                        vyber_pojistence()
                    elif akce == "5":
                        menu()
                    else:
                        print("Zadali jste chybný znak.")
                        vyber_akce()

                vyber_akce()

            vyber_pojistence()

        elif vstup == "5":

            pojistenec.vymaz()

            input("Stiskněte libovolnou klávesu pro pokračování")

        elif vstup == "6":

            pojistenec.vypis_vsechny()

        elif vstup == "7":
            print("Odhlášení proběhlo úspěšně")
            prihlaseni()

        elif vstup == "8":
            print("Děkujeme za použití našich služeb.")
            break

        elif vstup == "9":
            login = Admin(connection)
            akce = input(f"---------------------------------\n"
                         f"Přidání, nebo smazání admina\n"
                         f"---------------------------------\n"
                         f"1 - Přidat nového admina\n"
                         f"2 - Smazat admina\n"
                         f"3 - Zpět do hlavního menu\n")

            if akce == "1":

                login.vytvor()
            elif akce == "2":

                login.vymaz()
            elif akce == "3":
                menu()
            else:
                print("Zadali jste chybný znak.")

        else:
            print("Neplatný vstup")
            input("Stiskněte libovolnou klávesu pro pokračování")


if __name__ == "__main__":
    prihlaseni()
