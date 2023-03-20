"""
l1 = ['a','e','v','j','a']

vowels_list = ['a','e','e','o','u']

l2 = []

def checkvowel():

    for c in l1:
        if c in vowels_list:
            l2.append(c)

checkvowel()

for i in l2:
    print(i)
"""
l1 =['English','Math','Java','Android','SS']

tops_subject = ['C','C++','Java','Android','Flutter']


def myfun(subject):
    if(subject in tops_subject):
        return True
    else:
        return False
    
filtered_data = filter(myfun,l1)

for i in filtered_data:
    print(i)
    













"""
l1 = ['a','e','v','j','a']

vowels_list = ['a','e','e','o','u']

def myfun(seq):
    if (seq in vowels_list):
        return True
    else:

        return False
    
filtered_data = filter(myfun,l1)

for i in filtered_data:
    print(i)
"""
"""
data_set = [12,23,45,6,4,78,5,3,33,67]

def myfun(data):
    if data %2==0:
        return True
    else:
        return False
    
    filtered_data = filter(myfun,data_set)

    for i in filtered_data:
        print(i)
"""
