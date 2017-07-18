#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
spacyRPCClient.py

(C) 2017 by Damir Cavar <damir@cavar.me>

In LingData use SentenceData to store properties of sentences and all tokens

The output of the Spacy pipeline is a sequence of sentences, plus correference of elements across sentences.

This code represents a XML-RPC client for the SpacyRPC server.

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


import os.path, sys, glob
from LingData import SentenceData, Document, labels
import xmlrpc.client


def main(fname):
    print(fname)

    example = "Tim Cook is the CEO of Apple. He is not the CEO of Google."

    s = xmlrpc.client.ServerProxy('http://localhost:8000')
    res = s.parse(example)
    print(res)

    # Print list of available methods
    print(s.system.listMethods())


if __name__=="__main__":
    main("")
    for y in sys.argv[1:]:
        for x in glob.glob(y):
            main(x)

