def add_expences(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
      print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)



def main():
    expenses = []
    while True:
      print('\nExpense Tracker')
      print('1. Add an expense')
      print('2. List all expenses')
      print('3. Show total expenses')
      print('4. Filter expenses by category')
      print('5. Exit')

      choice = input("Enter you choice: ")
      if choice == '1':
         amount = float(input("Enter the amount: "))
         category = input("Enter the category: ")
         add_expences(expenses=expenses, amount=amount, category=category)
      
      elif choice == '2':
         print_expenses(expenses=expenses)
      
      elif choice == '3':
         print(total_expenses(expenses=expenses))
        
      elif choice == '4':
          category = input("Enter the category: ")
          expenses_by_category = list(filter_expenses_by_category(expenses, category))
          print(expenses_by_category[0])
      
      elif choice == '5':
         break
      
main()
