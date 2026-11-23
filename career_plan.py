name = input("Enter your name: ")
age = int(input("How old are you right now? "))

print(f"\n--- AI ROADMAP FOR {name.upper()} ---")

if age < 18:
    years_left = 18 - age
    print(f"Stage: High School Builder ({years_left} years until university)")
    print("Focus now: Score A+ in Add Maths, learn Python, and build mini-projects!")
elif age <= 22:
    print("Stage: University Tech Student")
    print("Focus now: Compete in hackathons, build a GitHub portfolio, and land a top internship!")
else:
    print("Stage: Career Switcher / Tech Pro")
    print("Focus now: Master LLM deployment, cloud tools, and ship production AI systems!")