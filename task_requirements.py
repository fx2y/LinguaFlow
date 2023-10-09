class TaskRequirements:
    @staticmethod
    def is_compatible_role(role, mode):
        # Check if role is defined
        if not role:
            return False, "Error: Agent role is not defined."

        # Check if role is consistent with task requirements
        if mode == "task1":
            if role not in ["role1", "role2"]:
                return False, "Error: Agent role is not consistent with task requirements."
        elif mode == "task2":
            if role not in ["role3", "role4"]:
                return False, "Error: Agent role is not consistent with task requirements."
        else:
            return False, "Error: Invalid mode."

        return True, ""
