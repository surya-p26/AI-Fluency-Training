import json
from datetime import datetime

print("=" * 60)
print("RULE-BASED WORKFLOW")
print("=" * 60)

with open("private_data.json", "r") as file:
    data = json.load(file)

assignments = data["assignments"]

today = datetime.strptime("2026-09-21", "%Y-%m-%d")

pending_assignments = []

for assignment in assignments:

    deadline = datetime.strptime(
        assignment["deadline"],
        "%Y-%m-%d"
    )

    days_left = (deadline - today).days

    # Predefined rules
    if assignment["status"] == "pending":

        if days_left >= 0 and days_left <= 7:

            pending_assignments.append({
                "subject": assignment["subject"],
                "task": assignment["task"],
                "deadline": assignment["deadline"],
                "days_left": days_left
            })

# Sort by nearest deadline
pending_assignments.sort(
    key=lambda x: x["days_left"]
)

print("\nAssignments due within 7 days:\n")

for assignment in pending_assignments:

    print(
        f"Subject: {assignment['subject']}"
    )

    print(
        f"Task: {assignment['task']}"
    )

    print(
        f"Deadline: {assignment['deadline']}"
    )

    print(
        f"Days remaining: {assignment['days_left']}"
    )

    print("-" * 40)


if pending_assignments:

    first = pending_assignments[0]

    print("\nRecommended first task:")
    print(
        f"{first['subject']} - {first['task']}"
    )

else:

    print("\nNo assignments are due soon.")