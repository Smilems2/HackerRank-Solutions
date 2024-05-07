import textwrap

def wrap(string, max_width):
    i=0
    output=""
    while (i<=len(string)):
        output+= string[i:i+max_width]
        output+= "\n"
        i+=max_width
    return output
    
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)