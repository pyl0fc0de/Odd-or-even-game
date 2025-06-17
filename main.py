
import random
def main():
    print("\tODD or EVEN GAME\n")
    print("Instructions : \n1.Enter your prediction(odd/even) in lowercase\n2.Press \"Enter\" key to roll dice")
    print("3.When sum of outcome is same as prediction you gain a point")
    print()
    score=0
    for i in range(5):
        sum=0
        p=input("Your Prediction  : ")
        c=input("Preparing to roll .......")
        while True:
            if(c==""):
                break
        a=random.randint(1,6)
        b=random.randint(1,6)
        print("Outcome of die 1 : ",a)
        print("Outcome of die 2 : ",b)
        sum=a+b
        print("Sum : ",sum)
        if((sum%2==0)and(p=="even")):
            score+=1
        elif((sum%2!=0)and(p=="odd")):
            score+=1
        else:
            score=score+0
            i+=1
        print("Score = ",score,"/5")
        print()
       
    print("Game Over.....")
if __name__ == "__main__":
    main()