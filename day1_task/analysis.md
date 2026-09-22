# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Introduction

AI systems can solve tasks in different ways depending on how they are designed. A plain chatbot mainly uses a Large Language Model (LLM) to understand a user request and generate a response. A rule-based workflow follows predefined programming rules and conditions to process information. An AI agent combines an LLM with tools and an execution loop so that it can decide when a tool is needed, use the tool, observe the result, and continue processing until the task is completed.

This project compares these three approaches using a private student assignment management scenario.

## 2. Scenario

The selected scenario is a Private Student Assignment Assistant.

The system contains student assignment information such as subject, task name, deadline, and completion status. This information is stored locally in a JSON file named `private_data.json`.

The user asks:

"Which assignments are due soon, and what should I work on first?"

The objective is to compare how a plain chatbot, a rule-based workflow, and an AI agent handle the same task.

## 3. Private Data

The project uses sample student assignment data stored in `private_data.json`.

The data contains:

* Subject
* Assignment or task name
* Deadline
* Status

The data is synthetic sample data created for this project. No real personal or confidential student information is used.

The assignments include Database Management System, Operating Systems, Computer Networks, and Artificial Intelligence.

## 4. Plain Chatbot

### 4.1 How it works

The plain chatbot uses an LLM to generate a response based on information supplied directly in the conversation.

The assignment information is included in the prompt given to the LLM. The chatbot then generates a natural-language answer to the user's question.

The chatbot does not independently access the private JSON file.

### 4.2 Data Used

The assignment information is manually provided to the LLM as part of the prompt.

### 4.3 Tools

The plain chatbot does not use external or custom tools.

It only uses the LLM to understand the provided information and generate a response.

### 4.4 Request Handling

The chatbot receives the assignment information and the user's question. It analyzes the supplied information and generates a recommendation.

For example, it identifies the Database Management System SQL Assignment as the first task because it has the earliest deadline.

### 4.5 Limitations

The chatbot cannot automatically retrieve new information from the private JSON file in this implementation.

If the assignment data changes, the updated information must be provided to the chatbot.

Therefore, it is useful for conversation and explanation when the required information is already available, but it does not independently perform private-data retrieval.

## 5. Rule-Based Workflow

### 5.1 How it works

The rule-based workflow uses predefined Python instructions to process the private assignment data.

It reads `private_data.json`, checks the status and deadline of each assignment, filters assignments according to predefined conditions, and sorts them by the number of days remaining.

### 5.2 Data Used

The workflow directly reads the local `private_data.json` file.

### 5.3 Rules

The workflow uses predefined rules such as:

1. Check whether the assignment status is `pending`.
2. Calculate the number of days remaining until the deadline.
3. Select assignments due within seven days.
4. Sort the selected assignments by the nearest deadline.
5. Select the assignment with the smallest number of days remaining.

### 5.4 Request Handling

The workflow follows the same predefined process every time.

For the sample data, the SQL Assignment is selected first because it has the nearest deadline among the pending assignments.

### 5.5 Limitations

The workflow is predictable and easy to understand, but it has limited flexibility.

If the user asks a completely different type of question, additional programming rules may be required.

The workflow does not use an LLM to dynamically decide which action or tool is required.

## 6. AI Agent

### 6.1 How it works

The AI agent combines an LLM, a tool, and an execution loop.

The LLM receives the user's request and determines that assignment information is required. It selects the `get_student_assignments` tool.

The tool reads the private assignment information from `private_data.json` and returns the result to the agent.

The LLM then analyzes the retrieved information and produces the final answer.

The process can be represented as:

LLM → Tool Selection → Tool Execution → Observation → LLM Analysis → Final Response

### 6.2 Data Used

The AI agent accesses the same local `private_data.json` file, but it does so through a custom tool called:

`get_student_assignments`

The assignment information is therefore not manually inserted into the initial user prompt.

### 6.3 Tools

The agent has access to the `get_student_assignments` tool.

The tool is responsible for reading the private JSON data.

The agent decides when the tool is required.

### 6.4 Agent Loop

The agent follows an iterative process:

1. Receive the user's request.
2. Analyze whether private assignment information is required.
3. Select the appropriate tool.
4. Execute the tool.
5. Receive the tool result.
6. Analyze the retrieved information.
7. Generate the final response.

In the experiment, the terminal output showed:

`Tool selected: get_student_assignments`

followed by:

`Private data retrieved successfully.`

This demonstrates the tool-use part of the agent architecture.

### 6.5 Request Handling

The agent can interpret the user's natural-language request and use the available tool to obtain the required information.

After retrieving the assignment data, it identifies pending assignments, checks upcoming deadlines, and recommends the task with the earliest deadline.

### 6.6 Limitations

The agent depends on the quality of the LLM, tool implementation, instructions, and validation.

An agent may also require additional safeguards when working with important or sensitive data.

Therefore, tool access and agent decisions should be properly controlled and tested.

## 7. Comparison

| Basis for comparison | Plain Chatbot                                  | Rule-Based Workflow                     | AI Agent                                                  |
| -------------------- | ---------------------------------------------- | --------------------------------------- | --------------------------------------------------------- |
| Flexibility          | High for natural-language responses            | Limited to predefined rules             | High because the LLM can adapt to different requests      |
| Decision-making      | Generates a response from supplied information | Uses fixed programmed conditions        | LLM can decide when a tool is needed                      |
| Tool usage           | No custom tool                                 | Program directly accesses the JSON file | Uses a custom tool to retrieve private data               |
| Private-data access  | Information must be supplied to the model      | Direct access through program code      | Access through an agent tool                              |
| Multi-step handling  | Mainly generates a response                    | Possible when explicitly programmed     | Can perform tool-use steps through an execution loop      |
| Automation           | Limited for private-data retrieval             | High for predefined tasks               | High for dynamic tasks                                    |
| Reliability          | Depends on supplied information and LLM output | Predictable for programmed cases        | Depends on the model, tools, instructions, and validation |

## 8. Suitability Analysis

### Plain Chatbot

A plain chatbot is suitable when the required information is already available in the conversation and the main requirement is explanation, summarization, or natural-language interaction.

For example, a student could provide their assignment list and ask the chatbot to summarize it.

### Rule-Based Workflow

A rule-based workflow is suitable when the task follows fixed and predictable conditions.

For example, automatically finding all pending assignments due within seven days is a suitable rule-based task because the conditions can be explicitly programmed.

### AI Agent

An AI agent is suitable when the user may ask different types of questions and the system needs to decide when to retrieve information or use a tool.

For example, the student may ask about pending assignments, upcoming deadlines, or a specific subject. The agent can use the assignment retrieval tool and then analyze the returned information according to the request.

## 9. Conclusion

The three approaches solve the same assignment-management scenario using different architectures.

The plain chatbot mainly focuses on understanding the user's request and generating a response using information supplied to the LLM.

The rule-based workflow uses predefined programming conditions to process private data. It is predictable and effective for fixed tasks.

The AI agent combines an LLM, tools, and an execution loop. It can decide when a tool is required, retrieve private information through the tool, observe the result, and use the information to generate a response.

Therefore, the appropriate approach depends on the task. Plain chatbots are useful for conversational responses, rule-based workflows are useful for predictable processes, and AI agents are useful for dynamic tasks that require reasoning and tool usage.
