print('Enter a three-digit value: ')

usr_val         = int(input())                  #Ex. Enter 365 as your value.
ones_digit      = usr_val % 10
tmp_val         = usr_val // 10

print('The ones digit is \n' + str(ones_digit))  

tens_digit      = tmp_val % 10
tmp_val         = tmp_val // 10

print('The tens digit is \n' + str(tens_digit))

hundreds_digit  = tmp_val % 10

print('The hundreds digit is \n' + str(hundreds_digit))
