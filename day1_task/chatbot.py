from groq import Groq

client = Groq()

print("=" * 60)
print("PLAIN CHATBOT")
print("=" * 60)

assignment_information = """
The student has the following assignments:

1. Database Management System - SQL Assignment
   Deadline: 2026-09-23
   Status: Pending

2. Operating Systems - Process Scheduling Report
   Deadline: 2026-09-25
   Status: Pending

3. Computer Networks - Network Topology Exercise
   Deadline: 2026-09-30
   Status: Completed

4. Artificial Intelligence - AI Agent Lab
   Deadline: 2026-09-24
   Status: Pending
"""

question = """
Which assignment should the student work on first?
Explain the reason.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful student assistant. "
                "Use only the information provided by the user. "
                "Do not access files or external tools."
            )
        },
        {
            "role": "user",
            "content": assignment_information + "\n" + question
        }
    ]
)

print("\nQuestion:")
print(question)

print("\nChatbot Response:")
print(response.choices[0].message.content)