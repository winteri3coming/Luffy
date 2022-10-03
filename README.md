# Luffy
Local File Inclusion hunting tool

## Description
Luffy is a tool that helps find Local File Inclusion vulnerabilities, by providing a list of urls and endpoints.. Luffy combines them with a list of payloads from the 'payloads.txt' file, and then try all the possbile combinations including URI injected payloads or parameterized payloads.

### Example
url: https://www.example.com/path1/path2/path3?search=lfi&exploit=vulnerable
Luffy is going to test for all these next combinations:
`
https://www.example.com/PAYLOAD
https://www.example.com/path1/PAYLOAD
https://www.example.com/path1/path2/PAYLOAD
https://www.example.com/path1/path2/path3?search=PAYLOAD&exploit=vulnerable
https://www.example.com/path1/path2/path3?search=lfi&exploit=PAYLOAD`

## Install
`git clone https://github.com/FrozenOption/Luffy`
`cd Luffy & pip3 install -r requirements.txt`

## Usage
`python3 luffy.py -f urls.txt -p payloads.txt`
#### Note: if -p is ommited, 'payloads.txt' file will be used by default.
