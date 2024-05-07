def print_formatted(number):
    # your code goes here
    w=len(bin(number)[2:])
    for i in range (1,number+1):
        decimal=str(i) 
        octal=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        binary=bin(i)[2:]
        print(decimal.rjust(w), octal.rjust(w), hexa.rjust(w), binary.rjust(w))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)