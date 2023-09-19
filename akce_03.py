class EditorPojistence:
    def __init__(self, evidence_instance):
        self.evidence_instance = evidence_instance
    def editace(self):
        while True:
            input_id = input("Zadejte čtyřmístné ID číslo (nebo zadejte klávesu 'q' pro předešlou nabídku): ")
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
                            menu_EditorPojistence = input("Vyberte si akci (nebo zadejte klávesu 'q' pro předešlou nabídku):   ")
                            if menu_EditorPojistence == 'q':
                                return
                            if menu_EditorPojistence.isdigit() and len(menu_EditorPojistence) == 1:
                                menu_EditorPojistence = int(menu_EditorPojistence)
                                if menu_EditorPojistence == 1:
                                    osoba.status = False
                                elif menu_EditorPojistence == 2:
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
                "\n"
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
                        osoba.jmeno = osoba.jmeno.capitalize()  # Upraví první písmeno na velké, zbytek na malé
                    elif volba_editace == 2:
                        osoba.prijmeni = input("Zadejte nové příjmení: ")
                        osoba.prijmeni = osoba.prijmeni.capitalize()  # Upraví první písmeno na velké, zbytek na malé
                    elif volba_editace == 3:
                        osoba.predvolba = input("Zadejte novou předvolbu: ")
                    elif volba_editace == 4:
                        osoba.telNumber = input("Zadejte nové telefonní číslo: ")
                    elif volba_editace == 5:
                        osoba.vek = input("Zadejte nový věk: ")
                    print(self.evidence_instance.format_output(osoba))
                    print("\nÚdaj byl úspěšně změněn.")
                else:
                    print("Neplatná volba.")
            else:
                print("Neplatná volba.")