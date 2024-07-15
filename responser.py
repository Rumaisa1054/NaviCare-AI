from langflow.helpers import *
from langflow.graph import Graph
import os
import streamlit as st
from typing import List
from langflow.graph.schema import RunOutputs
from langflow.load import run_flow_from_json

# Ensure the environment variables are set
api_endpoint = os.getenv('api_endpoint')
token = os.getenv('token')
print()
print(api_endpoint)
print(token)
print()
if not api_endpoint or not token:
    raise ValueError("Astra DB credentials are not set in the environment variables.")

TWEAKS = {
    "AstraDBSearch-Sd8UL": {
        "api_endpoint": api_endpoint,
        "token": token,
        "collection_name": "doraforam"
    }
}

def doc_runner(prompt):
    result = run_flow_from_json(flow="doctor_finder.json", input_value=prompt, fallback_to_env_vars=True)
    return ((result[0].outputs[0]).results)

def visit(prompt):
    result = run_flow_from_json(flow="Notetaker.json", input_value=prompt, fallback_to_env_vars=True, tweaks=TWEAKS)
    return ((result[0].outputs[0]).results)

def apt(prompt):
    result = run_flow_from_json(flow="Appointment Maker.json", input_value=prompt, fallback_to_env_vars=True, tweaks=TWEAKS)
    return ((result[0].outputs[0]).results)

def well(prompt):
    result = run_flow_from_json(flow="Health&Wellness.json", input_value=prompt, fallback_to_env_vars=True, tweaks=TWEAKS)
    return ((result[0].outputs[0]).results)