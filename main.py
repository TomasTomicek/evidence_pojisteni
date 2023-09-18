from akce import Akce
from evidence import Evidence
from help import Help

print("-" * 80)
print("Evidence pojištěných")
print("-" * 80)


evidence_instance = Evidence()  # Vytvoření instance třídy Evidence
help_instance = Help(evidence_instance)  # Vytvoření instance třídy Help a předání evidence_instance
akce_instance = Akce(evidence_instance)  # Předání instance evidence třídě Akce
akce_instance.spustit_menu()  # Spuštění menu
