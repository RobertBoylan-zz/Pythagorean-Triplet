def PythagoreanTriplet(numbers):
  for i in range(len(numbers)):
    for j in range(len(numbers)):
      if i == j:
        continue
      for k in range(len(numbers)):
        if i == k or j == k:
          continue
		  
        if numbers[k]**2 == numbers[i]**2 + numbers[j]**2:
          return True
  
  return False;

def main():
  numbers = [1,2,3,4,5,6,7,8]
    
  print(PythagoreanTriplet(numbers))
  
if __name__ == '__main__':
  main()
