from core.coordinator import CoordinatorAgent

user = {
    "age": 22,
    "income": 180000,
    "occupation": "student",
    "language": "en"
}

agent = CoordinatorAgent()
schemes = agent.run(user)

for s in schemes:
    print(s)
