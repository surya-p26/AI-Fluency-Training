import json
from groq import Groq

client = Groq()


# ==================================================
# PRIVATE DATA TOOL
# ==================================================

def get_student_assignments():
    """
    Reads assignment information from private_data.json.
    """

    with open("private_data.json", "r") as file:
        data = json.load(file)

    return json.dumps(data["assignments"])


# ==================================================
# TOOL DEFINITION
# ==================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_student_assignments",
            "description": (
                "Read the student's private assignment "
                "information from the local JSON file."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


# ==================================================
# USER REQUEST
# ==================================================

user_question = """
Which assignments are due soon?

Please:
1. Identify pending assignments.
2. Identify assignments with upcoming deadlines.
3. Tell me which assignment I should work on first.
4. Explain the reason.
"""


# ==================================================
# INITIAL REQUEST TO LLM
# ==================================================

messages = [
    {
        "role": "system",
        "content": """
You are an AI student assignment assistant.

You have access to private student assignment
information through a tool.

When assignment information is needed,
use the get_student_assignments tool.

After receiving the tool result:
- Analyze the assignments.
- Identify pending assignments.
- Identify upcoming deadlines.
- Suggest which task should be handled first.
- Explain the reason.
- Do not invent information.
"""
    },
    {
        "role": "user",
        "content": user_question
    }
]


# ==================================================
# AGENT LOOP
# ==================================================

while True:

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    # Add model response to conversation
    messages.append(message)

    # Check whether the model requested a tool
    if not message.tool_calls:
        break

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name

        print("\n[Agent Action]")
        print("Tool selected:", tool_name)

        if tool_name == "get_student_assignments":

            # Execute the tool
            result = get_student_assignments()

            print("Private data retrieved successfully.")

            # Send tool result back to the LLM
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )


# ==================================================
# FINAL RESPONSE
# ==================================================

print("\n" + "=" * 60)
print("AI AGENT")
print("=" * 60)

print("\nUser Request:")
print(user_question)

print("\nAgent Response:")
print(message.content)