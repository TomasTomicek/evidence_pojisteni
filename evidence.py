class Evidence:

    def __init__(self, jmeno=None, prijmeni=None, predvolba=None, telNumber=None, vek=None, ident_number=None, status=True, evidence_pojistencu=None):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.predvolba = predvolba
        self.telNumber = telNumber
        self.vek = vek
        self.ident_number = ident_number
        self.status = status
        self.evidence_pojistencu = evidence_pojistencu or []
        self.current_ident_number = 1000  # Počáteční hodnota ident_number --> pridano

    @staticmethod
    def format_header():
        separator = "-" * 80
        header = "{:<15} {:<15} {:<15} {:<15} {:<15}".format('ID číslo', 'Jméno', 'Příjmení', 'Tel. číslo', 'Věk')
        return f"{separator}\n{header}\n{separator}"
    def format_output(self, osoba):
        formatted_data = "{:<15} {:<15} {:<15} {:<15} {:<15}".format(
            osoba.ident_number, osoba.jmeno, osoba.prijmeni, "+{}".format(osoba.predvolba) + osoba.telNumber, osoba.vek,
        )
        return formatted_data

