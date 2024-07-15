from langflow.load import run_flow_from_json
from langflow.helpers import *
from langflow.graph import Graph
TWEAKS = {
"ChatInput-L0uOU": {},
"TextOutput-N20Bj": {},
"OpenAIEmbeddings-eVjoh": {},
"OpenAIModel-2vxW0": {},
"Prompt-ogc6k": {},
"File-za6DG": {},
"RecursiveCharacterTextSplitter-bsgSY": {},
"AstraDBSearch-agcpq": {},
"AstraDB-7t3HQ": {},
"OpenAIEmbeddings-KuzNY": {},
"ChatOutput-ATIfO": {}
}
def get_bot_response(response_data):
    return response_data['outputs'][0]['outputs'][0]['results']['message']['data']['text']

"""tweaks = TWEAKS"""
def doc_runner1(prompt):
    result = run_flow_from_json(flow="doctor_finder.json",
                                input_value=prompt
                                )
    
    return ((result[0].ouputs[0]).results)
import time
import random
import requests
import json
BASE_API_URL = "http://localhost:7860/api/v1/run"
FLOW_ID =  "437d30ca-21d9-47c6-8328-67248785f37f"

def run_flow(message, endpoint, output_type="chat", input_type="chat", tweaks=None):
    api_url = f"{BASE_API_URL}/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    if tweaks:
        payload["tweaks"] = tweaks
    response = requests.post(api_url, json=payload)
    return response.json()
    
def doc_runner(prompt):
    bot_response = get_bot_response(run_flow("", FLOW_ID, tweaks=TWEAKS))
    return bot_response


    