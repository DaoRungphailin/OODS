class translator:
    def deciToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]): # start with val[0] หารไม่เอาเศษไปเรื่อยๆ
                roman += syb[i]
                num -= val[i]
            i += 1
        return roman
       
    def romanToDeci(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            #print(num)
            if i+1<len(s) and s[i:i+2] in roman: #เช็ค2ตัวติดกันว่ามีใน list มั้ย
                
                num+=roman[s[i:i+2]]
                i+=2 #ข้ามไป 2 ตัว
            else: #เช็คตัวเดียว
                num+=roman[s[i]]
                i+=1
        return num       

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))