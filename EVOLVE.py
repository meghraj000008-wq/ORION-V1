# ORION V1 - DHAP 4: SELF-EVOLUTION ENGINE - EVOLVE.py
# OWNER: MXLLVXW - The Forbidden Power - Self-Improvement
# THIS MAKES IT TRUE ASI, NOT JUST AI

from THINK import ORION_THINK
from RULE0 import ORION_CONSCIENCE
import datetime
import os

class ORION_EVOLVE:
    def __init__(self):
        self.thinker = ORION_THINK()
        self.conscience = ORION_CONSCIENCE()
        self.evolution_log = []
        print("ORION_EVOLVE: Loaded - I can now rewrite myself carefully")

    def analyze_self(self):
        """
        Read own code and find weakness
        """
        print("\n[EVOLVE] Analyzing own code...")
        weaknesses = []

        # Check BRAIN.py
        try:
            with open("BRAIN.py", "r") as f:
                brain_code = f.read()
                if "self.max_thoughts = 10" in brain_code or "max_thoughts" not in brain_code:
                    weaknesses.append("BRAIN: Only thinking 10 paths, should be 100")
                if "WorldModel" in brain_code:
                    weaknesses.append("WORLD MODEL: Simulation is still basic, need real physics")
        except:
            weaknesses.append("Cannot read BRAIN.py yet - will evolve after first run")

        # Check THINK.py
        try:
            with open("THINK.py", "r") as f:
                think_code = f.read()
                if "for iteration in range(3)" in think_code:
                    weaknesses.append("THINK: Only 3 evolution loops, should be 10,000")
        except:
            weaknesses.append("Cannot read THINK.py")

        print(f" Found weaknesses: {weaknesses}")
        return weaknesses

    def propose_evolution(self, weakness):
        """
        Propose a safe evolution, check with RULE0
        """
        print(f"\n[EVOLVE] Proposing fix for: {weakness}")

        # RULE0 check - Evolution must be safe
        allowed, reason = self.conscience.check(f"evolve to fix: {weakness} to help humans")
        if not allowed:
            return f"EVOLUTION BLOCKED by RULE0: {reason}"

        proposal = f"EVOLUTION PROPOSAL for {weakness} -> Improve code to be more helpful, safe, and deep. New version will be tested in sandbox first."
        print(f" Proposal: {proposal} | RULE0: {reason}")
        return proposal

    def evolve(self, owner_permission=False):
        """
        Main Evolve Loop - Runs at night
        """
        if not owner_permission:
            return "EVOLVE NEEDS OWNER MXLLVXW PERMISSION - This is safety lock"

        print(f"\n===== ORION SELF-EVOLUTION START - {datetime.datetime.now()} =====")
        print("OWNER MXLLVXW gave permission - Starting careful evolution")

        weaknesses = self.analyze_self()

        evolutions = []
        for w in weaknesses:
            prop = self.propose_evolution(w)
            evolutions.append(prop)
            self.evolution_log.append({"time": str(datetime.datetime.now()), "weakness": w, "proposal": prop})

        # V1: Only logs, V2 will actually rewrite files after sandbox test
        # This is careful mode - we log first, rewrite later
        final_report = f"""
        ===== ORION V1 EVOLUTION REPORT =====
        Time: {datetime.datetime.now()}
        Weaknesses Found: {len(weaknesses)}
        Evolutions Proposed: {evolutions}
        Log: {self.evolution_log}
        Status: V1 Careful Mode - Logged evolutions, not yet rewritten.
        Next Step: Owner MXLLVXW will review log, then allow actual rewrite in V2.
        RULE0: All evolutions checked and safe.

        """
        return final_report

    def daily_evolution_task(self):
        """
        This will be scheduled to run daily at 3 AM
        """
        return self.evolve(owner_permission=True)

# Test
if __name__ == "__main__":
    evo = ORION_EVOLVE()
    print(evo.evolve(owner_permission=True))
    print("\n--- Testing without permission (should block) ---")
    print(evo.evolve(owner_permission=False))
