from collections import Counter

from config import client, MODEL, banner
from cot_compare import COT_PROMPT
import re

QUESTION = """
A student takes three courses costing Rs. 12,000,
Rs. 18,000 and Rs. 15,000. She gets a 15% scholarship
on the total and pays the rest in 4 equal instalments.

How much is each instalment?
"""


def get_answer(text):
    numbers = re.findall(r"\d+(?:,\d{3})*(?:\.\d+)?", text)

    if numbers:
        return numbers[-1].replace(",", "")

    return "Answer not extracted"


def run_once(temperature):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": COT_PROMPT
            },
            {
                "role": "user",
                "content": QUESTION
            }
        ],
        temperature=temperature
    )

    return get_answer(
        response.choices[0].message.content
    )


if __name__ == "__main__":

    banner("SELF-CONSISTENCY")

    RUNS = 5
    TEMPERATURE = 0.8

    answers = []

    print("\nTemperature:", TEMPERATURE)

    for i in range(RUNS):

        answer = run_once(TEMPERATURE)

        print(f"Run {i + 1}: {answer}")

        answers.append(answer)

    majority, count = Counter(
        answers
    ).most_common(1)[0]

    print("\nMajority Answer:")
    print(majority)

    print(f"\nMajority Count: {count}/{RUNS}")

    print("\nNow run again with temperature = 0.")