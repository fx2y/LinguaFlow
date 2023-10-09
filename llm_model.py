class LLMModel:
    @staticmethod
    def is_compatible_personality(personality, mode):
        # Check if personality is compatible with LLM model and task requirements
        if mode == "task1":
            if personality in ["A", "B", "C"]:
                return True
            else:
                return False
        elif mode == "task2":
            if personality in ["D", "E", "F"]:
                return True
            else:
                return False
        else:
            return False
