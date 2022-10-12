import os

if __name__ == '__main__':

    version = '2'
    print(f"Input file: input{version}.txt, output file: output{version}.txt")
    os.system(f"python checkers.py ./checkers_validate/input{version}.txt ./checkers_validate/output{version}.txt")

    output_read = open(f"./checkers_validate/output{version}.txt", "r")
    solution_read = open(f"./checkers_validate/solution{version}.txt", "r")

    output_lines = output_read.readlines()
    solution_lines = solution_read.readlines()
    passed = True

    for index in range(1, len(output_lines)):
        if output_lines[index].strip() != solution_lines[index].strip():
            print(f"Line {index + 1}: "
                  f"Expected <{output_lines[index].strip()}> "
                  f"Encountered <{solution_lines[index].strip()}>\n")
            passed = False
            break

    print("Checkers output matches solution file.")
