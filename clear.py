import pickle
import pprint

cleard_dict = {
    'easy':[],
    'hard':[],
    'medium':[]
}
print("Warning!!! This will clear the funny_question_data.pickle file")
choice = input("Enter 'YES' if you want to continue and clean the file else just hit enter: ")
if choice == "YES":
    print("Clearing the file...")

    with open("funny_question_data.pickle", "wb") as file:
        pickle.dump(cleard_dict, file, protocol=pickle.HIGHEST_PROTOCOL)
    
    print("File cleared")
else:
    print("Skipped clearing the file")
