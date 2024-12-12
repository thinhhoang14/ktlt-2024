print('hoàng đình thịnh msv 235752021610114')
def pascal_triangle(n):

  triangle = [[1]]
  for i in range(1, n):
    row = [1]
    for j in range(1, i):
      row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)
    triangle.append(row)
  return triangle

def print_pascal_triangle(n):


  triangle = pascal_triangle(n)
  for row in triangle:
    print(' '.join(map(str, row)))

n = int(input("Nhập số hàng của tam giác Pascal: "))

print_pascal_triangle(n)
