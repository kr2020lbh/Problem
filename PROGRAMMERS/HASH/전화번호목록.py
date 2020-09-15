def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    for i in range(len(phone_book)-1):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False
    return True

phone_book = ['119','1111','11', '97674223', '195524421']
print(solution(phone_book))