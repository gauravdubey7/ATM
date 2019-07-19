input("Welcome to 'AXIS BANK ATM'. Press 'ENTER' to continue. ")
input("Swipe your card. Press 'ENTER'. ")
option = ['Balance enquiry','Withdraw money','Quit']
pin_no = 1000
pin_no = input("'ENTER' your pin to proceed:")
try:
  if pin_no = 1000:
    print('Type your option from the following:')
    print('1.Balance enquiry')
    print('2.Withdraw money')
    print('3.Quit')
except Exception:
  print('You entered the wrong pin.Try again!')
  
opt = input('Type your option here:')
if opt == 'Balance enquiry':
  slip = input('Do you want slip?')
  if slip == 'Yes':
    print('Here is your slip!')
  else:
    print('Thanks for using AXIS BANK ATM. ')
elif opt == 'Withdraw money':
  amount = input('Enter your amount to proceed:')
  if amount>0:
    print('Collect your cash,Thanks!')
  else:
    print('Enter valid amount to proceed.')
elif opt == 'Quit':
  quit = input("Type 'Yes' to quit:")
  if quit == 'Yes':
    print('You have quit, Thanks!')
  else:
    print('Choose any transaction please!')

  
