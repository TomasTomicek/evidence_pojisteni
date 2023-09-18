from help import Help
from akce_01 import Akce_01
from akce_02 import Akce_02
from akce_03 import Akce_03




class Akce:
    def __init__(self, evidence_instance):
        self.evidence_instance = evidence_instance
        self.akce_01_instance = Akce_01(self.evidence_instance)  # Vytvoření instance třídy Akce_01
        self.akce_02_instance = Akce_02(self.evidence_instance)  # Vytvoření instance třídy Akce_02
        self.akce_03_instance = Akce_03(self.evidence_instance)  # Vytvoření instance třídy Akce_03
    def spustit_menu(self):
        Help.naplneni_zakazniku(self)  # naplneni zakazniku z 'class Help' a 'def naplneni_zakazniku'
        while True:
            print("\nVyberte si akci:")
            print(
                "1 - Přidat nového pojistného\n"            #akce_01.py
                "2 - Filtr, výběr sestavy pojištěnců\n"     #akce_02.py
                "3 - Editovat, smazat pojištěnce\n"         #akce_03.py
                "\n"
                "q - Konec\n"
                "h - Help\n"
            )
            vyber_akce = input("Vyberte si akci:   ")
            print("-" * 80)
            if vyber_akce == 'h':
                Help.zobraz_napovedu()  # Spustíme statickou metodou zobraz_napovedu() ze souboru help.py
            elif vyber_akce == 'q':
                break  # Ukončení programu
            elif vyber_akce.isdigit():  # Ověřte, zda je vstup číslo.
                vyber_akce = int(vyber_akce)  # Převedeme vstup na celé číslo.

                if 1 <= vyber_akce <= 3:
                    if vyber_akce == 1:
                        self.akce_01_instance.pridani_pojistence()  # Volání metody z třídy Akce_01
                    elif vyber_akce == 2:
                        self.akce_02_instance.hledani_pojistence()  # Volání metody z třídy Akce_02
                    elif vyber_akce == 3:
                        self.akce_03_instance.editace()  # Volání metody z třídy Akce_03
                else:
                    print("Zadejte číslo v rozsahu 1-3.\n")
            else:
                print("Zadejte platné číslo.\n")





