#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


"""
spacyRPCServer.py

(C) 2017 by Damir Cavar <damir@cavar.me>

This code runs Spacy in server mode as an XML-RPC server.

The defaults are:
- port = 8000
- host = "localhost"
- language = 'en'

Prerequisites:
- Python 3.x
- Installed modules: spacy, argparse


\copyright Copyright 2017 by Damir Cavar

\license{Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.}
"""


import argparse, sys
from xmlrpc.server import SimpleXMLRPCServer
import spacy


def usage():
    print("spacyRPC")


if __name__=="__main__":
    parser = argparse.ArgumentParser(prog="spacyRPC",
                                     description='Command line arguments.',
                                     epilog='')

    parser.add_argument('-p', '--port', dest="port", default=8000, type=int, help="Port number")
    parser.add_argument('-n', '--hostname', dest="hostname", default="localhost", help="Server name or IP address")
    parser.add_argument('-l', '--language', dest="language", default="en", choices=['en', 'de'], help="Language pipeline")

    args = parser.parse_args()

    # main(args.hostname, args.port, args.language)

    server = SimpleXMLRPCServer((args.hostname, args.port),
                                allow_none=True)
    server.register_introspection_functions()

    nlp = spacy.load(args.language)
    def parse(text):
        doc = nlp(text, parse=True)
        for sentence in doc.sents:
            res = tuple( [ x.text for x in sentence ] )
        print(res)
        return res
    server.register_function(parse)

    print('Serving XML-RPC on', args.hostname, 'port', args.port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)

