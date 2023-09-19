from help import Help
from akce_01 import NovyPojistenec
from akce_02 import FiltrPojistence
from akce_03 import EditorPojistence

class HlavniMenu:
    """
    Třída představující hlavní menu systému pojišťovnictví.

    Atributy:
        evidence_instance (Evidence): Instance třídy Evidence pro evidenci pojištěných osob.
        NovyPojistenec (NovyPojistenec): Instance třídy NovyPojistenec pro přidávání nových pojištěnců.
        FiltrPojistence (FiltrPojistence): Instance třídy FiltrPojistence pro filtrování pojištěnců.
        EditorPojistence (EditorPojistence): Instance třídy EditorPojistence pro úpravu pojištěnců.
    """

    def __init__(self, evidence_instance):
        """
        Inicializuje novou instanci třídy HlavniMenu.

        Args:
            evidence_instance (Evidence): Instance třídy Evidence pro evidenci pojištěných osob.
        """
        self.evidence_instance = evidence_instance
        self.NovyPojistenec = NovyPojistenec(self.evidence_instance)  # Vytvoření instance třídy NovyPojistenec
        self.FiltrPojistence = FiltrPojistence(self.evidence_instance)  # Vytvoření instance třídy FiltrPojistence
        self.EditorPojistence = EditorPojistence(self.evidence_instance)  # Vytvoření instance třídy EditorPojistence

    def spustit_menu(self):
        """
        Spouští hlavní menu systému pojišťovnictví.
        """
        Help.naplneni_zakazniku(self)  # Naplnění zákazníků z 'class Help' a 'def naplneni_zakazniku'
        while True:
            print("\nVyberte si akci:")
            print(
                "1 - Přidat nového pojistného\n"            # Volba pro přidání nového pojištěnce
                "2 - Filtr, výběr sestavy pojištěnců\n"     # Volba pro filtrování a výběr sestavy pojištěnců
                "3 - Editovat, smazat pojištěnce\n"         # Volba pro úpravu nebo smazání pojištěnce
                "\n"
                "q - Konec\n"
                "h - Help\n"
            )
            vyber_akce = input("Vyberte si akci:   ")
            print("-" * 80)
            if vyber_akce == 'h':
                Help.zobraz_napovedu()  # Spuštění zobraz_napovedu() ze třídy Help
            elif vyber_akce == 'q':
                break  # Ukončení programu
            elif vyber_akce.isdigit():  # Ověřte, zda je vstup číslo.
                vyber_akce = int(vyber_akce)  # Převedeme vstup na celé číslo.
                if 1 <= vyber_akce <= 3:
                    if vyber_akce == 1:
                        self.NovyPojistenec.pridani_pojistence()  # Volání metody pro přidání nového pojištěnce
                    elif vyber_akce == 2:
                        self.FiltrPojistence.hledani_pojistence()  # Volání metody pro filtrování pojištěnců
                    elif vyber_akce == 3:
                        self.EditorPojistence.editace()  # Volání metody pro úpravu pojištěnců
                else:
                    print("Zadejte číslo v rozsahu 1-3.\n")
            else:
                print("Zadejte platné číslo.\n")