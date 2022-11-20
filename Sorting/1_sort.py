'''
ให้น้องๆทำการตรวจสอบว่า input ที่เราใส่ลงไปนั้นได้มีการเรียงลำดับมาแล้วหรือไม่ ถ้าหากเรียงมาแล้วให้แสดงผลเป็น Yes แต่ถ้าหากไม่ให้แสดงผลเป็น No

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''
def sort(lis):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if j+1 < len(lis) and lis[j]>lis[j+1]:
                temp=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=temp
inp=[int(e) for e in input('Enter Input : ').split()]
trySort = inp.copy()
sort(trySort)
if inp == trySort:
    print('Yes')
else :
    print('No')