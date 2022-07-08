def find_number_of_increase(filename):
  with open(filename, 'r') as file:
    for line in file:
      print(line.rstrip())

find_number_of_increase("./day1/data.txt")