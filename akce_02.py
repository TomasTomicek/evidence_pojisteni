from evidence import Evidence

class Akce_02:  # reakce na funkci 'spustit_menu' ze souboru akce.py ...  2 - Vypsat všechny pojištěné

    def __init__(self, evidence_instance):
        self.evidence_instance = evidence_instance

    def vypsat_pojistence(self, status_filter=True):
        for osoba in self.evidence_instance.evidence_pojistencu:
            if osoba.status == status_filter:
                print(self.evidence_instance.format_output(osoba))


    def hledani_pojistence(self):
        while True:
            print(
                "Vyber si číslo/parametr, podle kterého budeš hledat:\n"
                "0 - Vypsát všechny pojíštěné\n"
                "1 - Vypsát všechny smazané pojíštěné\n"
                "2 - Jméno\n"
                "3 - Příjmení\n"
                "4 - Předvolba\n"
                "5 - Telefonní číslo\n"
                "6 - Věk\n"
            )
            volba = input("Zde napiš výběr:    ")

            if volba == 'q':
                return
            elif volba.isdigit():                # Zpracujte další výběr podle uživatelova vstupu.
                volba_akce = int(volba)  # Převedeme vstup na celé číslo.
                if 0 <= volba_akce <= 6:
                    if volba_akce == 0:
                        self.vypsat_pojistence()
                    elif volba_akce == 1:
                        self.vypsat_pojistence(False)
                    elif 2 <= volba_akce <= 6:
                        filtr = input(
                            "Zadej filtr: ").lower()  # Převedeme filtr na malá písmena pro nesensitive porovnání
                        nalezeni = []

                        for osoba in self.evidence_instance.evidence_pojistencu:
                            if volba_akce == 2 and filtr in osoba.jmeno.lower():
                                nalezeni.append(osoba)
                            elif volba_akce == 3 and filtr in osoba.prijmeni.lower():
                                nalezeni.append(osoba)
                            elif volba_akce == 4 and filtr in osoba.predvolba:
                                nalezeni.append(osoba)
                            elif volba_akce == 5 and filtr in osoba.telNumber:
                                nalezeni.append(osoba)
                            elif volba_akce == 6 and filtr in osoba.vek:
                                nalezeni.append(osoba)

                        if nalezeni:
                            print("\nVýsledky vyhledávání:")
                            print(self.evidence_instance.format_header)  # Tiskneme hlavičku a oddělovací čáru
                            for osoba in nalezeni:
                                print(self.evidence_instance.format_output(osoba))
                            print(self.evidence_instance.format_header)  # Tiskneme oddělovací čáru na konci
                        else:
                            print("\nNenalezeno žádné odpovídající záznamy.")
                    break
                else:
                    print("Zadejte číslo v rozsahu 0-5.")
            else:
                print("Zadejte platné číslo.")