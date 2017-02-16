'''
The Paideia Institute for Humanistic Study
written and tested Python 3.5.2
02.16.2017 by Lachlan Kermode (github 'breezykermo')
----------------------------------------------------
Note how to generate different outputs modifying the header params.
'''
import csv
import sys
from random import shuffle

# 6 sessions in total
# 3 latin sessions sat, 13 groups for three sessions of no more than 12
# 3 latin sessions sun, 12 groups.

# 4 greek groups, 2 beginner, and 2 intermediate/advanced.

len_args = len(sys.argv)
assert (len_args == 3), "\n\nYou need exactly 2 arguments: you have "+str(len_args)+"." \
  + "\n python process.py no_of_groups lang"


# HEADER PARAMS
# -------------
levels = ['None', 'Beginner', 'Intermediate', 'Advanced']
latinSkill = 'Experience with Spoken Latin'
greekSkill = 'Knowledge of Ancient Greek'

INPUT_FILENAME = 'data2017.csv'
OUTPUT_FILENAME = 'partitioned.csv'
NO_OF_GROUPS = int(sys.argv[1])
LANGUAGE = sys.argv[2]

# print(type(NO_OF_GROUPS))
assert (type(NO_OF_GROUPS)), "1st argument needs to be an integer."
print(LANGUAGE)
assert (LANGUAGE == 'greek' or LANGUAGE == 'latin') , "2nd argument needs to be 'greek' or 'latin'."
# -------------

latin = {
  'beginner': [],
  'intermediate': [],
  'advanced': [],
  'other': []
}

# process a list into into GROUP_NO subsets
# chunks: 'a list -> int -> 'a list list
def chunks_of(l, n=NO_OF_GROUPS):
  return [l[i:i + n] for i in range(0, len(l), n)]

def chunks(l, n=NO_OF_GROUPS):
  return  [l[i:i+(len(l)//n)] for i in range(n)]

# read from csv
key_fields = []
empty_person = {}
with open(INPUT_FILENAME, 'r') as f:
  data = csv.DictReader(f)
  # separate into classes
  for person in data:
    key_fields = person.keys()
    if person[latinSkill] == levels[1]:
      latin['beginner'].append(person)
    elif person[latinSkill] == levels[2]:
      latin['intermediate'].append(person)
    elif person[latinSkill] == levels[3]:
      latin['advanced'].append(person)
    else:
      print("Someone's data was corrupted; check other")
      latin['other'].append(person)
  # process a skill into into GROUP_NO 

with open(OUTPUT_FILENAME, 'w') as f:
  writer = csv.DictWriter(f,fieldnames=key_fields)
  # partition
  # print(len(latin['beginner']))
  groups = chunks(latin['beginner'])
  print(len(groups[0]))
  # print(groups)
  for group in groups:
    # print(len(group))
    for person in group:
      writer.writerow(person)
    # writer.writerow(empty_person)
  


# TESTING
# --------
# ts = map(lambda x: x[latinSkill], latin['beginner'])
# for t in ts:
#   print(t)
