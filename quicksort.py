from unicodedata import name
import numpy as np
import sys
 
def main(num_list):
    print(f"Your list has {len(num_list)} numbers.")

if __name__ == '__main__':
    n = len(sys.argv)
    print(f"{n} arguments passed")
    for i in range(len(sys.argv)):
        print(f"arg {i}: {sys.argv[i]}")
    num_list = sys.argv[1:]
    main(num_list)
