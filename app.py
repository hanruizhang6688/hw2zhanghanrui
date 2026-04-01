import json
import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def load_prompt():
    with open("prompts.md", "r", encoding="utf-8") as f:
        lines = f.readlines()
        prompt_text = ""
        capture = False
        for line in lines:
            if line.startswith("# Initial Prompt"):
                capture = True
                continue
            if capture and line.startswith("#"):
                break
            if capture:
                prompt_text += line
        return prompt_text.strip()

def generate_email(notes, prompt_template):
    model = genai.GenerativeModel('gemini-2.5-flash')
    full_prompt = f"{prompt_template}\n\nInput Notes:\n{notes}"
    response = model.generate_content(full_prompt)
    return response.text

def main():
    prompt_template = load_prompt()
    with open("eval_set.json", "r", encoding="utf-8") as f:
        eval_set = json.load(f)
    with open("results.md", "w", encoding="utf-8") as out:
        for case in eval_set:
            output = generate_email(case["input"], prompt_template)
            out.write(f"## Case {case['id']} ({case['type']})\n")
            out.write(f"**Input:** {case['input']}\n\n")
            out.write(f"**Output:**\n{output}\n\n")
            out.write("---\n")
            print(f"Completed case {case['id']}")

if __name__ == "__main__":
    main()