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

damping_factor = 0.85

page_ranks = dict((filename, 1) for filename in html_filenames)
old_page_ranks = dict(page_ranks)

for _ in range(50):
    for filename in html_filenames:
        page_rank = 0
        for linked_file in in_links[filename]:
            page_rank += old_page_ranks[linked_file]/len(out_links[linked_file])
        page_rank = (1-damping_factor) + (damping_factor * page_rank)
        page_ranks[filename] = round(page_rank, 3)
        print("old_page_ranks: ", old_page_ranks)
        print("page_ranks: ", page_ranks)
        
    old_page_ranks = dict(page_ranks)

print("page_ranks : \n", page_ranks, end="\n\n")
