'''
รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

- หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

- หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"

- หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''
def drome(lst):
    maxtoMin = True
    minToMax = True
    unique = True
    same = True
    temp = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            maxtoMin = False
        if lst[i] > lst[i+1]:
            minToMax = False
        if lst[i] in temp:
            unique =False
        if lst[i] != lst[i+1]:
            same = False
        temp.append(lst[i])
    if lst[len(lst)-1] in temp:
        unique = False

    if same:
        return "Repdrome"
    elif minToMax and unique:
        return "Metadrome"
    elif minToMax and not unique:
        return "Plaindrome"
    elif maxtoMin and unique:
        return "Katadrome"
    elif maxtoMin and not unique:
        return "Nialpdrome"
    else:
        return "Nondrome"

in_lst = list(map(int, input("Enter Input : ")))
print(drome(in_lst))