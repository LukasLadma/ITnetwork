class Admin:

    def __init__(self, connection):
        self.connection = connection

    def prihlaseni(self):
        print("Přihlášení administrátora")
        uzivatelske_jmeno = input("Zadejte uživatelské jméno administrátora: (lenovo)")
        heslo = input("Zadejte heslo: (legion)")

        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM admini WHERE uzivatelske_jmeno = ? AND heslo = ?", (uzivatelske_jmeno, heslo)
        )
        uzivatel = cursor.fetchone()
        return uzivatel

    def vytvor(self):
        print("Vytváříte nového administrátora")
        uzivatelske_jmeno = input("Zadejte uživatelské jméno: ")
        heslo = input("Zadejte heslo: ")
        email = input("Zadejte email: ")
        telefon = input("Zadejte telefoní číslo: ")
        if uzivatelske_jmeno != "" and heslo != "" and email != "" and telefon != "":
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO admini (uzivatelske_jmeno, heslo, email, telefon) VALUES (?, ?, ?, ?)",
                (uzivatelske_jmeno, heslo, email, telefon),
            )
            self.connection.commit()
            print(f"Admin    {uzivatelske_jmeno}    {heslo}   {email}    {telefon}"
                  f" byl vytvořen.")
        else:
            print("Chybně jste zadali některý z údajů.")

    def vymaz(self):
        print("Smazání administrátora")
        uzivatelske_jmeno = input("Zadejte uživatelské jméno: ")
        heslo = input("Zadejte heslo: ")
        if uzivatelske_jmeno != "" and heslo != "":
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM admini  WHERE uzivatelske_jmeno = ? AND heslo = ?", (uzivatelske_jmeno,
                                                                                               heslo))
            admin = cursor.fetchone()
            print(f"Admin {admin[1]} s heslem {admin[2]}, byl smazán")
            cursor.execute("DELETE FROM admini WHERE uzivatelske_jmeno = ? AND heslo = ?", (uzivatelske_jmeno, heslo))
            self.connection.commit()
        else:
            print("Chubně zadané uživatelské jméno nebo heslo.")
