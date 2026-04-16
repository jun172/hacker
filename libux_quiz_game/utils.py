def check_answer(user_input, correct_answer, options):
    try:
        return options[int(user_input)-1] == correct_answer
    except:
        return False
    
def save_score(username, score, file_path="scores.json"):
    import json,os
    if os.path.exists(file_path):
        with open(file_path,"r") as f:
            data = json.load(f)
    else:
        data = {}
    data[username] = score
    with open(file_path,"w") as f:
        json.dump(data,f,indent=4)