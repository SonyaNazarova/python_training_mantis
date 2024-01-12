import random
import string
from model.project import Project
import os.path
import jsonpickle
import getopt
import sys

try:
    opts,args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
out = "../data/projects.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        out = a


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_status():
    status = ["в разработке", "выпущен", "стабильный", "устарел"]
    return random.choice(status)

def random_view_state():
    status = ["публичный", "приватный"]
    return random.choice(status)


testdata = [
    Project(name = random_string("name",10), status = random_status(),
            view_state = random_view_state(),
            description = random_string("description", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), out)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))