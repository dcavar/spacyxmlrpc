# spaCy XML-RPC example

(C) 2017 by [Damir Cavar]


This [spaCy] XML-RPC example shows how you can fire up a [spaCy] server and communicate with it using
[XML-RPC in Python].

The initialization of [spaCy] could be slow and not practicle for processing of big data and large text collections.


## Command Line

Start the server using the command line:

    python spacyRPCServer.py

The default parameters are:

- port: 8000
- hostname: localhost
- language: en

Use for *--help* option for details:

    python spacyRPCServer.py --help



## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



[spaCy]: https://spacy.io/ "spaCy"
[XML-RPC in Python]: https://docs.python.org/3/library/xmlrpc.html "Python 3 XML-RPC"
[Damir Cavar]: http://damir.cavar.me/ "Damir Cavar homepage"
