print ('program mencari angka terbesar')
print('***********************************')
print()
n = int(input('masukan jumlah elemen'))
print()
print('masukan',n,'angka,kemudian enter:')

#simpan setiap angka yang diinput dalam 
x= []
for i in range(n):
    print('angka ke-',i+1,':',sep="end=")
    x.append(int(input()))
    print()

#proses mencari nilai terbesar 
max_num  = x[0];
for i in range(1,n):
  if(x[i]>max_num):
   max_num = x[i];
print('angka terbesar adalah:',max_num);