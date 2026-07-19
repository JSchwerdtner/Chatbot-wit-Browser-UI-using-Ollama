from google.adk.agents import Agent


root_agent = Agent(
    name="CorporateAssistant",
    model="gemini-2.0-flash", 
    instruction="You are a helpful assistent."
)