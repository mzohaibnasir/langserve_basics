from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate


from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os


from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# langchain
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


fastAPIapp = FastAPI(
    title="Langchain Server", version="1.0", description="A simple API server"
)

# adding routes
# add_routes(fastAPIapp, ChatOpenAI(), path="/openai")

# to integrate prompt template with the route
# model1
llmOpenAI = ChatOpenAI()
# model2
llmLlama = Ollama(model="llama2")


# will interact with openAI
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

# will interact with llama2
prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} with 100 words"
)


add_routes(fastAPIapp, prompt1 | llmOpenAI, path="/essay")

add_routes(fastAPIapp, prompt2 | llmLlama, path="/poem")


if __name__ == "__main__":
    uvicorn.run(fastAPIapp, host="localhost", port=8000)
