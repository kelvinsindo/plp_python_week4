class Person:
    def __init__(me, name, age, gender):
        me.name = name
        me.age = age
        me.gender = gender

    def introduce(me):
        print(f"Hi, my name is {me.name}. I am {me.age} years old {me.gender}.")
        
#instance of the Person class
person1 = Person("Kelvin", 21, "Male")

#the introduce method
person1.introduce()