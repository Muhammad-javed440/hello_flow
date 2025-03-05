from crewai.flow import Flow, start, listen

from hello_flow.crews.dev_crew.dev_crew import DevCrew

class DevFlow(Flow):
    @start()
    def generate_code(self):
        print("Generating code")
        result=DevCrew().crew().kickoff(inputs={"problem":"write python code for addition two numbers"})
        return result.raw
    
    
def kickoff1():
    obj=DevFlow()
    output=obj.kickoff()
    print(output)
    
if __name__ == "__main__":
    kickoff1    