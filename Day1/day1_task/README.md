# Agentic AI: Foundations and Open-Source Practice

## Day 1 – Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

This project compares three approaches to solving the same private-data task:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The project demonstrates the difference between using an LLM alone, using predefined programming rules, and combining an LLM with tools and an execution loop.

---

## 1. Project Scenario

### Private Student Assignment Assistant

The system uses a local JSON file containing sample student assignment information.

The user asks:

> Which assignments are due soon, and what should I work on first?

The system processes the assignment information and identifies upcoming deadlines.

The data is synthetic sample data created for this project and does not contain real private student information.

---

## 2. Project Architecture

### Plain Chatbot

```text
User Request
     ↓
    LLM
     ↓
Response
```

The assignment information is directly provided to the LLM.

---

### Rule-Based Workflow

```text
private_data.json
       ↓
Python Program
       ↓
Predefined Rules
       ↓
Decision
       ↓
Response
```

The workflow directly reads the JSON file and applies fixed conditions.

---

### AI Agent

```text
User Request
     ↓
    LLM
     ↓
Tool Selection
     ↓
get_student_assignments
     ↓
private_data.json
     ↓
Tool Result
     ↓
LLM Analysis
     ↓
Final Response
```

The AI agent uses an LLM together with a custom tool and an execution loop.

---

## 3. Technologies Used

* Python
* Groq API
* OpenAI GPT-OSS 20B model through Groq
* JSON
* Git and GitHub
* Python virtual environment

---

## 4. Project Structure

```text
agentic-ai-day1-assignment/
│
├── .gitignore
├── README.md
├── analysis.md
├── requirements.txt
├── private_data.json
│
├── chatbot.py
├── workflow.py
├── agent.py
│
└── Output/
    ├── chatbot_output.png
    ├── workflow_output.png
    └── agent_output.png
```

---

## 5. File Description

| File                | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| `chatbot.py`        | Implements the plain LLM chatbot                             |
| `workflow.py`       | Implements the predefined rule-based workflow                |
| `agent.py`          | Implements the AI agent with tool calling                    |
| `private_data.json` | Contains synthetic student assignment data                   |
| `analysis.md`       | Contains the detailed comparison and analysis                |
| `requirements.txt`  | Contains required Python packages                            |
| `.gitignore`        | Prevents unnecessary or sensitive files from being committed |
| `Output/`           | Contains screenshots of the three implementations            |

---

## 6. Installation

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd agentic-ai-day1-assignment
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 7. API Key Setup

This project uses the Groq API.

The API key should not be written directly inside the Python source code.

For Windows PowerShell, set the key using:

```powershell
$env:GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

Do not commit the API key to GitHub.

---

## 8. Running the Project

### Plain Chatbot

Run:

```powershell
python chatbot.py
```

The chatbot receives the assignment information through the prompt and generates a response using the LLM.

---

### Rule-Based Workflow

Run:

```powershell
python workflow.py
```

The workflow reads `private_data.json` and applies predefined rules.

It filters pending assignments, checks upcoming deadlines, and selects the assignment with the nearest deadline.

---

### AI Agent

Run:

```powershell
python agent.py
```

The agent uses the `get_student_assignments` tool to retrieve assignment information from the local JSON file.

The terminal output demonstrates the tool selection:

```text
[Agent Action]
Tool selected: get_student_assignments
Private data retrieved successfully.
```

---

## 9. Example Result

For the sample data, the three implementations identify:

```text
Database Management System
SQL Assignment
Deadline: 2026-09-23
Status: Pending
```

as the assignment with the earliest upcoming deadline.

The three systems reach the result using different approaches.

---

## 10. Key Learning

This project demonstrates the basic architecture of an AI agent:

```text
Agent = LLM + Tools + Loop
```

### LLM

The LLM understands the user's natural-language request and analyzes information.

### Tools

Tools allow the agent to interact with external data or perform actions.

In this project, the custom tool reads the local assignment data.

### Loop

The agent can repeatedly reason, use a tool, observe its result, and continue until it can produce a final response.

---

## 11. Comparison

| Feature                | Plain Chatbot                  | Rule-Based Workflow   | AI Agent                                             |
| ---------------------- | ------------------------------ | --------------------- | ---------------------------------------------------- |
| LLM                    | Yes                            | No                    | Yes                                                  |
| Predefined rules       | No                             | Yes                   | Can use instructions, but not limited to fixed rules |
| Tool usage             | No                             | Direct program access | Yes                                                  |
| Private-data retrieval | Information supplied in prompt | Direct file access    | Through a tool                                       |
| Flexibility            | High for conversation          | Limited               | High                                                 |
| Multi-step handling    | Limited                        | Programmed explicitly | Supported through agent loop                         |
| Decision-making        | LLM response generation        | Fixed conditions      | LLM-driven tool selection                            |
| Automation             | Limited                        | High for fixed tasks  | High for dynamic tasks                               |

---

## 12. Output Screenshots

### Plain Chatbot

The screenshot shows the LLM generating a response using the assignment information supplied in the prompt.

### Rule-Based Workflow

The screenshot shows the predefined Python rules filtering and sorting the assignments.

### AI Agent

The screenshot shows the agent selecting the `get_student_assignments` tool and using the retrieved private data to generate the final response.

The screenshots are available in the `Output/` directory.

---

## 13. Conclusion

The project demonstrates three different approaches to solving the same problem.

A plain chatbot is mainly focused on natural-language interaction using an LLM.

A rule-based workflow is useful for predictable tasks where the conditions can be explicitly programmed.

An AI agent combines an LLM with tools and an execution loop, allowing it to dynamically use available tools and process their results.

The experiment demonstrates why tools and an execution loop are important components of an agentic AI system.
