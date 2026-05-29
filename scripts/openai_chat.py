#!/usr/bin/env python3
import os
import sys
import openai

def main():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("Error: OPENAI_API_KEY not set. See README.md")
        sys.exit(1)
    openai.api_key = key
    prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Say hello from VS Code"
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2,
    )
    try:
        content = resp["choices"][0]["message"]["content"]
    except Exception:
        content = str(resp)
    print(content)

if __name__ == "__main__":
    main()
