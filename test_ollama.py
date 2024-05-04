from langchain_community.llms import Ollama

if __name__ == "__main__":

    llm = Ollama(model="llama2")

    print(llm.invoke("Tell me a joke about weather"))
