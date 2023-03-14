import random
letter_table={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
        'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
        'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
for j in range(20):
    letter=random.choice(list(letter_table.keys()))
    letter_num=letter_table[letter] #type:int
    letter_num_array=list(str(letter_num)) #int > str > list > int
    letter_num_tens=int(letter_num_array[0])
    letter_num_units=int(letter_num_array[1])

    sex=random.choice([1,2])

    id_str=""
    check_sum=list()
    for i in range(7):
        id_num=random.randint(0,9) #是9非10
        id_str=id_str+str(id_num)
        check_sum.append(id_num*(7-i))

    check_num=10-((letter_num_tens+letter_num_units*9+sex*8+sum(check_sum))%10)
    if (letter_num_tens+letter_num_units*9+sex*8+sum(check_sum))%10==0:
        check_num=0
        
    id=str(letter)+str(sex)+str(id_str)+str(check_num)
    print(id)
