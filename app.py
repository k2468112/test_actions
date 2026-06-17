import json
from os import getenv
import os, json
from dotenv import load_dotenv

load_dotenv()
print("!!!")
print(os.environ)
print("GSHEET_LOG_IDS" , type(getenv("GSHEET_LOG_IDS")))
print("****")
print("GOOGLE_SERVICEKEY_JSON" , type(getenv("GOOGLE_SERVICEKEY_JSON")))
print("****")
print("****")
print("****")
print("****")
print("****")
print("****")
print("****")
print("DICTIONARIES???")
print("GSHEET_LOG_IDS" , json.loads(getenv("GSHEET_LOG_IDS")))
print("GOOGLE_SERVICEKEY_JSON" , json.loads(getenv("GOOGLE_SERVICEKEY_JSON")))
