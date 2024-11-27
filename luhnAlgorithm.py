def card_number_checker(card_number):
  '''Checks the validity of Credit card number, Debit card number, IMEI number, etc.'''
  translation = str.maketrans({'-':'',' ':''})
  card_number_translated = card_number.translate(translation)
  # for odd index digits 
  sum_of_odd_index_digits = 0
  
  # Lets reverse the number to access right most number first 
  card_number_reversed = card_number_translated[::-1]  
  # print(card_number_reversed)
  # Lets separate every odd index digit from card number
  odd_index_digits = card_number_reversed[::2]
  # print(odd_index_digits)
  for digit in odd_index_digits:
    sum_of_odd_index_digits += int(digit)
  # print(sum_of_odd_index_digits)

  # For even
  sum_of_even_index_digits = 0
  even_index_digit = card_number_reversed[1::2]
  # print(even_index_digit)
  for digit in even_index_digit:
    number = int(digit)*2
    if number >= 10:
      number = (number // 10) + (number % 10)
    sum_of_even_index_digits += number
  
  total_sum = sum_of_even_index_digits+sum_of_odd_index_digits
  return total_sum % 10 
  
def main():
  card_number = '4111-1111-4555-1142'
  
  
  if card_number_checker(card_number=card_number) == 0:
    print("The Card number is Valid!")
  
  else:
    print("The card number is Invalid!")

main()