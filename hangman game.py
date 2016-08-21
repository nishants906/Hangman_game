import random
print("\t\t\t\t\tGAME BEGINS\n")
word=["andrapradesh","arunachalpradesh","assam","bihar","chhattisgarh","goa","gujarat","haryana","himachalpradesh","jammuandkashmir","jharkhand","karnataka","kerala","madhyapradesh","maharashtra","manipur","meghalaya","mizoram","nagaland","orissa","punjab","rajasthan","sikkim","tamilnadu","tripura","telangana","uttaranchal","uttarpradesh","westbengal"]

a='y'

while a=='y':
    e=0
    b=random.randint(0,28)
    c=len(word[b])
    print("enter the name of state starting with",word[b][0],"and having length =",c)
    d=raw_input("enter the name of state :")
    for i in range(c-1):
        if (word[b][i]==d[i]):
            e+=1
        else:
            print("sorry! u guess it wrong")
            break

    if (e==(c-1)):
        print("hurray! you done it")
            
    f=raw_input("want to try aain(y/n)")
    if f=='y':
        a='y'
        print("\n")
    else:
        break
    
