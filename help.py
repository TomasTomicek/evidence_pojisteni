from evidence import Evidence

class Help:
    def __init__(self, evidence_instance):
        self.evidence_instance = evidence_instance
 #       self.current_ident_number = 1000  # Počáteční hodnota ident_number
        self.vymysleni_pojistenci = []  # Seznam pro dočasné ukládání vytvořených zákazníků

    @staticmethod
    def zobraz_napovedu():
        print("-" * 36 + "  Help  " + "-" * 36)
        print("Vítejte v nápovědě k programu:\n")
        print("{:<10}{:<15}{:<60}".format("", "q", "při použití tohoto znaků vyjedete z nabídky bez jejího uložení"))
        print("-" * 36 + "  Help  " + "-" * 36)

    def naplneni_zakazniku(self):
        self.vymysleni_pojistenci = [
            ["Alice", "Nováková", "420", "606354256", "30", "1000", True],
            ["Bob", "Smith", "421", "606123456", "35", "1001", True],
            ["Charlie", "Brown", "422", "606789012", "40", "1002", False],
            ["Dav", "Johnson", "423", "606987654", "25", "1003", True],
            ["Eva", "Garcia", "424", "606111222", "28", "1004", True],
            ["Frank", "Lee", "425", "606333444", "45", "1005", True],
            ["Grace", "Martinez", "426", "606555666", "33", "1006", False],
            ["Henry", "Lopez", "427", "606777888", "38", "1007", True],
            ["Isabella", "Davis", "428", "606999000", "27", "1008", True],
            ["Jack", "Miller", "429", "606000111", "31", "1009", True]
        ]
        for osoba in self.vymysleni_pojistenci:
            ident_number = str(self.evidence_instance.current_ident_number)  # Použití aktuálního ident_number
            jmeno, prijmeni, predvolba, telNumber, vek, ident_number, status = osoba
            nova_osoba = Evidence(jmeno, prijmeni, predvolba, telNumber, vek, ident_number, status)
            self.evidence_instance.evidence_pojistencu.append(nova_osoba)
            self.evidence_instance.current_ident_number += 1