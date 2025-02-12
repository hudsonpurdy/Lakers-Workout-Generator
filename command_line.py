#!/usr/bin/env python3

"""
Implementation of basic command line interface.
Functionality includes:
- Getting help using the CLI
- Searching for exercises by muscle group
- Searching for exercises by equipment used
"""

import sys
from ProductionCode.datasource import DataSource
import pandas as pd


def main():
  data = DataSource()
  
  if len(sys.argv) >= 2 and sys.argv[1] == "--help":
    print()
    print("--musclegroup (--m) for all exercises using input muscle, eg. Lats, Lower-Back")
    print("--equipment (--e) for all exercises using input equipment, eg. Barbell, Dumbbell")
    print("Words should be separated with a hyphen '-'")
    print()

  elif len(sys.argv)==3:
    
    if sys.argv[1] == "--musclegroup" or sys.argv[1]=="--m":
      # Since muscle groups are sometimes multiple words, we will have the user separate words with hyphens
      print()
      print(list(data.getExerciseByMuscle(sys.argv[2].replace("-"," "))))
      print()
    
    elif sys.argv[1] == "--equipment" or sys.argv[1]=="--e":
      # Since equipments sometimes have multiple words, we will have the user separate words with hyphens
      print()
      print(list(data.getExerciseByEquipment(sys.argv[2].replace("-"," "))))
      print()

    else:
      print()
      print("Error: invalid command")
      print("--help for list of commands")
      print()
  
  elif len(sys.argv)<=2: # Want to print usage statement as the default
      print()
      print("Error: invalid input")
      print("--help to get help/command reminders")
      print("--musclegroup (--m) for all exercises using input muscle, eg. Lats, Lower-Back")
      print("--equipment (--e) for all exercises using input equipment, eg. Barbell, Dumbbell")
      print("Words should be separated with a hyphen '-'")
      print()

  else: # Remind the user to separate words with hyphens
    print()
    print("Reminder: words should be separated with a hyphen '-'")
    print()

if __name__=='__main__':
  main()
