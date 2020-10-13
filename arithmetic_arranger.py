def arithmetic_arranger(problems, to_solve = False):
    if len(problems) > 5:
        return "Error: Too many problems."

  #definition of variables
    number1 = ""
    sumorres = ""
    number2 = ""
    spaces = "    "
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
  #strip
    for problem in problems:
        splitted = problem.split(" ")
        if len(splitted[0]) > 4 or len(splitted[2]) > 4 :
            return "Error: Numbers cannot be more than four digits."
        width = max(len(splitted[0]), len(splitted[2]))
        if not splitted[0].isnumeric():
            return "Error: Numbers must only contain digits."
        if not splitted[2].isnumeric():
            return "Error: Numbers must only contain digits."
        number1 = int(splitted[0].rstrip())
        sumorres = splitted[1].rstrip()
        number2 = int(splitted[2].rstrip())

        if sumorres == '+':
            result = number1 + number2
        elif sumorres == '-':
            result = number1 - number2
        else:
            return "Error: Operator must be '+' or '-'."

        line1 = line1 + (str(number1)).rjust(width + 2) + spaces
        line2 = line2 + str(sumorres) + " " + (str(number2)).rjust(width) + spaces
        line3 = line3 + ("-"*(width + 2)).rjust(width) + spaces
        line4 = line4 + (str(result).rjust(width + 2)) + spaces

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    if to_solve :
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()

    return arranged_problems
