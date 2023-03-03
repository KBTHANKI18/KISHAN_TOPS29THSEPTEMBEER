quiz = {
    1 :{
        "que":"most popular programming language",
        "ans":"python"

    },
    2 :{
        "que":"prime minister of india",
        "ans":"narendra modi"
    }
}

for i in range(1,len(quiz)+1):
    print(quiz[i]["que"])
    ans = input("Enter Ans : ")
    if ans == quiz[i]["ans"]:
        print("Right Answer")
    else:
        print("Wrong Answer")
            

