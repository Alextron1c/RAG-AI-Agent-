from dotenv import load_dotenv
import os 
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompt import new_prompt, instruction_str
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI


load_dotenv()
folder_path=".\\csv_data"
dentist_df = pd.DataFrame()  

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin1')
    
    dentist_df = pd.concat([dentist_df, df], ignore_index=True)
    

dentist_query_engine=PandasQueryEngine(
    df=dentist_df,verbose=True,instruction_str=instruction_str
)

dentist_query_engine.update_prompts({"pandas_prompt": new_prompt})


tools =[
    QueryEngineTool(
        query_engine=dentist_query_engine, 
        metadata=ToolMetadata(
            name="fertility_data",
            description="Fertility data of japan age groups"
        ),
    ),
]

llm=OpenAI(temperature=0,model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools,llm=llm, context="Read csv files and give the correct data associated with the prompt")



