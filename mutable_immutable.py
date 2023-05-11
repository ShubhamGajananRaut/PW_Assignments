# immutable example
a = 5
b = "hello"
c = (1, 2, 3)

# trying to modify an immutable type raises an error
a += 1 # raises TypeError
b += " world" # raises TypeError
c[0] = 4 # raises TypeError


# mutable example
my_list = [1, 2, 3]
my_dict = {'key': 'value'}
my_set = {1, 2, 3}

# modifying a mutable type is allowed
my_list.append(4) # [1, 2, 3, 4]
my_dict['new_key'] = 'new_value' # {'key': 'value', 'new_key': 'new_value'}
my_set.add(4) # {1, 2, 3, 4}