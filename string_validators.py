if __name__ == '__main__':
  string = input()

# Check for alphanumeric characters
  print(any(c.isalnum() for c in string))

# Check for alphabetical characters
  print(any(c.isalpha() for c in string))

# Check for digits
  print(any(c.isdigit() for c in string))

# Check for lowercase characters
  print(any(c.islower() for c in string))

# Check for uppercase characters
  print(any(c.isupper() for c in string))