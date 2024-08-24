import os
import re

def extract_hrefs_and_srcs(folder_path):
  """
  Extracts href and src attributes from HTML files within a specified folder and its subfolders.

  Args:
    folder_path: The path to the folder containing HTML files.

  Returns:
    A list of tuples, where each tuple contains the href and src attributes of an HTML element.
  """

  hrefs_and_srcs = []

  for root, dirs, files in os.walk(folder_path):
    for file in files:
      if file.endswith(".html"):
        file_path = os.path.join(root, file)
        with open(file_path, 'r') as f:
          content = f.read()

        new_content = re.sub(r'(href|src)="(/)', r'\1="https://baloola.github.io/sudan-house/', content)

        with open(file_path, 'w') as f:
          f.write(new_content)

  return hrefs_and_srcs

# Example usage
folder_path = "./naucse_build"
results = extract_hrefs_and_srcs(folder_path)
print(results)