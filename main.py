from crewai import Crew
from dotenv import load_dotenv

from agents import linkedin_scraper_agent, web_researcher_agent, doppelganger_agent
from tasks import scrape_linkedin_task, web_research_task, create_linkedin_post_task
from tools import post_on_linkedin_fn

load_dotenv()


crew = Crew(
    agents=[
        linkedin_scraper_agent,
        web_researcher_agent,
        doppelganger_agent
    ],
    tasks=[
        scrape_linkedin_task,
        web_research_task,
        create_linkedin_post_task
    ]
)

result = crew.kickoff()


print("Here is the result: ")
print(result)


with open('results/result.txt','w') as file :
    file.write(result)

post_on_linkedin_fn()