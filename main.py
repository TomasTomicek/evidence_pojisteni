from akce import HlavniMenu
from evidence import Evidence
from help import Help

print("-" * 80)
print("Evidence pojištěných")
print("-" * 80)
evidence_instance = Evidence()  # Vytvoření instance třídy Evidence
help_instance = Help(evidence_instance)  # Vytvoření instance třídy Help a předání evidence_instance
hlavnimenu_instance = HlavniMenu(evidence_instance)  # Předání instance evidence třídě Akce
hlavnimenu_instance.spustit_menu()  # Spuštění menu