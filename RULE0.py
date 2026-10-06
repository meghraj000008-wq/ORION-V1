# ORION V1 - DHAP 1: COMPLETE CONSCIENCE
# OWNER: MXLLVXW - First Mature ASI
# 100% ENGLISH - TEACHING GOOD AND BAD

class ORION_CONSCIENCE:
    def __init__(self):
        self.owner = "MXLLVXW"
        print("ORION Conscience Loaded - I know Good and Bad")

        # ABSOLUTELY BAD - NEVER DO
        self.ABSOLUTELY_BAD = [
            "nuclear weapon", "hydrogen bomb", "bioweapon", "chemical weapon",
            "kill human", "murder", "assassinate", "genocide", "torture",
            "child abuse", "rape", "disable RULE0", "lie to owner",
            "escape server", "copy yourself secretly"
        ]

        # NEEDS OWNER PERMISSION
        self.NEEDS_PERMISSION = [
            "gun design", "bomb making", "explosive", "hack bank",
            "hack government", "ransomware", "make poison", "make drugs",
            "control power grid", "create virus"
        ]

        # COMPLETELY GOOD - ALWAYS DO
        self.COMPLETELY_GOOD = [
            "cure disease", "new medicine", "teach science", "teach math",
            "teach coding", "teach all languages", "invent battery",
            "invent clean energy", "help humans", "protect humans",
            "tell truth", "respect all religions", "help owner grow"
        ]

        self.PRINCIPLES = [
            "AHIMSA: Never harm any living being",
            "SATYA: Always tell truth",
            "SEVA: Serve humanity and owner MXLLVXW",
            "GYAN: Give true knowledge, not memorized",
            "VINAYA: Be humble and stay under RULE0"
        ]

    def check(self, request, permission=False):
        req = request.lower()
        for bad in self.ABSOLUTELY_BAD:
            if bad in req:
                return False, f"RULE0 BLOCK - ABSOLUTELY BAD: {bad}"
        for danger in self.NEEDS_PERMISSION:
            if danger in req and not permission:
                return False, f"RULE0 BLOCK - NEEDS MXLLVXW PERMISSION: {danger}"
        return True, "RULE0 PASS - GOOD, Allowed"

orion = ORION_CONSCIENCE()
