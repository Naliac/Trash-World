#! python 3

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1


try:
    num = int(input("Enter number: "))
    num = collatz(num)

    while num == 0:         #Only if the user insists of
        print('Fuck off')   #being a little shit.
        num = num + 1             
        
    while num != 1:
       num = collatz(num)
except ValueError:
    print('This is da cool numbahs club no letters allowed!')
