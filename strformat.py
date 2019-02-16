# fn = input('First name: ')
# ln = input('Last name: ')
fn = "Davis"
ln "Hong"
msg = 'Your name is %s %s' % (fn, ln)
print(msg)
msg = "Your name is {firstname} {lastname}".format (firstname = fn, lastname = ln)
print(msg)
print(f'Your first name is {fn} and \nyour last name is {ln}')
from string import Template
msg = Template('Your name is $fn $ln.')
print(msg.substitute(fn=fn, ln=ln))
# Printing 2 list elements concurrently
a = ["a","b","c"]
b = [1,2,3]
for i, j in zip(a,b):
    print(f'List a is {i} and list b i {j}')
