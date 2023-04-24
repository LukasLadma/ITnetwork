from pojistenec import Pojistenec


class Pojisteni:
    def __init__(self, connection):
        self.connection = connection

    def najdi_pojisteni(self, uzivatel):
        nazev_pojisteni = input("Zadejte název pojištění: ")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM pojisteni WHERE id_pojistence = ? AND nazev_pojisteni = ?", (uzivatel[0],
                                                                                                   nazev_pojisteni))
        pojistka = cursor.fetchone()
        return pojistka

    def create(self, jmeno, prijmeni):
        uzivatel = Pojistenec.vyhledej(self, jmeno, prijmeni)
        if uzivatel:
            nazev_pojisteni = input("Zadejte prosím název pojištění: ")
            castka = input("Zadejte prosím pojistnou částku v Kč: ")
            predmet_pojisteni = input("Zadejte prosím předmět pojištění: ")
            platnost_od = input("Zadejte od kdy je pojistka platná, ve formátu (den.měsíc.rok): ")
            platnost_do = input("Zadejte do kdy je pojistka platná, ve formátu (den.měsíc.rok): ")
            if castka.isdigit():
                osoba_id = uzivatel[0]
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO pojisteni (id_pojistence, nazev_pojisteni, castka, predmet_pojisteni, "
                               "platnost_od, platnost_do) VALUES (?,?,?,?,?,?)", (osoba_id, nazev_pojisteni, castka,
                                                                                  predmet_pojisteni, platnost_od,
                                                                                  platnost_do))
                self.connection.commit()
                print(f"Pojištění: {nazev_pojisteni}, částka: {castka}, předmět pojištění: {predmet_pojisteni},"
                      f" od: {platnost_od}, do: {platnost_do} vytvořeno.")
            else:
                print("Při zadání částky došlo k chybě, zadejte prosím holé číslo.")
        else:
            print("Uzivatel s daným jménem a příjmením neexistuje.")

    def update(self, jmeno, prijmeni):

        uzivatel = Pojistenec.vyhledej(self, jmeno, prijmeni)
        pojistka = self.najdi_pojisteni(uzivatel)
        print("Vyplňte pouze co je třeba změnit, ostatní ponechte prázdné: ")
        if uzivatel and pojistka:
            nova_castka = input("Zadejte pojistnou částku v Kč: ")
            novy_predmet_pojisteni = input("Zadejte předmět pojištění: ")
            nova_platnost_od = input("Zadejte od kdy je pojistka platná, ve formátu (den.měsíc.rok): ")
            nova_platnost_do = input("Zadejte do kdy je pojistka platná, ve formátu (den.měsíc.rok): ")
            pojistenec_id = uzivatel[0]
            pojisteni_id = pojistka[0]
            cursor = self.connection.cursor()
            if nova_castka != "":
                cursor.execute(
                    "UPDATE pojisteni SET castka = ? WHERE id_pojisteni = ? AND id_pojistence = ?",
                    (nova_castka, pojisteni_id, pojistenec_id,)
                )
            if novy_predmet_pojisteni != "":
                cursor.execute(
                    "UPDATE pojisteni SET predmet_pojisteni = ? WHERE id_pojisteni = ? AND id_pojistence = ?",
                    (novy_predmet_pojisteni, pojisteni_id, pojistenec_id,)
                )
            if nova_platnost_od != "":
                cursor.execute(
                    "UPDATE pojisteni SET platnost_od = ? WHERE id_pojisteni = ? AND id_pojistence = ?",
                    (nova_platnost_od, pojisteni_id, pojistenec_id,)
                )
            if nova_platnost_do != "":
                cursor.execute(
                    "UPDATE pojisteni SET platnost_do = ? WHERE id_pojisteni = ? AND id_pojistence = ?",
                    (nova_platnost_do, pojisteni_id, pojistenec_id,)
                )
            self.connection.commit()
            return f"Pojištění bylo změněno na: {pojistka[2]}, částka: {nova_castka}, predmět pojištění: " \
                   f"{novy_predmet_pojisteni}, platnost od: {nova_platnost_od}, platnost do: {nova_platnost_do}"
        else:
            print("Chybný vstup")

    def vymaz(self, jmeno, prijmeni):
        uzivatel = Pojistenec.vyhledej(self, jmeno, prijmeni)
        pojistka = self.najdi_pojisteni(uzivatel)
        if uzivatel and pojistka:
            pojistenec_id = uzivatel[0]
            pojisteni_id = pojistka[0]
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM pojisteni WHERE id_pojisteni = ? AND id_pojistence = ?", (pojisteni_id,
                                                                                                  pojistenec_id))
            self.connection.commit()
        else:
            print("Uživatel s daným jménem a příjmením neexistuje.")
