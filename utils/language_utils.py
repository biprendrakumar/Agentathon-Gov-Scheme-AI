def localize_benefit(benefit: str, language: str) -> str:
	"""Return a localized version of a benefit string.

	This is intentionally simple — replace or extend with real translations later.
	"""
	if language == "hi":
		# lightweight demonstration translation; replace with real i18n later
		return f"यह योजना: {benefit}"
	return benefit


def localize_name(name: str, language: str) -> str:
	"""Return a localized version of a scheme name."""
	if language == "hi":
		# Simple translations for demo
		translations = {
			"Pradhan Mantri Jan Dhan Yojana": "प्रधान मंत्री जन धन योजना",
			"PM Kisan Samman Nidhi": "पीएम किसान सम्मान निधि",
			"National Scholarship Scheme": "राष्ट्रीय छात्रवृत्ति योजना"
		}
		return translations.get(name, name)
	return name


def localize_steps(steps: list, language: str) -> list:
	"""Return localized steps."""
	if language == "hi":
		# Simple translations
		step_translations = {
			"Visit nearest bank": "निकटतम बैंक जाएं",
			"Submit Aadhaar and PAN": "आधार और पैन जमा करें",
			"Fill account opening form": "खाता खोलने का फॉर्म भरें",
			"Visit pmkisan.gov.in": "pmkisan.gov.in पर जाएं",
			"Register farmer details": "किसान विवरण दर्ज करें",
			"Submit land documents": "जमीन के दस्तावेज जमा करें",
			"Visit scholarships.gov.in": "scholarships.gov.in पर जाएं",
			"Register with Aadhaar": "आधार के साथ पंजीकरण करें",
			"Apply for scholarship": "छात्रवृत्ति के लिए आवेदन करें"
		}
		return [step_translations.get(step, step) for step in steps]
	return steps
