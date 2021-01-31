#!/usr/bin/python3

import sys, json

from pogodata import PogoData
help = 'pogodata-cli.py move|pokemon <name>'
outputText = ''

def main(argv):
   if len(argv) < 1 :
      print('null')
      sys.exit()
   if argv[0] == "moves":
      data = PogoData(language="english")
      print("[\n{}")
      for entry in data.moves:
        print("," + json.dumps(entry.raw))
      print("\n]\n")
   elif argv[0] in ("species", "pokemon"):
      data = PogoData(language="english")
      print("[\n{}")
      for entry in data.mons:
        print("," + json.dumps(entry.raw))
      print("\n]\n")
   else:
      print('null')
      sys.exit()
   sys.exit()

#    if len(argv) < 2 :
#       outputText = help
#    if argv[0] == "move":
#       data = PogoData(language="english")
#       outputText = data.get_move(name=argv[1]).raw.replace("'", '"')
#    elif argv[0] in ("species", "default_mon"):
#       data = PogoData(language="english")
#       outputText = data.get_default_mon(name=argv[1]).raw.replace("'", '"')
#    elif argv[0] in ("poke", "pokemon", "mon"):
#       data = PogoData(language="english")
#       outputText = data.get_mon(name=argv[1]).raw.replace("'", '"')
#    else:
#       outputText = help
#
#    print(outputText)
#    sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])
