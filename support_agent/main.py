import os
from dotenv import load_dotenv
from config import GEMINI_API_KEY
from context import UserContext
from agents import triage

load_dotenv()

print("🎓 Welcome to the Support Agent Console System\n")

name = input("Enter your name: ")
is_premium = input("Are you a premium user? (yes/no): ").strip().lower() == "yes"

context = UserContext(name=name, is_premium=is_premium)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ("exit", "quit"):
        break

    response = triage.triage(user_input, context)

    # Output Guardrail: remove "sorry"
    response = response.replace("sorry", "[filtered]")

    print(f"Agent: {response}")
