#change dir_path to where you have downloaded the .htm files; remember that Windows uses back slashes and Macs use forward slashes

import glob
import os.path
from bs4 import BeautifulSoup

dir_path = r"/Users/admin/Downloads"

for file_name in glob.glob(os.path.join(dir_path, "*.htm")):
    with open(file_name) as html_file:
        soup = BeautifulSoup(html_file, "html.parser")

    results_file = os.path.splitext(file_name)[0] + '.txt'
    with open(results_file, 'wt') as outfile:
        for i in soup.find_all('p'):
            outfile.write(i.text + "\n")
