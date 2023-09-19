import re  # Modul pro regulární výrazy
from evidence import Evidence

class NovyPojistenec:
    """
    Třída představující reakci na funkci 'spustit_menu' ze souboru hlavnimenu.py pro přidání nového pojistného.

    Atributy:
        evidence_instance (Evidence): Instance třídy Evidence pro evidenci pojištěných osob.
    """
    def __init__(self, evidence_instance):
        """
        Inicializuje novou instanci třídy NovyPojistenec.

        Args:
            evidence_instance (Evidence): Instance třídy Evidence pro evidenci pojištěných osob.
        """
        self.evidence_instance = evidence_instance

    def pridani_pojistence(self):
        """
        Metoda pro přidání nového pojistného do evidence.

        Returns:
            bool: False pro ukončení programu.
        """
        while True:
            while True:
                jmeno = input("Zadejte jméno pojistného (nebo zadejte klávesu 'q' pro předešlou nabídku): ").lower()
                if jmeno == 'q':
                    return False
                elif re.match(r'^[a-zá-ž]+$', jmeno):
                    jmeno = jmeno.capitalize()  # Upraví první písmeno na velké, zbytek na malé
                    break
                else:
                    print("Neplatný formát jména. Zadejte pouze písmena.")

            while True:
                prijmeni = input("Zadejte příjmení: ").lower()
                if re.match(r'^[a-zá-ž]+$', prijmeni):
                    prijmeni = prijmeni.capitalize()  # Upraví první písmeno na velké, zbytek na malé
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

            while True:
                telNumber = input("Zadejte telefonní číslo: ")
                if re.match(r'^\d{7,10}$', telNumber):  # testování 'telNumber' na počet 7-10 znaku
                    break
                else:
                    print("Neplatný formát telefonního čísla. Zadejte znovu, max. počet číselných znaků 7-10.")

            while True:
                vek = input("Zadejte věk: ")
                if re.match(r'^\d{1,3}$', vek):  # testování 'vek' na počet 1-3 znaku
                    break
                else:
                    print("Neplatný formát pro věk. Zadejte znovu, max. počet číselných znaků 1-3.")

            print("-" * 80)
            ident_number = str(self.evidence_instance.current_ident_number)  # Použití aktuálního ident_number
            novy_pojisteny = Evidence(jmeno, prijmeni, predvolba, telNumber, vek, ident_number)
            self.evidence_instance.evidence_pojistencu.append(novy_pojisteny)  # Zapiseme nového pojistence do seznamu 'evidence_pojistencu' v souboru evidence.py
            print(self.evidence_instance.format_output(novy_pojisteny))  # Vypiseme na obrazovku přidaného nového pojistného
            self.evidence_instance.current_ident_number += 1  # Zvýšení aktuálního ident_number pro další záznam
            return False  # Ukončíme program.