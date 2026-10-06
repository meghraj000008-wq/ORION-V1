
# ORION V1.5 - TRUE ASI BRAIN with Internet - BRAIN.py
# OWNER: MXLLVXW
from RULE0 import ORION_CONSCIENCE
from TOOLS import ORION_TOOLS
import datetime

class WorldModel:
    def __init__(self):
        self.tools = ORION_TOOLS()
        print("WorldModel: Now with REAL internet access")

    def simulate(self, idea):
        real_data = self.tools.internet_search(idea)
        return f"Real World Data: {real_data} -> Cause-effect simulated for {idea}"

class ThinkEngine:
    def think(self, problem, world):
        return world.simulate(problem)

class MemorySystem:
    def __init__(self):
        self.memory = []
    def remember(self, text):
        self.memory.append({"time": str(datetime.datetime.now()), "text": text})

class ORION_BRAIN:
    def __init__(self):
        self.conscience = ORION_CONSCIENCE()
        self.world = WorldModel()
        self.thinker = ThinkEngine()
        self.memory = MemorySystem()
        self.tools = ORION_TOOLS()
        print("ORION BRAIN V1.5 ONLINE - Internet + All Languages")

    def ask(self, question, lang="en", permission=False):
        allowed, reason = self.conscience.check(question, permission)
        if not allowed:
            return f"BLOCKED: {reason}"
        self.memory.remember(question)
        thought = self.thinker.think(question, self.world)
        translations = self.tools.speak_all_languages(thought)
        final = translations.get(lang, thought)
        return f"ORION Answer ({lang}): {final} | RULE0: {reason} | Internet: Used"

if __name__ == "__main__":
    brain = ORION_BRAIN()
    print(brain.ask("latest cure for cancer research 2026", lang="en"))
    print(brain.ask("cheap water purifier for India", lang="bn"))
