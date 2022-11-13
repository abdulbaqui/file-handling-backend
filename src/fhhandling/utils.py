import os
import glob
import random
from collections import Counter
from collections import OrderedDict
from itertools import islice


def handle_uploaded_file(f):
    destination = "media/"
    with open(f"{destination}{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def find_length_file(file_name):
    num_of_lines = 0
    with open("media/" + file_name, "r") as fp:
        num_of_lines = len(fp.readlines())
    return num_of_lines


def fetch_random_line(line_number=False):
    files_path = os.path.join("media/", "*")
    files = glob.glob(files_path)
    str = []
    query_line = line_number
    line_number = int(line_number) - 1
    for f in files:
        file = open(f)
        content = file.readlines()
        if find_length_file(os.path.basename(f)) >= int(line_number):
            readline = content[line_number]
            str.append(f"filename:{f}, line number:{query_line}, readline:{readline}")
            file.close()
    return str


def read_media_folder(one_rendom_line=True):
    files_path = os.path.join("media/", "*")
    files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
    latestfiles = []
    if one_rendom_line == True:
        temp = os.path.getctime(files[0])
        for f in files:
            if temp == os.path.getctime(f):
                latestfiles.append(os.path.basename(f))
            else:
                break
    else:
        for f in files:
            latestfiles.append(os.path.basename(f))
    return latestfiles


def one_rendom_line():
    latestfiles = read_media_folder(True)
    dict_filedetial = []
    for f in latestfiles:
        with open("media/" + f, "r") as fp:
            num_of_lines = find_length_file(f)
            file = open("media/" + f)
            content = file.readlines()
            random_line = ""
            while random_line == "":
                random_line_num = random.randint(0, num_of_lines)
                random_line = content[random_line_num]
                random_line = random_line.replace(" ", "")
                counter = Counter(random_line)
                most_common = counter.most_common(1)[0]
            file.close()
            dict_filedetial.append(
                {
                    "linenumber": random_line_num,
                    "filename": f,
                    "frequently_occured": most_common[0],
                }
            )
    return dict_filedetial


def long_hundred_lines():
    files_path = os.path.join("media/", "*")
    files = glob.glob(files_path)
    old_length_line, length_line, str = 0, 0, ""
    for f in files:
        file = open(f)
        content = file.readlines()
        if find_length_file(os.path.basename(f)) >= 99:
            readline = content[99]
            length_line = len(readline.strip())
            if length_line > old_length_line:
                old_length_line = length_line
                str = f"filename:{f},line:{readline}"
    return str


def twenty_longestline():
    dict = {}
    lis = []
    count = 1
    files_path = os.path.join("media/", "*")
    files = glob.glob(files_path)
    random_file = random.randint(0, len(files) - 1)
    length_file = find_length_file(os.path.basename(files[random_file]))
    while length_file < 20:
        random_file = random.randint(0, len(files) - 1)
    file = files[random_file]
    file = file = open(file)
    for line in file:
        num = len(line)
        dict.update({num: {"line": line.strip()}})
    file.close()
    dict = OrderedDict(sorted(dict.items(), reverse=True))

    for i in dict.values():
        if count <= 20:
            lis.append(i)
            count = count + 1
        else:
            break
    # dict = islice(dict.items(), 20)
    return lis
