import random
list_of_responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
eight_ball_input = input("What is your question?")
x = 0
while x == 0:
    if "?" in eight_ball_input:
        num = random.randint(0,19)
        response = list_of_responses[num]
        print(response)
        x = 1
    else:
        print("I'm sorry, I can only answer questions.")
        eight_ball_input = input("What is your question?")
        if eight_ball_input == "quit":
            x = 1
            print("Quitting program")
