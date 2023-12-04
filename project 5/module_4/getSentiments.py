#Rylie Ewers, Decker Gramlich
#cs325 project 6

import openai
import time

#method for the api call
def apiCall(prompt):
    try:
        response = openai.completions.create(
            model="text-davinci-003",
            prompt = prompt,
            max_tokens = 3000
        )
        return response.choices #returns the answers

    #if there is a rate limit error it will let the user know then wait 30 seconds and try again
    except openai.RateLimitError:
        print("waiting 30s because of rate limit")
        time.sleep(30)
        return apiCall(prompt)

#
def getSentiments(key, comments, outpath):

#key to the opanai API
    openai.api_key = key #'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'

#takes the comments list and add the prompt to it
    prompts = []
    for i in range(0, 50):
        prompts.append('Tell me in one word(positive, negative, or neutral), what is the sentiment of this comment: "' + comments[i].strip() + '".')

#makes a call to the openai API with the list and returns responses
    answers = []
    #list is split into 3 as to not get a rate limit error and lets the user know when which call is made
    answers.extend(apiCall(prompts[0: 20]))
    print("1 call made")
    answers.extend(apiCall(prompts[20: 40]))
    print("2 call made")
    answers.extend(apiCall(prompts[40: 50]))
    print("3 call made")

#takes the responses and puts them in its own file
    file = open(outpath, "w")
    for i in range (0, len(answers)):
        #sanitizing the api responses to write in file
        answer1 = answers[i].text #takes the text from the responses
        answer2 = answer1.strip() #getting rid of any white space(spaces, new lines)
        answer3 = answer2.strip('.,') #getting rid of any ponctuation marks
        answer4 = answer3.capitalize() #capitalizing the first letter
        answers[i] = answer4 #puts it back in the list

        file.write(answers[i])
        file.write('\n')
    file.close()

    return answers #returns the list of sentiments to be used for the plots
