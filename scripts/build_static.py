from __future__ import print_function
import os
import os.path
import subprocess
from HTMLParser import HTMLParser
import string
import sys

class HTMLTouchUp(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.cur_tag = ""

    def handle_starttag(self, tag, attrs):
        if len(self.cur_tag) > 0:
            self.cur_tag += "<{0}".format(tag)
        else:
            self.cur_tag = "<{0}".format(tag)
        for attr in attrs:
            self.cur_tag += ' {0}="{1}"'.format(attr[0], attr[1])
        self.cur_tag += ">"
    
    def handle_endtag(self, tag):
        self.cur_tag += "</{0}>".format(tag)

    def handle_startendtag(self, tag, attrs):
        if len(self.cur_tag) > 0:
            self.cur_tag += "<{0}".format(tag)
        else:
            self.cur_tag = "<{0}".format(tag)
        for attr in attrs:
            if attr[0] == "src" and attr[1] == "../dist/bundle.js":
                self.cur_tag += ' {0}="{1}"'.format(attr[0], "index.js")
            else:
                self.cur_tag += ' {0}="{1}"'.format(attr[0], attr[1])
        self.cur_tag += "/>"

    def handle_data(self, data):
        self.cur_tag += data

    def return_tag(self):
        return self.cur_tag


def main():
    # Check to ensure we are in the right directory
    if not os.path.basename(os.getcwd()) == "scripts":
        os.chdir("scripts");

    # Create the output script if it does not already exist
    if not os.path.exists("../dist/bundle.js"):
        subprocess.call(["npm", "run", "build"]);

    if not os.path.exists("../static"):
        os.mkdir("../static")

    bundle_js = None
    index_js = None
    index_html = None
    index_html_copy = None

    # Copy bundle.js to the static directory
    try:
        bundle_js = open("../dist/bundle.js", "r")
    except IOError as err:
        print(
            "While attempting to open bundle.js: ",
            err.strerror, 
            file=sys.stderr
        )

    try:
        index_js = open("../static/index.js", "w")
    except IOError as err:
        print("When attempting to open index.js: ",err.strerror,
            file = sys.stderr
        )


    for line in bundle_js.readlines():
        index_js.write(line)

    # Copy index.html to the static directory
    try:
        bundle_js = open("../dist/bundle.js", "r")
    except IOError as err:
        print(
            "While attempting to open bundle.js: ",
            err.strerror, 
            file=sys.stderr
        )

    try:
        index_js = open("../static/index.js", "w")
    except IOError as err:
        print(
            "When attempting to open index.js: ",
            err.strerror,
            file = sys.stderr
        )


    for line in bundle_js.readlines():
        index_js.write(line)
main()