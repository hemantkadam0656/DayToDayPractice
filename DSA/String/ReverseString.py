def ReverseString(string):
   newstring = ' '.join(string.split()[::-1])
   print(newstring)
  

if __name__ == '__main__':
    string = "    the pen "
    res = ReverseString(string)

    