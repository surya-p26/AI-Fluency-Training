from groq import Groq

client = Groq()

MODEL = "openai/gpt-oss-20b"


def banner(title):
    print("=" * 60)
    print(title)
    print("=" * 60)