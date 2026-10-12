import os

print("AI Review Started")

print("Repository:", os.getenv("GITHUB_REPOSITORY"))
print("Event:", os.getenv("GITHUB_EVENT_NAME"))