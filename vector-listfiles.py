import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
  client = OpenAI(
    api_key=os.getenv("ENV_AI_API_KEY")
  )

  allFiles = client.files.list()
  
  for file in allFiles:
    # print(file)
    print(file.filename)

if __name__ == "__main__":
  main()
