import os
import re
from collections import defaultdict

out_links = {}
in_links = defaultdict(list)

html_filenames = [filename for filename in os.listdir(".") if filename.endswith(".html")]

for filename in html_filenames:
    with open(filename, "r") as html_file:
        contents = html_file.read()
        links = re.findall(r'href="(.+\.html)"', contents)
        out_links[filename] = links
        for link in links:
            in_links[link].append(filename)

print("out_links : \n", out_links, end="\n\n")
print("in_links : \n", in_links, end="\n\n")

# authorities score for a node is the sum of the hubs scores of all the nodes pointing to that node
# hubs score for a node is the sum of the authorities scores of all the nodes that it points to

hubs_scores = dict((filename, 1) for filename in html_filenames)
authorities_scores = {}


while True:
    old_hubs_scores = dict(hubs_scores)
    old_authorities_scores = dict(authorities_scores)

    for filename in html_filenames:
        authorities_scores[filename] = sum(hubs_scores[linked_filename] for linked_filename in in_links[filename])
    
    # normalize authorities scores
    authorities_scores_total = sum(authorities_scores.values())
    for filename, score in authorities_scores.items():
        authorities_scores[filename] = round(score/authorities_scores_total, 3)

    for filename in html_filenames:
        hubs_scores[filename] = sum(authorities_scores[linked_filename] for linked_filename in out_links[filename])

    # normalize hubs scores
    hubs_scores_total = sum(hubs_scores.values())
    for filename, score in hubs_scores.items():
        hubs_scores[filename] = round(score/hubs_scores_total, 3)

    if (hubs_scores.items() == old_hubs_scores.items()) and (authorities_scores == old_authorities_scores):
        break

    print("authorities_scores: ", authorities_scores)
    print("hubs_scores: ", hubs_scores)
    print("\n\n")
