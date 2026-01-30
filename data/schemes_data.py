class SchemeDatabase:
    def __init__(self):
        self.schemes = [
            {
                "name": "Pradhan Mantri Jan Dhan Yojana",
                "income_limit": 250000,
                "occupation": "any",
                "benefit": "Zero balance bank account with insurance",
                "steps": [
                    "Visit nearest bank",
                    "Submit Aadhaar and PAN",
                    "Fill account opening form"
                ]
            },
            {
                "name": "PM Kisan Samman Nidhi",
                "income_limit": 200000,
                "occupation": "farmer",
                "benefit": "₹6000 yearly financial support",
                "steps": [
                    "Visit pmkisan.gov.in",
                    "Register farmer details",
                    "Submit land documents"
                ]
            },
            {
                "name": "National Scholarship Scheme",
                "income_limit": 300000,
                "occupation": "student",
                "benefit": "Scholarship for education",
                "steps": [
                    "Visit scholarships.gov.in",
                    "Register with Aadhaar",
                    "Apply for scholarship"
                ]
            }
        ]

    def get_schemes(self):
        return self.schemes
