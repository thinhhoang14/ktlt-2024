print('hoàng đình thịnh msv 235752021610114')
def count_upper_and_lower(input_string):

  upper_case = sum(1 for c in input_string if c.isupper())
  lower_case = sum(1 for c in input_string if c.islower())
  return upper_case, lower_case

input_string = input("Nhập câu của bạn: ")

upper_case, lower_case = count_upper_and_lower(input_string)

print(f"Số chữ hoa: {upper_case}")
print(f"Số chữ thường: {lower_case}")
