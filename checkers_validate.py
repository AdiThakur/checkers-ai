import os
import time

if __name__ == '__main__':

    passed = True

    for version in [0, 1, 2]:

        print(f"Input file: input{version}.txt, output file: output{version}.txt")
        start = time.time()
        os.system(f"python3 checkers.py ./checkers_validate/input{version}.txt ./checkers_validate/output{version}.txt")
        print(f"\tTook {time.time() - start} seconds")

        output_read = open(f"./checkers_validate/output{version}.txt", "r")
        solution_read = open(f"./checkers_validate/solution{version}.txt", "r")

        output_lines = output_read.readlines()
        solution_lines = solution_read.readlines()

        for index in range(1, len(output_lines)):
            if output_lines[index].strip() != solution_lines[index].strip():
                print(f"Line {index + 1}: "
                      f"Expected <{output_lines[index].strip()}> "
                      f"Encountered <{solution_lines[index].strip()}>\n")
                passed = False
                break

    if passed:
        print("Checkers output matches solution file.")
