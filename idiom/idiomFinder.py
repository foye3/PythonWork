import argparse
import json
import pinyin

PINYIN = False
TONE = False

def idiomFinder(first_character):
  with open('idiom_basic.json') as f:
    data = json.load(f)
  for idiom in data:
    if TONE:
      if idiom['pinyin'].split()[0] == pinyin.get(first_character):
        print(idiom['word'])
    elif PINYIN:
      if pinyin.get(idiom['word'][0],format="strip") == pinyin.get(first_character,format="strip"):
        print(idiom['word'])
    else:
      if idiom['word'][0] == first_character:
        print(idiom['word'])
  
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('first_character', help='find idioms by first character')
  parser.add_argument("-p", '--pinyin', help="find idioms by first character's pinyin", action="store_true")
  parser.add_argument("-t", '--tone', help="find idioms by first character's pinyin and tone", action="store_true")

  args = parser.parse_args()
  
  if args.pinyin:
    PINYIN = True
  
  if args.tone:
    TONE = True
    
  if args.first_character:
    idiomFinder(args.first_character)