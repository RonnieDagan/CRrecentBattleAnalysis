
def format_ai(ai_text):
    temp = ai_text.split("\n")
    strengths = []
    weaknesses = []
    summary = ""
    mode = 0
    for i in range(len(temp)):
        temp2 = temp[i].split(" ")
        if temp2[0] == "Cards" or temp2[0] == "Summary:":
            mode+=1
        if mode == 1:
            if temp2[0] != "Cards" and temp2[0] != "Summary:" and temp2[0] != '':
                strengths.append(temp[i])
        if mode == 2: 
            if temp2[0] != "Cards" and temp2[0] != "Summary:" and temp2[0] != '':
                weaknesses.append(temp[i])
        if mode == 3:
            for word in temp2:
                if word != 'Summary:':
                    summary+= word + ' '
        summary.rstrip()
    return [strengths, weaknesses, summary]

    
