from src.langgraphagenticai.state.state import State
from langchain_core.messages import AIMessage

class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a chatbot response.
        """
        response = self.llm.invoke(state['messages'])
        return {"messages": [response]}

