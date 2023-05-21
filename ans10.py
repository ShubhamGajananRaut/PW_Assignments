# Q10. Given the string "Hello, World!", extract the substring "World".

test_string = "Hello, World!"

print(test_string[7:12])

substring = test_string.split(", ")[1]
final = substring[0:-1]
print(final)

