
# Run and test
# python example-6-3-list-input.py < colors_input.txt

#reads colors from the user and appends to a list
#until the user presses the Enter key.
def main():
  colors = []
  #notice how we read one time outside the loop
  #check and then enter the loop
  aColor = input("Enter a color: ")
  while (aColor != ''):
    colors.append(aColor)
    aColor = input("Enter a color: ")

  print(colors)
  print("If you want it formatted better: ")
  printColors(colors)


def printColors(colors):
  for num in range(len(colors)-1):
    print(colors[num], ", ", sep = '', end = '')
  print(colors[num+1])

#call main
main()
