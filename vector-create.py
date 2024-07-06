import os
import argparse

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create a new vector store
def create_store():
  parser = argparse.ArgumentParser(description="Create a new vector store")
  parser.add_argument('-p', '--project_id', type=str, help='Project ID')
  parser.add_argument('-n', '--name', type=str, help='Name of the store')

  args = parser.parse_args()
  project_id = args.project_id
  name = args.name
  
  client = OpenAI(
    api_key=os.getenv("ENV_AI_API_KEY"),
    organization=os.getenv("ENV_AI_ORGANIZATION"),
    project=project_id,
  )
      
  store = client.beta.vector_stores.create(
    name=name
  )
  
  print(f'Vector Store: {store.id}')

if __name__ == "__main__":
  create_store()
