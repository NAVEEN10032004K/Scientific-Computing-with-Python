def case_converter(pascal_or_camel_case_string):
  result_string_list = ['_'+ char.lower()
                   if char.isupper()
                   else char 
                   for char in pascal_or_camel_case_string ]
  result_string = ''.join(result_string_list).strip('_')
  return result_string

def main():
  print("camelCase/PascalCase to snake_case converter.")
  string = input("Enter your string in camel case or pascal case: ")
  print(case_converter(string))

main()
