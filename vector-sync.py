import os
import argparse

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv("ENV_AI_API_KEY"),
  organization=os.getenv("ENV_AI_ORGANIZATION"),
)

# Upload files to OpenAI
def upload_files_to_openai():
  parser = argparse.ArgumentParser(description="Enter the folder path")
  parser.add_argument('-f', '--folder', type=str, help='Folder path')
  parser.add_argument('-v', '--vector_id', type=str, help='Vector ID')
  
  args = parser.parse_args()
  folder_path = args.folder
  vector_id = args.vector_id
  
  if not os.path.isdir(folder_path):
    print(f"The folder path {folder_path} does not exist.")
    return
  
  file_paths = []
  
  # List all files in the specified folder
  for filename in os.listdir(folder_path):
    if filename.endswith(".txt") or filename.endswith(".pdf") or filename.endswith(".doc") or filename.endswith(".docx"):
      file_paths.append(os.path.join(folder_path, filename))
  
  file_paths.sort()
  file_streams = [open(path, "rb") for path in file_paths]
  
  file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_id, files=file_streams
  )
  
  # Print the status and the file counts of the batch to see the result of this operation.
  print(f'------------------')
  print(file_paths)
  print(f'------------------')
  print(f'File Batch: {file_batch.id}')
  print(f'Status: {file_batch.status}')
  print(f'File(s): {file_batch.file_counts}')

if __name__ == "__main__":
  upload_files_to_openai()
