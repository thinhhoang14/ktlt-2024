print('hoàng đình thịnh msv 235752021610114')
def nhi_phan_sang_thap_phan(chuoi_nhap):
  danh_sach_nhi_phan = chuoi_nhap.split(',')

  print("Các số thập phân tương ứng là:")
  for so_nhi_phan in danh_sach_nhi_phan:
    so_thap_phan = int(so_nhi_phan, 2)
    print(so_thap_phan)
    
chuoi_nhap = input("Nhập chuỗi các số nhị phân (cách nhau bởi dấu phẩy): ")

nhi_phan_sang_thap_phan(chuoi_nhap)

