import random
import string
import os

num_files = 20
filename_length = 10

html_filenames = []
for _ in range(num_files):
    random_filename = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=filename_length)) + '.html'
    html_filenames.append(random_filename)

try:
    os.mkdir("generated_html_files")
except:
    pass

base_dir = "generated_html_files"

for filename in html_filenames:
    with open(os.path.join(base_dir, filename), 'w') as file_obj:
        file_obj.write("<p> This is page {} </p> \n".format(filename))

        filenames_to_link = set()
        for _ in range(random.randint(0, num_files)):
            filenames_to_link.add(random.choice(html_filenames))

        for filename_to_link in filenames_to_link:
            file_obj.write('<a href="{}"> Page B link </a> \n'.format(filename_to_link))

