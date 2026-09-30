# Day 2 Task – Reasoning and Acting: Comparing Direct Prompting, Chain-of-Thought, and ReAct

## 1. Introduction

This task compares three approaches used with Large Language Models (LLMs): Direct Prompting, Chain-of-Thought (CoT) Prompting, and ReAct Agent. The comparison is based on a student course-fee and scholarship scenario.

The main question used for the ReAct demonstration was:

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? And by how much?

The course fees are:

* CS101 = Rs. 12,000
* AI202 = Rs. 18,000
* DS303 = Rs. 15,000

For the first option, CS101 and AI202 cost Rs. 30,000 before the scholarship. After a 10% scholarship, the cost is Rs. 27,000.

For the second option, all three courses cost Rs. 45,000 before the scholarship. After a 25% scholarship, the cost is Rs. 33,750.

Therefore, the first option is cheaper by Rs. 6,750.

The task also uses reasoning questions to compare direct prompting and Chain-of-Thought prompting and uses self-consistency to observe how repeated non-zero-temperature runs can vary.

---

## 2. Direct Prompting

Direct prompting asks the LLM to provide an answer without requiring an explicit reasoning process. The model receives the question and the required information directly in the prompt.

In this task, the direct prompting program provided the course fees and scholarship question to the model. The model generated the following result:

* CS101 + AI202 with a 10% scholarship = Rs. 27,000
* All three courses with a 25% scholarship = Rs. 33,750
* Difference = Rs. 6,750

The answer was correct.

The main advantage of direct prompting is simplicity. It requires less prompt structure and normally produces an answer quickly. It is suitable when the required information is already available in the prompt and the problem is relatively simple.

However, direct prompting does not provide a tool-use mechanism in this implementation. If the required information is missing from the prompt, the model cannot obtain it through an external tool. It may also provide less explanation about how it reached the answer.

---

## 3. Chain-of-Thought Prompting

Chain-of-Thought prompting asks the model to solve a problem through multiple reasoning steps before providing the final answer. In this task, three reasoning questions were tested.

### Question 1: Course instalment

The question involved three course fees of Rs. 12,000, Rs. 18,000 and Rs. 15,000, a 15% scholarship, and four equal instalments.

The direct version produced:

> Rs. 9,562.50 per instalment.

The Chain-of-Thought version calculated the total cost, calculated the scholarship, calculated the remaining amount, and divided the remaining amount by four.

The final answer was:

> Rs. 9,562.50 per instalment.

### Question 2: Computer laboratory

The question involved 18 computers, with two students using each computer in the morning and three students using each computer in the afternoon.

The direct version produced:

> 90

The Chain-of-Thought version calculated five student sittings per computer and then multiplied by 18 computers.

The final answer was:

> 90 student sittings.

### Question 3: Height comparison

The relationships were:

* Ravi is taller than Kumar.
* Kumar is taller than Arun.
* Priya is shorter than Arun.

The direct version produced:

> Tallest: Ravi
> Shortest: Priya

The Chain-of-Thought version constructed the complete ordering:

> Ravi > Kumar > Arun > Priya

The final answer was also:

> Ravi is the tallest and Priya is the shortest.

These experiments show that both direct prompting and Chain-of-Thought produced the same correct answers for the tested questions. The main difference was that Chain-of-Thought provided intermediate reasoning and calculations.

Chain-of-Thought is useful for multi-step reasoning problems, but it does not automatically provide missing external information. If the model needs information that is not present in the prompt, another mechanism such as tool use is required.

---

## 4. ReAct Agent

ReAct combines reasoning and acting by allowing an LLM to interact with tools. The general process used in this task is:

**Thought → Action → Observation → Thought/Action → Final Answer**

The ReAct implementation used two tool functions:

* `get_course_fee()` – obtains the fee for a course.
* `calculator()` – performs mathematical calculations.

During the actual run, the agent requested the following information:

### Action 1

Tool:

`get_course_fee`

Course:

`CS101`

Observation:

`12000`

### Action 2

Tool:

`get_course_fee`

Course:

`AI202`

Observation:

`18000`

### Action 3

Tool:

`get_course_fee`

Course:

`DS303`

Observation:

`15000`

The calculator was then used for the scholarship calculations.

### Action 4

Expression:

`(12000 + 18000) * 0.90`

Observation:

`27000.0`

### Action 5

Expression:

`(12000 + 18000 + 15000) * 0.75`

Observation:

`33750.0`

### Action 6

Expression:

`33750 - 27000`

Observation:

`6750`

The final result was:

* Option 1 = Rs. 27,000
* Option 2 = Rs. 33,750
* Difference = Rs. 6,750

This demonstrates the main advantage of ReAct in this scenario: the agent can obtain information using tools and then use the returned observations to produce the answer.

ReAct is more complex than direct prompting because it requires tool definitions, tool execution, and handling of observations. It may also require more model calls and therefore can be slower and more expensive than a simple direct prompt.

