#!/usr/bin/env python3
import os
import sys
from anthropic import Client

def main():
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        print("Error: ANTHROPIC_API_KEY not set. See README.md")
        sys.exit(1)
    client = Client(api_key=key)
    prompt_input = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Say hello from VS Code"
    prompt = f"Human: {prompt_input}\nAssistant:"
    resp = client.completions.create(
        model="claude-2.1",
        prompt=prompt,
        max_tokens_to_sample=300,
    )
    try:
        print(resp.completion)
    except Exception:
        print(resp)

if __name__ == "__main__":
    main()
