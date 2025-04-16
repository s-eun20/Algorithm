def solution(name, yearning, photo):
    answer = [] # answer list
    for people in photo: # iterate photos
        total_score = 0 # set total score to 0
        for person in people: # iterate people in photo
            if person in name: # if person in the name list
                idx = name.index(person) # find the index of the person
                total_score += yearning[idx] # add person's yearning score to the total score
        answer.append(total_score) # add the total score to the answer list
    return answer # return the answer list