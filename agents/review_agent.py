from utils.language_utils import localize_benefit


class ReviewAgent:
    def __init__(self):
        pass

    def localize(self, schemes, language):
        """Return a localized copy of `schemes` without mutating input.

        The returned list preserves the original `benefit` under
        `benefit_original` and replaces `benefit` with the localized text
        so existing UI (which reads `benefit`) continues to work.
        """
        localized = []

        for s in schemes:
            s_copy = s.copy()
            s_copy["benefit_original"] = s_copy.get("benefit")
            s_copy["benefit"] = localize_benefit(s_copy["benefit"], language)
            localized.append(s_copy)

        return localized
