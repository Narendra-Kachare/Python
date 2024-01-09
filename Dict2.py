"""
    Dictionary 2

"""
import os

def main():
    print("Demonstration of Dictionary")
    
    # Inside dictionary : list is used to store values    
    Dict1 = {1:["One"], 2:["Two"], 3:["Three"], 4:["Four"], 5:["Five"]}
    print(Dict1)


    # Insert Values
    Dict1[6] = ["Sixx"]
    print(Dict1)

    # Update Values
    Dict1.update({6:["Six"]})
    print(Dict1)

    # Append values
    for i in range(1,7,1):
        Dict1[1].append(i)
    Dict1[1].append("Root")
    print(Dict1)
    print(Dict1[1][7])
    Dict1[1].remove(Dict1[1][3])
    print(Dict1)
    # print(list(Dict1[1][7]).remove())

    

    

   
if __name__ == "__main__":
    main()