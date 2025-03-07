from crewai.flow import Flow, start, listen

from hello_flow.crews.dev_crew.dev_crew import DevCrew

class DevFlow(Flow):
    @start()
    def generate_code(self):
        print("Generating code")
        result=DevCrew().crew().kickoff(inputs={"problem":"write python code for login page component"})
        return result.raw
    
    
def kickoff2():
    obj=DevFlow()
    output=obj.kickoff()
    print(output)
    
if __name__ == "__main__":
    kickoff2    