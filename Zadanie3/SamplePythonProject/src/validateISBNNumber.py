class validateISBNNumber:
    def validate(num):
        isbnNumber = num.replace("-","")
        if len(isbnNumber) != 13:
            return False
        else:
            suma = 0
            for i in range(len(isbnNumber)):
                if (i+1)%2!=0:
                    suma += int(isbnNumber[i])*1
                else:
                    suma += int(isbnNumber[i])*3
            return suma%10 == 0
