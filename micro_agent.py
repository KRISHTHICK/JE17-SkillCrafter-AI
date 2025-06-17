import subprocess

def ask_micro_agent(prompt):
    command = f"A user wants to learn: {prompt}. Generate tips and guidance."
    result = subprocess.run(["ollama", "run", "tinyllama", command], capture_output=True, text=True)
    return result.stdout.strip()
