"""
Utilize this script by passing in the title of the research paper that you wish to create a citation for

E.g. python index-generator.py "Efficient Logistic Regression on Large Encrypted Data"

Then copy the index printed by the script into the index list of the .md file.
"""

import sys

title = str(sys.argv[1])
parsed_title = title.lower().replace(" ", "-").replace(":", "")


print(f"[{title}](#{parsed_title})")