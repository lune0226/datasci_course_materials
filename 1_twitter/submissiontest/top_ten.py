import sys
import json


def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    lines = tweet_file.readlines()

    hashtagsdict = {}
    for (i, line) in enumerate(lines):
      obj = json.loads(line)
      if "text" in obj and "lang" in obj:
        if obj["lang"] != "en": continue
        hashtags = obj[u"entities"][u"hashtags"]
        for h in hashtags:
          hashtagsdict.setdefault(h["text"], 0)
          hashtagsdict[h["text"]] += 1
      


    toptags = sorted(hashtagsdict.items(), key=lambda kv: kv[1], reverse=True)
    for k, v in toptags[0:10]:
      print k

if __name__ == '__main__':
    main()
