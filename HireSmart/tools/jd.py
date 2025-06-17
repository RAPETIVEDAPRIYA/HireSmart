from adk.tools import AgentTool
import re
import openai
class JDParser(AgentTool):
    def run(self,input):
        jd=input.get("jd")
        if not jd:
            return {"error": "no job description found"}
        jd_clean=self.clean_text(jd)
        jd_text=self.skills_extract(jd_clean)
    def clean_text(self,text):
        text = re.sub(r"<.*?>","",text)
        text=re.sub(r"\s+"," ",text).strip()
        return text
    def skills_extract(self,text):
        try:
            response=openai.ChatCompletion.create(
                model="gpt-4o"
                messages = [{"role":"system","content":"You are an expert HR assistant and need extract the required skills"},
                messages = {"role":"user","content":"Extract a list of all tools , technical skills, frameworks and soft skills from this text:\n{text}"}],
                temperature = 0.2
            )
            content = response['choices'][0]['messages']['content']
            skills=re.split(r",|\n|-",content)
            skills = [s.strip() for s in skills if s.strip()]
            return list(set(skills))
        except Exception as e:
            return [f"AI extraction failed: {str(e)}"]