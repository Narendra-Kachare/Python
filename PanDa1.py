"""
    Dataframes using python : panda2
"""

import pandas as pd

def main():
    print("Empty data frame")
    df = pd.DataFrame()
    print(df)

    print("Dataframe with list")
    data = [1,2,3,4,5]
    df = pd.DataFrame(data)
    print(df)

    print("Dataframe with list")
    data = [['PPA',4],['LB',3],['Angular',3],['Python',3]]
    df = pd.DataFrame(data,columns=['Name','Duration'])
    print(df,end="\n\n")

    data = {'Name': ['PPA','LB','Python','Angular'],'Duration':[4,3,3,3]}
    df = pd.DataFrame(data)
    print(df)

    print()
    data = [{'Name':'PPA','Duration':'3','Fees':18500},{'Name':'Angular','Duration':'3','Fees':18500},{'Name':'Python','Duration':'3','Fees':18500},{'Name':'LB','Duration':'3','Fees':18500},]
    df = pd.DataFrame(data)
    print(df)

    print("\n\n")
    data = {'One':pd.Series([1,2,3], index=['a','b','c']),'Two':pd.Series([1,2,3,4], index=['X','Y','Z','W'])}
    df = pd.DataFrame(data)
    print(df)

    print(df['One'])

if __name__ == "__main__":
    main()