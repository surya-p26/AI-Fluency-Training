from config import client, MODEL, banner

QUESTION = """
Which is cheaper: CS101 and AI202 with a 10% scholarship,
or all three courses with a 25% scholarship?
And by how much?

Course fees:
CS101 = Rs. 12,000
AI202 = Rs. 18,000
DS303 = Rs. 15,000
"""

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "Answer the question directly. Do not explain the steps."
        },
        {
            "role": "user",
            "content": QUESTION
        }
    ],
    temperature=0
)

banner("DIRECT PROMPTING")

print("\nQuestion:")
print(QUESTION)

print("\nAnswer:")
print(response.choices[0].message.content)