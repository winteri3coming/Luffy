![alt text][image]

[image]: https://i.imgur.com/f0LoUeJ.png

# Luffy
Local File Inclusion hunting tool for bugbounty and penetration testing.

### Description
Luffy is a tool that helps find Local File Inclusion vulnerabilities, by providing a list of urls and endpoints.. Luffy combines them with a list of payloads from the 'payloads.txt' file, and then try all the possbile combinations including URI injected payloads or parameterized payloads.

#### Example
- **URL:** https://www.example.com/path1/path2/path3?search=lfi&exploit=vulnerable

Luffy is going to test for all these next combinations:

>`https://www.example.com/PAYLOAD`

>`https://www.example.com/path1/PAYLOAD`

>`https://www.example.com/path1/path2/PAYLOAD`

>`https://www.example.com/path1/path2/path3?search=PAYLOAD&exploit=vulnerable`

>`https://www.example.com/path1/path2/path3?search=lfi&exploit=PAYLOAD`


### Install
`git clone https://github.com/FrozenOption/Luffy`

`cd Luffy & pip3 install -r requirements.txt`

### Usage
`python3 luffy.py -f urls.txt -p payloads.txt`

**Note:** if -p is ommited, 'payloads.txt' file will be used by default.


![alt text][image2]

[image2]: https://i.imgur.com/ZSp7sgq.png


### To-Add
- Add header based LFI detection support.
- Add Threading methods to make it go faster.
- Server detection or add a flag to use only suitable payloads.
- WAF detection and bypass methods.
- When vulnerable url found. Add primary basic RCE methods.
