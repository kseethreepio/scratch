# Re-writing my sol'n for this one since I overwrote my initial one

TOP_NUM = 1000

if __name__ == '__main__':
  running_sum = 0

  for num in xrange(0, TOP_NUM):  # Going w/ISO_80000-2
    if (num % 3 == 0) or (num % 5 == 0):
      running_sum += num

  print("Final sum of multiples of 3 & 5: %d" % running_sum)
