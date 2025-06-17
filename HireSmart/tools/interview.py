from adk.agent_tool import AgentTool
import openai

class Interviewer(AgentTool):
    def run(self, input):
        resume = input.get("resume_text")
        jd = input.get("jd_text")
        user_answer = input.get("user_answer")
        
        if not user_answer:
            # Generate mock interview question
            prompt = f"Given this resume:\n{resume}\nand this JD:\n{jd}\nGenerate a technical interview question."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return {"question": response['choices'][0]['message']['content']}
        else:
            # Score the user's answer
            prompt = f"Here is a question: {input.get('question')}\nHere is the answer: {user_answer}\nProvide a score out of 10 and feedback."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return {"feedback": response['choices'][0]['message']['content']}