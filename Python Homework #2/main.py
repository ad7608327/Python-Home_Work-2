"""
Home Work #2
it is about Functions

The Answers is:
Genre = jazz
year = 1962
Artist = jim hall
"""
# Genre Artist Year
def Genre():
    A="jazz"
    return A
def Artist():
    B="jim hall"
    return B
def Year():
    C="1962"
    return C
GEN, ART, YEAR = Genre(), Artist(), Year()
print("Note:* Dont Use Uppercase")
#SO I dont Want to to Make the Tradional Way So I think I can Make Something Else I hope you will Like it
A1=input("Can you Guess What is My Favorite Genre of Music? < ")
if A1 == GEN :
    print("Righ :0\n")
else:
    print("Ops :(\nThat is Rong\n")
    A2=input("Do you Want to try Again ? > ")
    if A2 =="yes":
        A1=input("Can you Guess What is My Favorite Genre of Music? < ")
        if A1 == GEN :
            print("Righ :0\n")
        else:
            print("Ops :(\nThat is Rong\n")
            A2=input("Do you Want to try Again ?")
            if A2 =="yes":
                A1=input("Can you Guess What is My Favorite Genre of Music? < ")
                if A1 == GEN :
                    print("Righ :0\n")
                else:
                    print("Ops :(\nThat is Rong\n")
                A2=input("Do you Want to try Again ?")
                if A2 =="yes":
                    A1=input("Can you Guess What is My Favorite Genre of Music? < ")
                    print("Righ :0\n")
                else:
                    print("Ops :(\nThat is Rong\n")
                    A2=input("Do you Want to try Again ?")
                    if A2 =="yes":
                        A1=input("Can you Guess What is My Favorite Genre of Music? < ")
                        if A1 == GEN :
                            print("Righ :0\n")
                        else:
                            print("Dont Hurt Your Brain it's Fine\n")
                            C99=input("Do you Want to Continue in Guessing? > ")
                            if C99 == "yes":
                                A1=input("Can you Guess What is Name of the Artist? < ")
                                if A1 == ART:
                                    print("Righ :0\n")
                                else:
                                    print("Ops :(\nThat is Rong\n")
                                    A2=input("Do you Want to try Again ?")
                                    if A2 =="yes":

                                        A1=input("Can you Guess What is Name of the Artist? < ")
                                        if A1== ART:
                                            print("Righ :0\n")
                                        else:
                                            print("Ops :(\nThat is Rong\n")
                                            A2=input("Do you Want to try Again ?")
                                            if A2 =="yes":

                                                A1=input("Can you Guess What is Name of the Artist? < ")
                                                if A1== ART:
                                                    print("Righ :0\n")
                                                else:
                                                    print("Ops :(\nThat is Rong\n")
                                                    print("Dont Hurt Your Brain it's Fine\n")
                                                    C89=input("Do you Want to Continue in Guessing? > ")
                                                    if C89 == "yes":
                                                        A1=input("Can you Guess The year of My Favorite Song ? > ")
                                                        if A1 == YEAR:
                                                            print("Righ :0\n")
                                                        else:
                                                            print("Ops :(\nThat is Rong\n")
                                                            A2=input("Do you Want to try Again ?")
                                                            if A2 == "yes":
                                                                A1=input("Can you Guess The year of My Favorite Song ? > ")
                                                                if A1 == YEAR:
                                                                    print("Righ :0\n")
                                                                else:
                                                                    print("Ops :(\nThat is Rong\n")
                                                                    A2=input("Do you Want to try Again ?")
                                                                    if A2 == "yes":
                                                                        A1=input("Can you Guess The year of My Favorite Song ? > ")
                                                                        if A1 == YEAR:
                                                                            print("Righ :0\n")
                                                                        else:
                                                                            print("it Rong\n Sorry :(\n")
                                                                            print("If you Cant Guess Any thing it's ok you Can Open the Script And Try Again\n Thaks For Playing With My Script")
