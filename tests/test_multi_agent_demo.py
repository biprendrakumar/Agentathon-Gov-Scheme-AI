import pytest

from agents.research_agent import ResearchAgent
from agents.review_agent import ReviewAgent


def test_research_eligibility():
	research = ResearchAgent()

	user = {"age": 22, "income": 180000, "occupation": "student", "language": "en"}
	schemes = research.find_schemes(user)
	names = {s["name"] for s in schemes}

	assert "Pradhan Mantri Jan Dhan Yojana" in names
	assert "National Scholarship Scheme" in names
	assert "PM Kisan Samman Nidhi" not in names


def test_review_localize_preserves_original():
	review = ReviewAgent()
	schemes = [{"name": "X", "benefit": "Original benefit", "steps": []}]

	out = review.localize(schemes, "hi")

	# original list must not be mutated
	assert schemes[0]["benefit"] == "Original benefit"

	# returned object should include the localized benefit and original preserved
	assert out[0]["benefit"] != schemes[0]["benefit"]
	assert out[0]["benefit_original"] == "Original benefit"
