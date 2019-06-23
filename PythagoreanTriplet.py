def PythagoreanTriplet(numbers):
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      for k in range(j+1, len(numbers)):
        if numbers[k]**2 == numbers[i]**2 + numbers[j]**2:
          return True
        continue
  
  return False;

def main():
  numbers = [1,2,3,4,5,6,7,8]
    
  print(PythagoreanTriplet(numbers))
  
if __name__ == '__main__':
  main()