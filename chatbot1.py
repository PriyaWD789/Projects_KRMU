import json
from difflib import get_close_matches

# Load existing data
def load_data(file_path:str)-> dict:
    with open(file_path,'r')as f:
        data:dict=json.load(f)
    return data
    
# Save updated data
def save_data(file_path:str,data:dict):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=3)


# Find best mathc of the  data
def find_match(user_input:str,questions:list[str])-> str | None:
    matches:list = get_close_matches(user_input,questions,n=1,cutoff=0.6)
    return matches[0]if matches else None

def get_answer(question:str,rules:dict)-> str| None:
    for q in rules["questions"]:
        if q["question"]== question:
            return q["answer"]
    return None

def chatbot():
    print("Chatbot is ready! (type 'quit' to exit)\n")
    rules:dict= load_data('rules.json')
    while True:
        user_input:str = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break

        best_match :str|None= find_match(user_input,[q["question"] for q in rules["questions"]])

        if best_match:
            answer:str=get_answer(best_match,rules)
            print(f'Bot: {answer}')
        else:
            print("Bot: I donot know the ans.")
            new_ans:str=input('Type the ans')


            if new_ans.lower()!='skip':
                rules["questions"].append({"question":user_input,"answer":new_ans})
                save_data(rules.json,rules)
                print("Bot: Thank you I learned a new response!")

if __name__ == "__main__":
    chatbot()



