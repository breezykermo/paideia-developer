'''
The Paideia Institute for Humanistic Study
written and tested Python 3.5.2
02.16.2017 by Lachlan Kermode (github 'breezykermo')
----------------------------------------------------
Note how to generate different outputs modifying the header params.
'''
import csv
import sys
import math
from random import shuffle

# 6 sessions in total
# 3 latin sessions sat, 13 groups for three sessions of no more than 12
# 3 latin sessions sun, 12 groups.

# 4 greek groups, 2 beginner, and 2 intermediate/advanced.

len_args = len(sys.argv)
assert (len_args == 4), "\n\nYou need exactly 3 arguments: you have "+str(len_args)+"." \
  + "\n python process.py no_of_groups lang outfile.csv"


# HEADER PARAMS
# -------------
levels = ['Beginner', 'Intermediate', 'Advanced']
latinSkill = 'Experience with Spoken Latin'
greekSkill = 'Knowledge of Ancient Greek'

INPUT_FILENAME = 'data2017.csv'
OUTPUT_FILENAME = sys.argv[3]
NO_OF_GROUPS = int(sys.argv[1])
LANGUAGE = sys.argv[2]


assert (type(NO_OF_GROUPS)), "1st argument needs to be an integer."
assert (LANGUAGE == 'greek' or LANGUAGE == 'latin') , "2nd argument needs to be 'greek' or 'latin'."
# -------------

# intermediate data structure to store categorized persons
# categories: 'a Categories
categories = {
  'beginner': [],
  'intermediate': [],
  'advanced': [],
  'other': []
}

# process a list into subsets of n items
# chunks_of: 'a list -> int -> 'a list list
def chunks_of(l, n):
  return [l[i:i + n] for i in range(0, len(l), n)]

# process a list into n subsets
# chunks: 'a list -> int -> 'a list list
def chunks(l, n):
  return  [l[i:i+(len(l)//n)] for i in range(n)]

# generate n categorized chunks from intermediate data structure
# split_by_category: 'a Categories -> 'a list list
def split_by_category(cgs):
  full = cgs['beginner'] + cgs['intermediate'] + cgs['advanced']
  group_threshold = int(math.ceil(len(full) / NO_OF_GROUPS))
  output = []
  for level in cgs:
    shuffle(cgs[level])
    for chunk in chunks_of(cgs[level], group_threshold):
      output.append(chunk)
  return output


# read from csv
key_fields = []
# configure skill as latin or greek field
skill = latinSkill if (LANGUAGE == 'latin') else greekSkill

# separate input into classes
with open(INPUT_FILENAME, 'r') as f:
  data = csv.DictReader(f)
  key_fields = data.fieldnames
  for person in data:
    if person[skill] == levels[0]:
      categories['beginner'].append(person)
    elif person[skill] == levels[1]:
      categories['intermediate'].append(person)
    elif person[skill] == levels[2]:
      categories['advanced'].append(person)
    else:
      categories['other'].append(person)

# write chunks to specified output
with open(OUTPUT_FILENAME, 'w') as f:
  writer = csv.DictWriter(f,fieldnames=key_fields)
  # partition
  # print(len(categories['beginner']))
  # groups = chunks(categories['beginner'])
  # print(len(groups[0]))
  # # print(groups)
  # for group in groups:
  #   # print(len(group))
  #   for person in group:
  #     writer.writerow(person)
  #   writer.writerow({})
  for group in split_by_category(categories):
    for person in group:
      writer.writerow(person)
    writer.writerow({})
  
print('Successfully generated '+OUTPUT_FILENAME)


# TESTING
# --------
# ts = map(lambda x: x[latinSkill], latin['beginner'])
# for t in ts:
#   print(t)
