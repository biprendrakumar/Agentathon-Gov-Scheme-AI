from data.schemes_data import SchemeDatabase

class ResearchAgent:
    def __init__(self):
        self.db = SchemeDatabase()

    def find_schemes(self, user):
        eligible = []

        for scheme in self.db.get_schemes():
            if user["income"] <= scheme["income_limit"]:
                if scheme["occupation"] == "any" or scheme["occupation"] == user["occupation"]:
                    eligible.append(scheme)

        return eligible
