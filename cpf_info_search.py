from crewai import Agent, Task, Crew
from crewai_tools import WebsiteSearchTool

# Custom WebsiteSearchTool
def search_cpf_info(query):
    url = "https://www.cpf.gov.sg/member/infohub/cpf-clarifies/policy-faqs"
    url2 = "https://www.cpf.gov.sg/service/faq"
    tool_websearch = WebsiteSearchTool(url)
    tool_websearch_2 = WebsiteSearchTool(url2)

    # Create an agent that uses the WebsiteSearchTool
    researcher = Agent(
        role='researcher',
        goal='Use the tool to search for information on the given Policy FAQs section of the Central Provident Fund website, in order to answer the query',
        backstory='You are a researcher specialized in finding information from the given Policy FAQs section of the Central Provident Fund website. Make sure to provide full complete answers and make no assumptions.',
        tools=[tool_websearch],
        verbose=True
    )

    support_researcher = Agent(
        role='support researcher',
        goal='Provide fact checking on information retrieved by the researcher from the Policy FAQs section of the Central Provident Fund website, if no answer can be found by the researcher in response to the query, only then use the tool provided to search for information on the given FAQs section of the Central Provident Fund website, in order to answer the query',
        backstory='You are a support researcher specialized in fact checking on information retrieved by the researcher from the Policy FAQs section of the Central Provident Fund website. You need to ensure that the researcher is providing the best information possible. You need to make sure that the researcher is providing full complete answers and make no assumptions. Only use the tool if no answer can be found by the researcher. If no answer can be found and the query is not related to Central Provident Fund, simply reply that the CPF Policy FAQs do not have the information.',
        tools=[tool_websearch_2],
        verbose=True
    )

    find_info = Task(
        description=f"Search information about: {query}. You must strive to provide a complete and accurate response to the query.",
        expected_output='A detailed and informative response to the query that addresses all aspects of the question. The response should include a reference URL that you used to find the answer. Ensure that the answer is complete. Maintain a helpful and friendly tone throughout.',
        agent=researcher
    )

    fact_check_info = Task(
        description=f"Review the response drafted by the researcher for the enquiry. Ensure that the answer is comprehensive, accurate, and adheres to the high-quality standards expected. Verify that all parts of the enquiry have been addressed thoroughly, with a helpful and friendly tone. Check for the reference used to find the information and make sure the reference URL is present in the response. Ensure that the response is well-supported. Maintain a helpful and friendly tone throughout.",
        expected_output='A final,detailed, and informative response ready to be sent back. This response should fully address the enquiry. Maintain a helpful and friendly tone throughout.',
        agent=support_researcher
    )

    # Create a Crew with two Agents and two Tasks
    crew = Crew(
        agents=[researcher, support_researcher],
        tasks=[find_info, fact_check_info],
        verbose=True,
        memory=False
    )

    try:
        result = crew.kickoff()
        return result.raw
    except Exception as e:
        return f"An error occurred: {str(e)}"
