from data.schemes_data import SchemeDatabase
import copy


class ResearchAgent:
    def __init__(self):
        self.db = SchemeDatabase()

    def find_schemes(self, user):
        # Get regular schemes from database
        schemes = self.db.get_schemes()
        all_schemes = []

        # Normalize user input
        user_age = user["age"]
        user_income = user["income"]
        user_occupation = user["occupation"].lower()
        user_caste = user.get("caste", "any").lower()

        # Process regular schemes
        for scheme in schemes:
            scheme_copy = copy.deepcopy(scheme)
            eligibility = scheme_copy.get("eligibility", {})

            scheme_copy["is_eligible"] = self._is_eligible(
                user_age,
                user_income,
                user_occupation,
                user_caste,
                eligibility
            )
            all_schemes.append(scheme_copy)

        # Add AI-generated personalized schemes
        ai_schemes = self.db.generate_ai_schemes(user)
        for scheme in ai_schemes:
            scheme_copy = copy.deepcopy(scheme)
            eligibility = scheme_copy.get("eligibility", {})

            scheme_copy["is_eligible"] = self._is_eligible(
                user_age,
                user_income,
                user_occupation,
                user_caste,
                eligibility
            )
            # Mark as AI-generated
            scheme_copy["is_ai_generated"] = True
            all_schemes.append(scheme_copy)

        return all_schemes

    # -----------------------------
    # Eligibility Logic
    # -----------------------------
    def _is_eligible(self, age, income, occupation, caste, eligibility):
        min_age = eligibility.get("min_age")
        max_age = eligibility.get("max_age")
        max_income = eligibility.get("max_income")
        occupations = eligibility.get("occupation", ["any"])
        castes = eligibility.get("caste", ["any"])

        if min_age is not None and age < min_age:
            return False

        if max_age is not None and age > max_age:
            return False

        if max_income is not None and income > max_income:
            return False

        if "any" not in occupations and occupation not in occupations:
            return False

        if "any" not in castes and caste not in castes:
            return False

        return True
