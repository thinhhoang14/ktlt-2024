print('hoàng đình thịnh msv 235752021610114')
def find_odd_numbers(input_numbers):

  odd_numbers = [num for num in input_numbers if num % 2 != 0]
  return odd_numbers

input_string = input("Nhập danh sách các số, phân cách bởi dấu phẩy: ")

numbers = [int(num) for num in input_string.split(',')]

odd_numbers = find_odd_numbers(numbers)

print(", ".join(map(str, odd_numbers)))
