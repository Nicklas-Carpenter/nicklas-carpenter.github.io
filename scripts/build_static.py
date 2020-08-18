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
        self.html = ""
        self.inside_tag = False

    def handle_starttag(self, tag, attrs):
        if len(self.html) > 0:
            self.html += "<{0}".format(tag)
        else:
            self.html = "<{0}".format(tag)
        for attr in attrs:
            if attr[0] == "src" and attr[1] == "../dist/bundle.js":
                self.html += ' {0}="{1}"'.format(attr[0], "index.js")
            else:
                self.html += ' {0}="{1}"'.format(attr[0], attr[1])
        self.html += ">"
        self.inside_tag = True
    
    def handle_endtag(self, tag):
        self.html += "</{0}>".format(tag)

    def handle_startendtag(self, tag, attrs):
        if len(self.html) > 0:
            self.html += "<{0}".format(tag)
        else:
            self.html = "<{0}".format(tag)
        for attr in attrs:
            if attr[0] == "src" and attr[1] == "../dist/bundle.js":
                self.html += ' {0}="{1}"'.format(attr[0], "index.js")
            else:
                self.html += ' {0}="{1}"'.format(attr[0], attr[1])
        self.html += "/>"
        self.inside_tag = False

    def handle_data(self, data):
        if self.inside_tag: 
            self.html += data.strip("\n ")

    def return_html(self):
        return self.html


def main():
    # Check to ensure we are in the right directory
    if not os.path.basename(os.getcwd()) == "scripts":
        os.chdir("scripts");

    # Create the output script if it does not already exist
    if not os.path.exists("../dist/bundle.js"):
        subprocess.call(["npm", "run", "static"]);

    if not os.path.exists("../static"):
        os.mkdir("../static")

    # Copy bundle.js to the static directory
    try:
        bundle_js = open("../dist/bundle.js", "r")

        try:
            index_js = open("../static/index.js", "w")
            for line in bundle_js.readlines():
                index_js.write(line)
            
            index_js.close()
        except IOError as err:
            print("When attempting to open index.js: ",err.strerror,
                file = sys.stderr
            )

        bundle_js.close()
    except IOError as err:
        print(
            "While attempting to open bundle.js: ",
            err.strerror, 
            file=sys.stderr
        )

    # Copy index.html to the static directory
    try:
        index_html = open("../public/index.html", "r")

        try:
            index_html_copy = open("../static/index.html", "w")

            html = index_html.read(os.stat("../public/index.html").st_size)
            parser = HTMLTouchUp()
            parser.feed(html)

            index_html_copy.write(parser.return_html())
            index_html_copy.close()
        except IOError as err:
            print(
                "When attempting to open static/index.html: ",
                err.strerror,
                file = sys.stderr
            )
        
        index_html.close()
    except IOError as err:
        print(
            "While attempting to open public/index.html: ",
            err.strerror, 
            file=sys.stderr
        )

if __name__ == "__main__":
    main()