print('hoàng đình thịnh msv 235752021610114')
def check_divisible_by_5(binary_string):

  decimal_num = int(binary_string, 2)
  return decimal_num % 5 == 0

def find_divisible_by_5(binary_numbers):
    
  numbers = binary_numbers.split(',')
  result = []
  for num in numbers:
    if check_divisible_by_5(num):
      result.append(num)
  return ','.join(result)

binary_input = input("Nhập chuỗi các số nhị phân (cách nhau bởi dấu phẩy): ")

result = find_divisible_by_5(binary_input)
print("Các số chia hết cho 5:", result)

