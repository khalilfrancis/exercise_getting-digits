print('Enter a three-digit value: ')

usr_val         = int(input())                  
ones_digit      = usr_val % 10                  # Ex: 365 % 10 is 5.
tmp_val         = usr_val // 10

print('The ones digit is\n' + str(ones_digit))  

tens_digit      = tmp_val % 10                  # Ex: tmp_val = 365 // 10 is 36. Then 36 % 10 is 6.
tmp_val         = tmp_val // 10

print('The tens digit is\n' + str(tens_digit))

hundreds_digit  = tmp_val % 10                  # Ex: tmp_val = 36 // 10 = 3. Then 3 % 10 is 3.

print('The hundreds digit is\n' + str(hundreds_digit))
