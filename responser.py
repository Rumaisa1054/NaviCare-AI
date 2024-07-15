
from langflow.helpers import *
from langflow.graph import Graph
import os
import streamlit as st
from typing import List
from langflow.graph.schema import RunOutputs
from langflow.load import run_flow_from_json
TWEAKS = {
"ChatInput-L0uOU": {},
"TextOutput-N20Bj": {},
"OpenAIEmbeddings-eVjoh": {},
"OpenAIModel-ibL7G": {},
"Prompt-ogc6k": {},
"File-za6DG": {},
"RecursiveCharacterTextSplitter-bsgSY": {},
"AstraDBSearch-agcpq": {},
"AstraDB-7t3HQ": {},
"OpenAIEmbeddings-KuzNY": {},
"ChatOutput-ATIfO": {}
}

def doc_runner(prompt):
    result = run_flow_from_json(flow="doctor_finder.json",input_value=prompt,fallback_to_env_vars=True,tweaks=TWEAKS)
    return ((result[0].ouputs[0]).results)

def visit(prompt):
    result = run_flow_from_json(flow="Notetaker.json",input_value=prompt,fallback_to_env_vars=True,tweaks=TWEAKS)
    return ((result[0].ouputs[0]).results)

def apt(prompt):
    result = run_flow_from_json(flow="Appointment Maker.json",input_value=prompt,fallback_to_env_vars=True,tweaks=TWEAKS)
    return ((result[0].ouputs[0]).results)

def well(prompt):
    result = run_flow_from_json(flow="Health&Wellness.json",input_value=prompt,fallback_to_env_vars=True,tweaks=TWEAKS)
    return ((result[0].ouputs[0]).results)

  

    