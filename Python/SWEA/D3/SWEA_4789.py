for t in range(1,int(input())+1):

    applauses = input()
    people = int(applauses[0])
    people_need = 0
    for idx, applause in enumerate(applauses[1:],1):
        if people < idx:
            people_need+=idx-people
            people+=int(applause)+idx-people
        else:
            people+=int(applause)

    print(f'#{t} {people_need}')

