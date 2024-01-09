"""
    Dictionary 1

"""


def main():
    print("Demonstration of Dictionary")
    
    # Dictionary (Key:Value) 
    Dict1 = {"Brand":"Maruti","Model":"Dzire","Year":2020}
    print(Dict1)

    # print Update keys
    Dict1["Brand"] = "Kia"
    print(Dict1)

    # Update keys
    Dict1["Model","Year"] = "Sonet",2019
    print(Dict1)    # ("Model","Year") : ("Sonet",2019) असा एकच  set तयार होईल.

    Dict1["NewModel"] = "Tata"
    print(Dict1)

    # for finding keys in dictioanry
    if "Brand" in Dict1:
        print("Key Found")
    else:
        print("Key is not found")

    # Length
    print(len(Dict1))


    # Update values
    Dict2 = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e",}
    print(Dict2)

    Dict2[1] = "A"
    Dict2[2] = "B"
    Dict2[3] = "C"
    Dict2[4] = "D"
    Dict2[5] = "E"

    print(Dict2)

    
    

   
if __name__ == "__main__":
    main()