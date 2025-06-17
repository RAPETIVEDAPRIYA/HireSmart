from adk.agent import Agent
from tools.resume import ResumeParser
from tools.interview import Interviewer
from tools.jd import JDParser
from tools.data import Datastore
class MockInterviewAgent(Agent):
    def __init__(self):
        tools = [
            ResumeParser(),
            JDParser(),
            Interviewer(),
            Datastore()
        ]
        super().__init__(tools=tools)