---

## 5. Comparison of the Three Approaches

| Aspect                              | Direct Prompting               | Chain-of-Thought                            | ReAct Agent                                         |
| ----------------------------------- | ------------------------------ | ------------------------------------------- | --------------------------------------------------- |
| Reasoning depth                     | Low to moderate                | Higher for multi-step problems              | Multi-step reasoning combined with actions          |
| Tool usage                          | No tool used                   | No tool used in this experiment             | Uses external tools                                 |
| Reliability on multi-step questions | Can solve simple problems      | Can improve structured multi-step reasoning | Useful when reasoning requires external information |
| Transparency                        | Final answer is mainly visible | Intermediate reasoning is requested         | Actions and observations are visible                |
| Speed / cost                        | Generally fastest and simplest | More output and reasoning                   | More steps and tool calls                           |
| Consistency across repeated runs    | Depends on temperature         | Can vary at non-zero temperature            | Depends on model and tool interactions              |

The comparison shows that the approaches serve different purposes. Direct prompting is simple when all required information is already available. Chain-of-Thought is useful when a problem requires several reasoning steps. ReAct becomes useful when the model must obtain information or perform actions using tools.

---

## 6. Self-Consistency Experiment

Self-consistency was tested using the course-instalment reasoning question.

The correct answer is:

**Rs. 9,562.50**

The model was run five times at a temperature of 0.8.

The actual results were:

| Run |  Answer |
| --- | ------: |
| 1   | 9562.50 |
| 2   | 9562.50 |
| 3   |  562.50 |
| 4   | 9562.50 |
| 5   | 9562.50 |

The majority answer was:

**9562.50**

The majority count was:

**4/5**

Four of the five runs produced the correct answer, while one run produced `562.50`. This demonstrates that a non-zero temperature can introduce variation between repeated runs.

The same question was then tested with temperature 0.

The actual results were:

| Run |  Answer |
| --- | ------: |
| 1   | 9562.50 |
| 2   | 9562.50 |
| 3   | 9562.50 |
| 4   | 9562.50 |
| 5   | 9562.50 |

The majority answer was:

**9562.50**

The majority count was:

**5/5**

In this experiment, temperature 0 produced the same correct answer in all five runs. Therefore, the experiment showed greater consistency at temperature 0 than at temperature 0.8 for this particular question.

---

## 7. Suitability for the Chosen Scenario

The three approaches are suitable for different parts of the scenario.

Direct prompting is suitable when the course-fee information is already supplied to the model and only a straightforward answer is required. It is simple and requires fewer components.

Chain-of-Thought prompting is suitable for questions involving multiple calculations or logical relationships. The experiments showed that it produced detailed intermediate calculations for the course-installment, laboratory, and height-comparison questions.

ReAct is suitable when the answer depends on obtaining information through tools. In the course-fee scenario, the ReAct agent obtained the CS101, AI202, and DS303 fees using the `get_course_fee` tool and then performed calculations. This makes the approach useful when information needs to be retrieved before the final answer can be produced.

Therefore, the suitability depends on the problem requirements rather than one approach being suitable for every situation.

---

## 8. Limitations

Direct prompting has limited access to information because the required information must be included in the prompt or already available to the model.

Chain-of-Thought can provide more detailed reasoning, but it still cannot automatically obtain missing external information without tools. It can also produce more output than a direct prompt.

ReAct requires additional implementation such as tool definitions, tool execution, and handling of tool responses. During development, the initial ReAct implementation encountered a tool-call validation error because the model generated an invalid calculator tool name. The implementation was then adjusted so that the required calculations were handled safely by the Python-side tool function.

Self-consistency requires multiple model calls. This can increase execution time and API usage. The temperature 0.8 experiment also showed that repeated runs can produce different answers, as one of the five runs returned `562.50` instead of `9562.50`.

---

## 9. Conclusion

Direct prompting, Chain-of-Thought prompting, and ReAct are different approaches for solving problems with LLMs.

Direct prompting is appropriate for simple questions where the required information is already available. It is straightforward and generally requires fewer processing steps.

Chain-of-Thought prompting is useful for problems that require multiple reasoning or calculation steps. In this experiment, it produced detailed calculations and reached the same correct answers as direct prompting for the tested reasoning questions.

ReAct is useful when a problem requires interaction with external information or tools. In the course-fee scenario, the agent retrieved course fees and used calculations before producing the final answer.

The self-consistency experiment showed that repeated runs at temperature 0.8 produced the correct answer in four out of five runs, while temperature 0 produced the same correct answer in all five runs for this particular test.

Overall, the choice of approach should depend on the problem. Direct prompting can be used when information is already available and the task is simple, Chain-of-Thought can be used for multi-step reasoning, and ReAct can be used when reasoning must be combined with tool-based information retrieval or actions.
