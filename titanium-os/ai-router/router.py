import os
from openai import OpenAI
import google.generativeai as genai
from anthropic import Anthropic

class TitaniumRouter:
    def __init__(self):
        self.oai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.claude = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    def route_task(self, task_type, prompt):
        # Intelligens útvonalválasztás a divízió és feladat alapján
        if task_type == "RESEARCH":
            model = genai.GenerativeModel('gemini-1.5-pro')
            return model.generate_content(prompt).text
        elif task_type == "SALES_COPY":
            res = self.oai.chat.completions.create(
                model="gpt-4o", messages=[{"role": "user", "content": prompt}])
            return res.choices[0].message.content
        elif task_type == "CONTRACT":
            res = self.claude.messages.create(
                model="claude-3-5-sonnet-20240620", max_tokens=1000,
                messages=[{"role": "user", "content": prompt}])
            return res.content[0].text
