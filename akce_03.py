class Akce_03:
    def __init__(self, evidence_instance):
        self.evidence_instance = evidence_instance

    def editace(self):
        while True:
            input_id = input("Zadejte ID číslo (počínaje od 1000): ")
            if input_id == 'q':
                return
            elif input_id.isdigit() and len(input_id) == 4 and int(input_id) >= 1000:
                for osoba in self.evidence_instance.evidence_pojistencu:
                    if input_id in osoba.ident_number:
                        if osoba.status == True:
                            print(self.evidence_instance.format_output(osoba))
                            print("\nVyberte si akci:")
                            print(
                                "1 - Smazat pojistného\n"
                                "2 - Editovat pojistného\n"
                            )
                            vyber_akce = input("Vyberte si akci:   ")
                            if vyber_akce.isdigit() and len(vyber_akce) == 1:
                                vyber_akce = int(vyber_akce)
                                if vyber_akce == 1:
                                    osoba.status = False
                                elif vyber_akce == 2:
                                    self.editovat_pojistneho(osoba)
                                else:
                                    print("Neplatná volba.")
                            else:
                                print("Neplatná volba.")
                        else:
                            print("\nTento klient má status 'False' a nelze na něj provádět akce.")
                        break
                else:
                    print("\nNenalezeny žádné odpovídající záznamy.")
            else:
                print("Neplatný vstup. Zadejte platné ID číslo (počínaje od 1000).")

    def editovat_pojistneho(self, osoba):
        while True:
            print("\nEditace pojistného (nezmění se ID číslo):")
            print(
                "1 - Změnit jméno\n"
                "2 - Změnit příjmení\n"
                "3 - Změnit předvolbu\n"
                "4 - Změnit telefonní číslo\n"
                "5 - Změnit věk\n"
                "q - Konec\n"
            )
            volba_editace = input("Vyberte si akci pro editaci:   ")
            if volba_editace == 'q':
                break
            elif volba_editace.isdigit() and len(volba_editace) == 1:
                volba_editace = int(volba_editace)
                if 1 <= volba_editace <= 5:
                    if volba_editace == 1:
                        osoba.jmeno = input("Zadejte nové jméno: ")
                    elif volba_editace == 2:
                        osoba.prijmeni = input("Zadejte nové příjmení: ")
                    elif volba_editace == 3:
                        osoba.predvolba = input("Zadejte novou předvolbu: ")
                    elif volba_editace == 4:
                        osoba.telNumber = input("Zadejte nové telefonní číslo: ")
                    elif volba_editace == 5:
                        osoba.vek = input("Zadejte nový věk: ")
                    print("\nÚdaj byl úspěšně změněn.")
                else:
                    print("Neplatná volba.")
            else:
                print("Neplatná volba.")