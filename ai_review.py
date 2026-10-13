import os
import json

print("AI Review Started")

event_file = os.getenv("GITHUB_EVENT_PATH")

with open(event_file) as f:
    data = json.load(f)

print("PR Number:", data["pull_request"]["number"])
print("PR Title:", data["pull_request"]["title"])

print("AI Review Completed")