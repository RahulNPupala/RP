import json

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from agents.prompts import SYSTEM_PROMPT
from models.schemas import AgentDecision

class CommunicationAgent:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4.1-mini")
        print("LLM initialized")
        print("-" * 80)

    def decide(self, record, examples):
        HUMAN_PROMPT = """
        Examples:
        {examples}
        
        Current Input:
        {record}
        
        Return ONLY the decision JSON.
        """

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SYSTEM_PROMPT),
                ("human", HUMAN_PROMPT)
            ]
        )

        # Provide output in a specific format via with_structured_output(AgentDecision)
        chain = prompt | self.llm.with_structured_output(AgentDecision)

        return chain.invoke(
            {
                "examples": json.dumps(examples, indent=2),
                "record": json.dumps(record, indent=2)
            }
        )