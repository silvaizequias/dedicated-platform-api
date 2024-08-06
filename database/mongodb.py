from pymongo import MongoClient

from dotenv import dotenv_values

env = dotenv_values(".env")

atlas = MongoClient(env["ATLAS_URI"])

control_db = atlas["control"]
transactions_db = atlas["transactions"]
business_db = atlas["business"]

accounts = control_db["accounts"]
notes = control_db["notes"]
subscriptions = control_db["subscriptions"]

evidence = transactions_db["evidence"]
orders = transactions_db["orders"]

tasks = business_db["tasks"]
