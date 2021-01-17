

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client
import datetime


def getdate():
    import datetime
    return datetime.datetime.now()


def gettime():
    return datetime.datetime.now()


choseLogOrRead = int(input("1 for Log And 2 For read\n"))


def take(k):
    #for File Create
    if k == 1:
        choseName = int(input("1 for harry 2 for rahon and 3 for hamid\n"))
        if choseName == 1:
            hexa = int(
                input("What You Went To log Food Or Exasise 1for food and 2 for food\n"))
            if hexa == 1:
                with open("harry_exasises.txt", "a")as f:
                    harry_exasisesinput = input("What You Went To Exasises\n")
                    f.write(str([str(gettime())])+":"+harry_exasisesinput+"\n")
                    print("sussedfull log Harry Exasise")
            elif hexa == 2:
                with open("harry_food_list.txt", "a")as f:
                    harry_food_input = input("Enret What you Eat\n")
                    f.write(str([str(gettime())])+":"+harry_food_input+"\n")
                    print("sussedFully Log Harry Food")

            else:
                print("Please Enter Valid Number\n")

        elif choseName == 2:
            rohanChose = int(input("1 for Exasise And 2 for Food\n"))
            if rohanChose == 1:
                with open("Rohan_exasies_list.txt", "a")as f:
                    rohan_eaxasise_input = input("What Rohan Exasise\n")
                    f.write(str([str(gettime())])+":" +
                            rohan_eaxasise_input+"\n")
                    print("succedfully Rohan_exasies_list log")
            elif rohanChose == 2:
                with open("Rohan_food_list.txt", "a")as f:
                    rohan_food_input = input("What Rohan food\n")
                    f.write(str([str(gettime())])+":"+rohan_food_input+"\n")
                    print("succedfully Rohan_food_list log")
            else:
                print("please Enter Valid Number")
        elif choseName == 3:
            hammadChose = int(input("1 For Exasise And 2 For Food"))
            if hammadChose == 1:
                with open("hammad_exasies_list.txt", "a")as f:
                    hammad_eaxasise_input = input("What hammad Exasise\n")
                    f.write(str([str(gettime())])+":" +
                            hammad_eaxasise_input+"\n")
                    print("succedfully hammad_exasies_list log")
            elif hammadChose == 2:
                with open("hammad_food_list.txt", "a")as f:
                    hammad_food_input = input("What hammad eat \n")
                    f.write(str([str(gettime())])+":" +
                            hammad_food_input+"\n")
                    print("succedfully hammad_food_list log")
            else:
                print("Please Enter Valid Number")


        else:
            print("Please Chose A Valid NAme")



                #For File Read 
    elif k == 2: #k== 2 Mens read The File
        readinp = int(
            input("1 for harry File 2 for Rohan File and 3 for Hammad\n"))



        #read Harry File
        if readinp == 1:
            read_chose_file = int(
                input("1 For Exasise File And 2 For Food File\n"))

                #read Harry Exsise File
            if read_chose_file == 1:
                with open("harry_exasises.txt", "r") as f:
                    # print(f.readlines())
                    lines = f.readlines()
                    # print(lines)
                    for line in lines:
                        print(line, end="")


                #read Harry Food FIle
            elif read_chose_file == 2:
                with open("harry_food_list.txt", "r") as f:
                    # print(f.readlines())
                    lines = f.readlines()
                    # print(lines)
                    for line in lines:
                        print(line, end="")
            else:
                print("pLease Enter Valid number")






        #read Rohan File
        elif readinp==2:

            # print("this is rohan")
            rohan_read_chose_file = int(
                input("1 For Exasise File And 2 For Food File\n"))

                #read Rohan Exasise file
            if rohan_read_chose_file == 1:
                with open("Rohan_exasies_list.txt", "r") as f:
                    # print(f.readlines())
                    lineso = f.readlines()
                    # print(lines)
                    for lineii in lineso:
                        print("Rohan Exasises")
                        print(lineii, end="")


                #read Rohan Food File
            elif rohan_read_chose_file == 2:
                with open("Rohan_food_list.txt", "r") as f:
                    # print(f.readlines())
                    lines = f.readlines()
                    # print(lines)
                    for line in lines:
                        print("Rohan Food List")
                        print(line, end="")
            else:
              print("Enter Valid Number")







              #hammad Read File
        elif readinp==3:
            hammad_chose_file = int(input("This Is hammad Read File 1 for Exasise And 2 for Food\n"))

            #hammad Exasise List REad
            if hammad_chose_file==1:
                with open("hammad_exasies_list.txt","r") as f:
                    hammad_exasies_list= f.readlines()
                    # print(hammad_exasies_list)
                    for exasies in hammad_exasies_list:
                        print(exasies, end="")

            #hammad Food List Read
            elif hammad_chose_file==2:
                with open("hammad_food_list.txt","r")as f:
                    hammad_food_list = f.readlines()
                    # print(hammad_food_list)
                    for food in hammad_food_list:
                        print(food ,end="")
            else:
              print("Enter Valid Number")

        else:
            print("please Enter Valid number")

    else:
        print("Please Enter A Valid Number")           
              


take(choseLogOrRead)
