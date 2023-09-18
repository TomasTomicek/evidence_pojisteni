import re  # Modul pro regulární výrazy
from evidence import Evidence
# reakce na funkci 'spustit_menu' ze souboru akce.py ...  1 - Přidat nového pojistného
class Akce_01:
    def __init__(self, evidence_instance):
        self.evidence_instance = evidence_instance
 #       self.current_ident_number = 1000  # Počáteční hodnota ident_number ... smazat a poresit, prenest do evidence.py
    def pridani_pojistence(self):
        while True:
            while True:
                jmeno = input("Zadejte jméno pojistného: ").lower()
                if jmeno == 'q':
                    return
                elif re.match(r'^[a-zá-ž]+$', jmeno):
                    break
                else:
                    print("Neplatný formát jména. Zadejte pouze písmena.")

            while True:
                prijmeni = input("Zadejte příjmení: ").lower()
                if re.match(r'^[a-zá-ž]+$', prijmeni):
                    break
                else:
                    print("Neplatný formát příjmení. Zadejte pouze písmena.")
            while True:
                predvolba = input("Zadejte předvolbu státu včetně znaku +: ")
                predvolba = predvolba.replace('+', '')  # Odstranění znaku "+" (křížku) ze vstupu
                if re.match(r'^\d{2,3}$', predvolba):  # testování 'predvolby' na počet 2-3 znaku
                    break
                else:
                    print("Neplatný formát předvolby. Zadejte znovu.")
            telNumber = input("Zadejte telefonní číslo: ")
            vek = input("Zadejte věk: ")
            print("-" * 80)
            ident_number = str(self.evidence_instance.current_ident_number)  # Použití aktuálního ident_number
            nova_osoba = Evidence(jmeno, prijmeni, predvolba, telNumber, vek, ident_number)
            self.evidence_instance.evidence_pojistencu.append(nova_osoba)
            self.evidence_instance.current_ident_number += 1  # Zvýšení aktuálního ident_number pro další záznam
            return False  # Ukončíme program.
