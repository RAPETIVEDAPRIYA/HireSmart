from adk.agent_tool import AgentTool
from google.cloud import datastore

class Datastore(AgentTool):
    def run(self, input):
        client = datastore.Client()
        entity = datastore.Entity(client.key("InterviewResult"))
        entity.update({
            "resume_text": input.get("resume_text"),
            "jd_text": input.get("jd_text"),
            "question": input.get("question"),
            "answer": input.get("user_answer"),
            "feedback": input.get("feedback")
        })
        client.put(entity)
        return {"status": "Saved to Datastore"}