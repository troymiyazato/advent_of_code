def find_number_of_increase(filename):
  with open(filename, 'r') as file:
    prev_number = file[0]
    increases = 0
    for number in file[1:]:
      if number > prev_number:
        increases += 1
        prev_number = number
      
    print(increases)

        

find_number_of_increase("./day1_troy/troy_data.txt")