class Pojistenec:

    def __init__(self, connection):
        self.connection = connection

    def vytvor(self):
        jmeno = input("Zadejte křestní jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        email = input("Zadejte email: ")
        telefon = input("Zadejte telefoní číslo: ")
        ulice_a_cislo_popisne = input("Zadejte ulici a číslo popisné: ")
        mesto = input("Zadejte město: ")
        psc = input("Zadejte PSČ: ")

        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO pojistenci (jmeno, prijmeni, email, telefon, ulice_a_cislo_popisne, mesto, psc) VALUES (?, "
            "?, ?, ?, ?, ?, ?)",
            (jmeno, prijmeni, email, telefon, ulice_a_cislo_popisne, mesto, psc),
        )
        self.connection.commit()
        print(f"Uživatel    {jmeno}    {prijmeni}   {email}    {telefon}   {ulice_a_cislo_popisne}    {mesto}    {psc}"
              f" byl vytvořen.")

    def vyhledej(self, jmeno, prijmeni):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM pojistenci WHERE jmeno = ? AND prijmeni = ?", (jmeno, prijmeni))
        uzivatel = cursor.fetchone()
        if uzivatel:
            return uzivatel

        else:
            print("Uzivatel nenalezen")
            input("Stiskněte libovolnou klávesu pro pokračování")

    def vypis_vsechny(self):
        print("Všichni pojištěnci:")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM pojistenci;")
        radky = cursor.fetchall()

        for radek in radky:
            print(radek)
        self.connection.commit()

    def uprav_pojistence(self):

        print("Stačí zadat ID nebo jméno a příjmení")
        jmeno = input("Zadejte křestní jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        print("Vyplňte pouze co je třeba změnit, ostatní ponechte prázdné: ")
        nove_jmeno = input("Zadejte nové jméno: ")
        nove_prijmeni = input("Zadejte nové příjmení: ")
        novy_email = input("Zadejte nový email: ")
        novy_telefon = input("Zadejte nové telefoní číslo: ")
        nova_ulice_a_cislo_popisne = input("Zadejte novou ulici a číslo popisné: ")
        nove_mesto = input("Zadejte nové město: ")
        nove_psc = input("Zadejte nové PSČ: ")

        cursor = self.connection.cursor()
        if jmeno != "" and prijmeni != "":
            if nove_jmeno != "":
                cursor.execute(
                    "UPDATE pojistenci SET jmeno = ? WHERE jmeno = ? AND prijmeni = ?",
                    (nove_jmeno, jmeno, prijmeni)
                )
            if nove_prijmeni != "":
                cursor.execute(
                    "UPDATE pojistenci SET prijmeni = ? WHERE jmeno = ? AND prijmeni = ?",
                    (nove_prijmeni, jmeno, prijmeni)
                )
            if novy_email != "":
                cursor.execute(
                    "UPDATE pojistenci SET email = ? WHERE jmeno = ? AND prijmeni = ?",
                    (novy_email, jmeno, prijmeni)
                )
            if novy_telefon != "":
                cursor.execute(
                    "UPDATE pojistenci SET telefon = ? WHERE jmeno = ? AND prijmeni = ?",
                    (novy_telefon, jmeno, prijmeni)
                )
            if nova_ulice_a_cislo_popisne != "":
                cursor.execute(
                    "UPDATE pojistenci SET elice_a_cislo_popisne = ? WHERE jmeno = ?"
                    " AND prijmeni = ?", (nova_ulice_a_cislo_popisne, jmeno, prijmeni)
                )
            if nove_mesto != "":
                cursor.execute(
                    "UPDATE pojistenci SET mesto = ? WHERE jmeno = ? AND prijmeni = ?",
                    (nove_mesto, jmeno, prijmeni)
                )
            if nove_psc != "":
                cursor.execute(
                    "UPDATE pojistenci SET psc = ? WHERE jmeno = ? AND prijmeni = ?",
                    (nove_psc, jmeno, prijmeni)
                )
       #### TADY JE POTREBA NAPSAT NA CO BYL UZIVATEL UPRAVEN

        else:
            print("Špatně jste zadali ID nebo jméno a příjmení")
            return
        self.connection.commit()

    def vymaz(self):
        jmeno = input("Zadejte křestní jméno pojištěnce: ")
        prijmeni = input("Zadejte příjmení pojištěnce: ")
        uzivatel = Pojistenec.vyhledej(self, jmeno, prijmeni)
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM pojistenci WHERE id_pojistenci = ?", (uzivatel[0],))
            cursor.execute("DELETE FROM POJISTENI WHERE id_pojistence = ?", (uzivatel[0],))
        self.connection.commit()
