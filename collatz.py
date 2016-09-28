def collatz(no):
    if no%2 == 0:
        no = no // 2
        return no
    elif no%2 == 1:
        no = 3 * no + 1
        return no
    else:
        print("enter valid no")
def enter():
    print("enter your no")
    value = input()
    print(int(value))
    no = value
    while no != 1:
        no = collatz(no)
        print(str(no))
enter()
