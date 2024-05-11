from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets_mock
from output_parsers import summary_parser


def ice_break_with(name: str) -> str:

    # real data extraction using agents
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_username, mock=True)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets_mock(twitter_username)

    summary_template = """
    given the information about a person from Linkedin {information},
    and their latest twitter posts {twitter_posts} I want you to create:
    1. A short summary
    2. two interesting facts about them

    Use both information from Twitter and Linkedin
    \n{format_instruction}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instruction": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})

    print(res)


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with(name="Eden Marco Udemy")
