import os
import re
import argparse


# Initialize parser.
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-u", "--host", help = "url host", default="https://sudan-club-austria.github.io/training-unit")

# Read arguments from command line
args = parser.parse_args()

def extract_hrefs_and_srcs(folder_path, url):
  """
  Extracts href and src attributes from HTML files within a specified folder and its subfolders.

  Args:
    folder_path: The path to the folder containing HTML files.

  Returns:
    A list of tuples, where each tuple contains the href and src attributes of an HTML element.
  """

  print (f"adding absolute path '{url}' ")
  hrefs_and_srcs = []

  for root, dirs, files in os.walk(folder_path):
    for file in files:
      if file.endswith(".html"):
        file_path = os.path.join(root, file)
        with open(file_path, 'r') as f:
          content = f.read()

        new_content = re.sub(r'(href|src)(="|= ")(/)', rf'\1="{url}/', content)
        final_content = re.sub(r'url\(\/static', f'url({url}/static', new_content)

        head_end = final_content.find('</head>')
        tracked_content = final_content[:head_end] + '<!-- Google tag (gtag.js) --><script async src="https://www.googletagmanager.com/gtag/js?id=G-CTEQ3ZJW1H"></script><script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag("js", new Date());gtag("config", "G-CTEQ3ZJW1H");</script>' + final_content[head_end:]

        with open(file_path, 'w') as f:
          f.write(tracked_content)

  return hrefs_and_srcs



folder_path = "./naucse_build"
results = extract_hrefs_and_srcs(folder_path, args.host)