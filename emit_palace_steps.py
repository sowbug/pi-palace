#!/usr/bin/python

from itertools import izip, islice

# 999 digits (multiple of 3)
# http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
PI=314159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019

f = open("pao-00-2014.tsv")
lines = f.readlines()
f.close()

PAO = {}

person_len_max = 0
action_len_max = 0
object_len_max = 0
print "KEY\n===\n"
for line in lines:
  line = line.strip()
  if not line or line.startswith("#") or line.startswith("Number"):
    continue
  try:
    (number, person, action, obj, mnemonic, category, reference) =\
      line.strip().split("\t")
  except ValueError:
    continue
  num_int = int(number)
  if num_int > 9:
    continue
  print number, person, action, obj, "(%s)" % mnemonic
  PAO[number] = { 'person': person,
                  'action': action,
                  'object': obj }
  if len(person) > person_len_max:
    person_len_max = len(person)
  if len(action) > action_len_max:
    action_len_max = len(action)
  if len(obj) > object_len_max:
    object_len_max = len(obj)

PAO['-'] = { 'person': 'nobody',
             'action': 'does nothing to',
             'object': 'nothing' }
MAX_PHRASE_LEN = person_len_max + action_len_max + object_len_max + 2

print


numstr = str(PI)
#print "\nmax phrase len:", MAX_PHRASE_LEN
print "Now generating mnemonics for %d digits..." % len(numstr)

while len(numstr) % 3 != 0:
  numstr += "-"

print "\n\nMEMORIZE THIS\n=============\n"

loci = 1
digits = 1
# http://stackoverflow.com/a/1162636/344467
for (d1, d2, d3) in izip(islice(numstr, 0, None, 3),
                         islice(numstr, 1, None, 3),
                         islice(numstr, 2, None, 3)):
  phrase = "%s %s %s" % (PAO[d1]['person'],
                         PAO[d2]['action'],
                         PAO[d3]['object'])
  phrase = "%58s" % phrase
  print "%3d %3d-%3d:" % (loci, digits, digits + 2), phrase, " => %s%s%s" % (d1,
                                                                             d2,
                                                                             d3)
  loci += 1
  digits += 3
