import sys
def elon():
    print("enter a name")
    name = input()
    print("enter a pronoun")
    pronoun=input()
    print("enter a date")
    date=input()
    print("enter a jobtitle")
    jobtitle=input()
    print("enter a year")
    year=input()
    print("enter 4 company names")
    company1=input()
    company2=input()
    company3=input()
    company4=input()
    print("enter 2 amounts of money")
    amountofmoney=input()
    money=input()
    print("enter a propernoun")
    propernoun=input()
    print("enter 3 contries")
    bornin=input()
    country=input()
    anothercountry=input()
    with open('libs/default/elon.txt', 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('$name', name)
    filedata = filedata.replace('$pronoun', pronoun)
    filedata = filedata.replace('$date', date)
    filedata = filedata.replace('$year', year)
    filedata = filedata.replace('$jobtitle', jobtitle)
    filedata = filedata.replace('$company1', company1)
    filedata = filedata.replace('$company2', company2)
    filedata = filedata.replace('$company3', company3)
    filedata = filedata.replace('$company4', company4)
    filedata = filedata.replace('$amountofmoney', amountofmoney)
    filedata = filedata.replace('$money', money)
    filedata = filedata.replace('$propernoun', propernoun)
    filedata = filedata.replace('$bornin', bornin)
    filedata = filedata.replace('$country', country)
    filedata = filedata.replace('$anouthercountry', anothercountry)
    print(filedata)
def main():
    elon()
if __name__ == "__main__":
    main()