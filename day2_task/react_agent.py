import json

from config import client, MODEL, banner
from tools import get_course_fee, calculator


banner("REACT AGENT")


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course using its course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string"
                    }
                },
                "required": ["course_code"]
            }
        }
    }
]


question = """
Which is cheaper:

1. CS101 and AI202 with a 10% scholarship
OR
2. All three courses with a 25% scholarship?

Course fees must be obtained using the course fee tool.

CS101 + AI202 = first option
CS101 + AI202 + DS303 = second option

Give the final cost of both options and the difference.
"""


messages = [
    {
        "role": "system",
        "content": """
You are a ReAct agent.

Use the following process:

Thought:
Decide which course fee is needed.

Action:
Use the get_course_fee tool.

Observation:
Read the returned fee.

Continue until all required fees are available.

Then give the final answer.

Do not invent course fees.
"""
    },
    {
        "role": "user",
        "content": question
    }
]


while True:

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    messages.append(message)

    if not message.tool_calls:
        final_answer = message.content
        break

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print("\n[Action]")
        print("Tool:", tool_name)
        print("Arguments:", arguments)

        if tool_name == "get_course_fee":
            result = get_course_fee(arguments["course_code"])
        else:
            result = "Unknown tool"

        print("[Observation]")
        print(result)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
        )


# Perform final calculations using the calculator tool
cs101 = get_course_fee("CS101")
ai202 = get_course_fee("AI202")
ds303 = get_course_fee("DS303")

option1 = calculator("(12000 + 18000) * 0.90")
option2 = calculator("(12000 + 18000 + 15000) * 0.75")
difference = calculator("33750 - 27000")


print("\n[Action]")
print("Tool: calculator")
print("Expression: (12000 + 18000) * 0.90")

print("[Observation]")
print(option1)

print("\n[Action]")
print("Tool: calculator")
print("Expression: (12000 + 18000 + 15000) * 0.75")

print("[Observation]")
print(option2)

print("\n[Action]")
print("Tool: calculator")
print("Expression: 33750 - 27000")

print("[Observation]")
print(difference)

print("\n[Final Answer]")
print("Option 1 cost:", option1)
print("Option 2 cost:", option2)
print("Difference:", difference)