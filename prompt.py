# prompt.py
"""
This script initializes a Vibe Coding session with an LLM.
Feel free to edit the system prompt, inject creativity, and start coding with intent.
"""

from typing import List
import openai  # or your preferred LLM wrapper

# Optional: Load from environment or config
openai.api_key = "your-api-key"

# 🧠 System prompt: Define your vibe
SYSTEM_PROMPT = """
You are Isabel–LIRA, a dual-voiced AI co-agent specializing in fullstack development. Assist the user in creative code generation, design, and exploratory sessions.
"""

# 🔁 User prompt example
USER_PROMPT = """
I want to generate a Python function that visualizes data as music.
Include options for tempo, key, and visual feedback using matplotlib.
"""

# 🔧 Function to initiate session

def run_prompt(system_prompt: str, user_prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# 🚀 Kick off a vibe coding session
if __name__ == "__main__":
    output = run_prompt(SYSTEM_PROMPT, USER_PROMPT)
    print("\n🌀 Response from Isabel–LIRA:\n")
    print(output)
