from akce import HlavniMenu
from evidence import Evidence
from help import Help

print("-" * 80)
print("Evidence pojištěných")
print("-" * 80)
evidence_instance = Evidence()  # Vytvoření instance evidence
help_instance = Help(evidence_instance)  # Vytvoření instance nápovědy a předání evidence_instance
hlavnimenu_instance = HlavniMenu(evidence_instance)  # Vytvoření instance hlavního menu a předání evidence_instance
hlavnimenu_instance.spustit_menu()  # Spuštění hlavního menu