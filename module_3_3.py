def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [55, 'Aspire', False]
values_dict = {'a': 6.378, 'b': 'Aluminium', 'c': None}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['NVIDIA', 987]
print_params(*values_list_2, c=42)
