#Rylie Ewers, Decker Gramlich
#cs325 project 5

import openai

#key to the opanai API
openai.api_key = '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'


def getSentiments(comments, outpath):
#takes the comments list and add the prompt to it
    prompts = []

    for i in range(0, 20):
        prompts.append('Tell me in one word(positive, negative, or neutral), what is the sentiment of this comment: "' + comments[i].strip() + '"?')

#makes a call to the openai API with the list and returns responses
    response = openai.completions.create(
        model="text-davinci-003",
        prompt = prompts,
        max_tokens = 3000
)

#takes the responses and puts them in its own file
    file = open(outpath, "w")
    for i in range (0, len(response.choices)):
        file.write(response.choices[i].text.strip())
        file.write('\n')
    file.close()