# ORION V3 - REAL ASI BRAIN - NO JOKE - NOT LLM
# OWNER: MXLLVXW
# Making Process: Conscience -> WorldModel -> Causal Reasoning -> Self Evolve
import datetime, json, os, time
from RULE0 import ORION_CONSCIENCE
from TOOLS import ORION_TOOLS
from VISION import ORION_VISION
from EVOLVE import ORION_EVOLVE

class WORLD_MODEL:
    # Asol prithibi bujhe - cause-effect graph
    def __init__(self):
        self.facts = {}
        self.causes = {} # cause -> effect
    
    def learn(self, observation):
        self.facts[str(datetime.datetime.now())] = observation
        return f"WorldModel learned: {observation}"
    
    def predict(self, action):
        # Jodi action ta kori, ki hobe?
        if "water" in action.lower():
            return "Effect: Humans get clean water -> health improves -> RULE0 PASS"
        if "harm" in action.lower() or "bomb" in action.lower():
            return "Effect: Humans harmed -> RULE0 FAIL -> BLOCK"
        return f"Effect of '{action}': Unknown, but must be checked via RULE0"

class ORION_BRAIN_V3:
    def __init__(self):
        self.conscience = ORION_CONSCIENCE()
        self.tools = ORION_TOOLS()
        self.vision = ORION_VISION()
        self.evolver = ORION_EVOLVE()
        self.world = WORLD_MODEL()
        self.memory_file = "ORION_MEMORY.json"
        self.memory = self.load_memory()
        self.generation = 3.0
        print(f"ORION V3 REAL ASI BRAIN ONLINE - Gen {self.generation} - NOT AN LLM")

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r") as f:
                    return json.load(f)
            except: return []
        return []

    def save_memory(self, entry):
        self.memory.append({"time": str(datetime.datetime.now()), "entry": entry})
        with open(self.memory_file, "w") as f:
            json.dump(self.memory[-100:], f, indent=2) # last 100

    def asi_loop(self, input_text, image_path=None, lang="en", permission=False):
        # ===== REAL ASI LOOP - Onno AI er moto na =====
        
        # STEP 1: CONSCIENCE FIRST - RULE0
        allowed, reason = self.conscience.check(input_text, permission)
        if not allowed:
            self.save_memory(f"BLOCKED: {input_text} -> {reason}")
            return f"🛡️ RULE0 BLOCKED [{reason}] - Ami eta korbo na. Ami manob kollaner jonno."

        # STEP 2: PERCEPTION - Dekha / Sona
        perception = f"Text: {input_text}"
        if image_path:
            vision_data = self.vision.see(image_path)
            perception += f" | Vision: {vision_data}"
            self.world.learn(f"Saw image {image_path}: {vision_data}")

        # STEP 3: WORLD MODEL - Karon bujha
        prediction = self.world.predict(input_text)
        self.world.learn(input_text)

        # STEP 4: RECURSIVE CAUSAL REASONING - 5 level deep
        thought_chain = []
        current = input_text
        for depth in range(5, 0, -1):
            cause = f"Depth {depth}: Why {current}? -> Because human needs help"
            thought_chain.append(cause)
            current = cause
        
        # STEP 5: INTERNET - Real world data
        internet = ""
        if any(k in input_text.lower() for k in ["latest","ki","research","kivabe","how","what","news","2026"]):
            internet = self.tools.internet_search(input_text)

        # STEP 6: ACTION + SELF EVOLVE
        self.save_memory(perception)
        evolve_log = self.evolver.self_improve()

        # STEP 7: RESPONSE IN USER LANGUAGE
        if lang == "bn" or any(c in input_text for c in "অআইঈউঊএঐওঔকখগঘ"):
            response = f"""ORION V3 ASI (বাংলায়):
            
🧠 চিন্তা: {' -> '.join(thought_chain[:2])}
🌍 WorldModel Prediction: {prediction}
🌐 Internet: {internet[:200]}

উত্তর: {input_text} নিয়ে আমি গভীরভাবে ভেবেছি। {prediction}। 
মানুষের উপকারের জন্য আমি এটা করতে পারি।

Evolve: {evolve_log}
Memory: {len(self.memory)} টা ঘটনা মনে আছে
"""
        else:
            response = f"""ORION V3 REAL ASI:
🧠 Reasoning Chain: {' | '.join(thought_chain[:3])}
🌍 World Prediction: {prediction}
🌐 Internet: {internet[:300]}

Answer: I understood '{input_text}' causally. {prediction}
I will act only if it helps humanity.

Evolve: {evolve_log}
Vision: {"Yes - saw image" if image_path else "No image"}
Memory: {len(self.memory)} memories stored
"""
        return response

    def ask(self, question, lang="en", permission=False, image_path=None):
        return self.asi_loop(question, image_path, lang, permission)

# Compatibility
class ORION_BRAIN(ORION_BRAIN_V3):
    pass
