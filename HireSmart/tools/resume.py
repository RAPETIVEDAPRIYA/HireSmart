from adk.agent_tool import AgentTool
import pdfplumber
class ResumeParser(AgentTool):
    def run(self,input):
        file_path=input.get("file_path")
        if not file_path:
            return {"error": "No resume found"}
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for p in pdf.pages:
                    text+= p.extract_text() + "\n"
        except Exception as e:
            return {"error":str(e)}
        return {"resume_text": text.strip()}