problem = input("what is your problem?  ")
problem_before = input("have you had this problem before (yes or no)?  ")
if problem_before.lower() == "yes":
    print("well, you have it again.")
elif problem_before.lower() == "no":
    print("well, you have it now")