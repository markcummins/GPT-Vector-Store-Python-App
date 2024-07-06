import os
import argparse

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv("ENV_AI_API_KEY")
)

# List all files in the specified folder
def list_files():
  parser = argparse.ArgumentParser(description="Enter the folder path")
  
  parser.add_argument('-f', '--folder', type=str, help='Folder path')

  args = parser.parse_args()
  folder_path = args.folder
  
  print('')
  print('settings:')
  print(f'Folder path: {folder_path}')
  print('')
    
  if not os.path.isdir(folder_path):
    print(f"The folder path {folder_path} does not exist.")
    return
  
  file_paths = []
  
  # List all files in the specified folder
  for filename in os.listdir(folder_path):
    if filename.endswith(".txt") or filename.endswith(".pdf") or filename.endswith(".docx") or filename.endswith(".doc"):
      file_paths.append(os.path.join(folder_path, filename))
      
  print('files:')
  print(file_paths)

if __name__ == "__main__":
  list_files()
