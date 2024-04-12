class SubfieldsInAI:
    def SubFields():
        subFieldList=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for x in subFieldList:        
            print(x)
class OddEven:         
    def OddEven():
        i=int(input("Enter a number:"))
        if(i%2==1):
            print(i,"is Odd Number")
        else:
            print(i,"is Even Number")
            
class ElegiblityForMarriage():
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="MALE" and age <21):
            print("NOT ELIGIBLE")
        elif(gender=="MALE" and age >= 21):  
            print("ELIGIBLE")
        elif(gender=="FEMALE" and age <18): 
            print("NOT ELIGIBLE")
        elif(gender=="FEMALE" and age >=18):
            print("ELIGIBLE")
            
class FindPercent():
    def percentage():
        subject1=int(input("Subject1="))
        subject2=int(input("Subject2="))
        subject3=int(input("Subject3="))
        subject4=int(input("Subject4="))
        subject5=int(input("Subject5="))
        total=subject1+subject2+subject3+subject4+subject5
        percentage = (subject1+subject2+subject3+subject4+subject5)/5
        print("Total :",total)
        print("Percentage :",percentage)
        
class triangle():
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        areaFormula= (height*breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",areaFormula)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))    
        breadth2=int(input("Breadth:"))
        formula=height1+height2+breadth2
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",formula)