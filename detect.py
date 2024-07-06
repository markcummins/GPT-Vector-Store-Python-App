import os
import argparse

from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import shutil

# Ensures the language detection is deterministic
DetectorFactory.seed = 0

def move_files_based_on_language():
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

  # Loop through all files in the directory
  for filename in os.listdir(folder_path):
      # Check if the file is a text file
      if filename.endswith('.txt'):
          file_path = os.path.join(folder_path, filename)
          try:
              with open(file_path, 'r', encoding='utf-8') as file:
                  text = file.read()
                  language = detect(text)
                  
                  # Create the target directory if it doesn't exist
                  target_dir = os.path.join(folder_path, language)
                  if not os.path.exists(target_dir):
                      os.makedirs(target_dir)
                  
                  # Move the file to the target directory
                  target_path = os.path.join(target_dir, filename)
                  shutil.move(file_path, target_path)
                  print(f"Moved file: {filename} to {target_dir}")
          except LangDetectException:
              print(f"File: {filename} - Language could not be detected")
          except Exception as e:
              print(f"Error processing file {filename}: {e}")
      else:
          print(f"Skipping non-text file: {filename}")

# Call the function
if __name__ == "__main__":
  move_files_based_on_language()

