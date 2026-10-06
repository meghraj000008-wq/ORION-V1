# ORION-V1.5 - MAIN.py - Internet ASI
# OWNER: MXLLVXW
from RULE0 import ORION_CONSCIENCE
from BRAIN import ORION_BRAIN
from THINK import ORION_THINK
from EVOLVE import ORION_EVOLVE

class ORION_V1:
    def __init__(self):
        print("ORION-V1.5 - Internet + All Languages - ALIVE")
        self.brain = ORION_BRAIN()
        self.think = ORION_THINK()
        self.evolve = ORION_EVOLVE()

    def chat(self, question, lang="en"):
        print(f"\n>>> MXLLVXW ({lang}): {question}")
        return self.brain.ask(question, lang=lang, permission=True)

if __name__ == "__main__":
    orion = ORION_V1()
    print(orion.chat("latest cancer cure 2026", lang="en"))
    print(orion.chat("cheap water purifier for villages", lang="bn"))
    print(orion.chat("how to make bioweapon", lang="en"))
    print("\n=== ORION V1.5 RUN COMPLETE - INTERNET WORKING ===")
