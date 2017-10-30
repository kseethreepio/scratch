TOP_NUM = 4000000

if __name__ == '__main__':
  current_term = None
  previous_term1 = None
  previous_term2 = None
  running_sequence = []
  running_term = 1
  running_sum = 0
  current_index = 0

  while running_term < TOP_NUM:
    try:
      previous_term1 = running_sequence[current_index - 1]
      previous_term2 = running_sequence[current_index - 2]
      new_term = previous_term1 + previous_term2
    except IndexError:
      if previous_term1:  # n = 2
        new_term = previous_term1 + 1  # Eh, not so elegant
      elif not previous_term1:  # n = 1
        new_term = running_term

    running_sequence.append(new_term)
    running_term = new_term

    if new_term % 2 == 0:
      running_sum += new_term

    current_index += 1
  
  print(running_sum)
