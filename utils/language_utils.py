def localize_benefit(benefit: str, language: str) -> str:
	"""Return a localized version of a benefit string.

	This is intentionally simple — replace or extend with real translations later.
	"""
	if language == "hi":
		# lightweight demonstration translation; replace with real i18n later
		return f"यह योजना: {benefit}"
	return benefit
