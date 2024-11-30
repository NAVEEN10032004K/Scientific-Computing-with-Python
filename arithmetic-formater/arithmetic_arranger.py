# To run tests the functions must have return statements for every test cases.
def arithmetic_arranger(problems, show_answer=False):
  
  if len(problems) > 5:
      return(f"Error: Too many problems.")

  first_operand = []
  second_operand = []
  operator = []

  for problem in problems:
    components = problem.split()  # Split function give you the list of all the componets in a string separated by " " by default 
    first_operand.append(components[0])
    second_operand.append(components[2])
    operator.append(components[1])

  if '*' in operator or '/' in operator:
     return (f"Error: Operator must be '+' or '-'.")

  for i in range(len(first_operand)):
     if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
        return (f"Error: Numbers must only contain digits.")

  for i in range(len(first_operand)):
     if len(first_operand[i]) > 4 or len(second_operand[i]) > 4 :
        return (f"Error: Numbers cannot be more than four digits.")
     
  first_line = []
  second_line = []
  third_line = []
  fourth_line = []

  for i in range(len(first_operand)):
     if len(first_operand[i]) > len(second_operand[i]):
        first_line.append(" "*2 + first_operand[i])
     else :
        first_line.append(" " * (len(second_operand[i]) - len(first_operand[i]) + 2 ) + first_operand[i])
  for i in range(len(second_operand)):
     if len(second_operand[i]) > len(first_operand[i]):
        second_line.append(operator[i]+ " " + second_operand[i])
     else:
        second_line.append(operator[i] + " "*(len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

  for i in range(len(first_line)):
      third_line.append("-" * (max(len(first_operand[i]), len(second_operand[i])) + 2)) 

  if show_answer:
     for i in range(len(first_operand)):
        if operator[i] == "+":
           answer = str(int(first_operand[i]) + int(second_operand[i]))
        else:
           answer = str(int(first_operand[i]) - int(second_operand[i]))
        
        if len(answer) > max(len(first_operand[i]), len(second_operand[i])):
           fourth_line.append(" " + answer)
        else:
           fourth_line.append(" " * (max(len(first_operand[i]), len(second_operand[i])) - len(answer) + 2 )+ answer)
      
     arranged_problem = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
  else:
     arranged_problem = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
   
  return arranged_problem
       
# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))


