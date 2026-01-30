class GenerationAgent:
    def __init__(self):
        pass

    def explain(self, schemes):
        result = []

        for s in schemes:
            result.append({
                "name": s["name"],
                "benefit": s["benefit"],
                "steps": s["steps"]
            })

        return result
