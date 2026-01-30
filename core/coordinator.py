from agents.research_agent import ResearchAgent
from agents.generation_agent import GenerationAgent
from agents.review_agent import ReviewAgent


class CoordinatorAgent:
    def __init__(self):
        self.research = ResearchAgent()
        self.generate = GenerationAgent()
        self.review = ReviewAgent()

    def _validate_user(self, user: dict):
        required = {
            "age": int,
            "income": (int, float),
            "occupation": str,
            "language": str,
        }

        if not isinstance(user, dict):
            raise ValueError("`user` must be a dict")

        for key, expected in required.items():
            if key not in user:
                raise ValueError(f"Missing required user field: {key}")
            if not isinstance(user[key], expected):
                raise ValueError(f"Invalid type for {key}: expected {expected}")

    def run(self, user):
        self._validate_user(user)

        schemes = self.research.find_schemes(user)
        explained = self.generate.explain(schemes)
        final_output = self.review.localize(explained, user["language"])
        return final_output
