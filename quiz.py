score=0
addition=5
print("Welcome To The Quiz Competition")
import time
print("Your time start now!!!")
start=time.time()
print("1. Which planet is known as the Red Planet?\na) Earth\nb) Jupiter\nc) Mars\nd) Venus")
value=input("Choose the correct option:").upper()
match value:
    case "A":
        print("You are wrong.")
    case "B":
        print("You are wrong.")
    case "C":
        print("You are correct.")
        score=score+addition
    case "D":
        print("You are wrong.")
    case _:
        print("Invalid choice.")
print("===================================================================")
print("2. Who wrote the national anthem of India?\na) Rabindranath Tagore\nb) Bankim Chandra Chattopadhyay\nc) Sarojini Naidu\nd) Subhash Chandra Bose")
value=input("Choose the correct option:").upper()
match value:
    case "A":
        print("You are correct.")
        score=score+addition
    case "B":
        print("You are wrong.")
    case "C":
        print("You are wrong.")
    case "D":
        print("You are wrong.")
    case _:
        print("Invalid choice.")
print("===================================================================")
print("3. Which keyword is used to define a function in Python?\na) func\nb) def\nc) define\nd) function")
value=input("Choose the correct option:").upper()
match value:
    case "A":
        print("You are wrong.")
    case "B":
        print("You are correct.")
        score=score+addition
        
        
    case "C":
        print("You are wrong.")
    case "D":
        print("You are wrong.")
    case _:
        print("Invalid choice.")


print("===================================================================")
print("4. What does RAM stand for?\na) Readable Access Memory\nb) Read All Memory\nc) Random Access Memory\nd) Ready Access Memory")
value=input("Choose the correct option:").upper()
match value:
    case "A":
        print("You are wrong.")
    case "B":
        print("You are wrong.")
    case "C":
        print("You are correct.")
        score=score+addition
        
        
    case "D":
        print("You are wrong.")
    case _:
        print("Invalid choice.")
print("===================================================================")
print("5. What is the chemical symbol for water?\na) O2\nb) H2O\nc) CO2\nd) HO")
value=input("Choose the correct option:").upper()
match value:
    case "A":
        print("You are wrong.")
    case "B":
        print("You are correct.")
        score=score+addition
        
    case "C":
        print("You are wrong.")
    case "D":
        print("You are wrong.")
    case _:
        print("Invalid choice.")
end=time.time()
print("Total score is now:",score)
if score < 15:
    print("Feedback: Need improvement.")
else:
    print("Feedback: Good job!")
print("Time taken:", end - start, "seconds")
if((end-start)>=20):
    print("Need better time management.")
