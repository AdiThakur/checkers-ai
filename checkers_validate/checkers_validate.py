import os

if __name__ == '__main__':

    print("Input file: input0.txt, output file: output0.txt")
    os.system("python3 ../checkers.py input0.txt output0.txt")

    output_read = open("output0.txt", "r")
    solution_read = open("solution0.txt", "r")

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
