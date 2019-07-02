questions_dic={
    "name":"Hello, my name is Bot may I know what is your name? ",
    "age":"How old are you? ",
    "coding":"Do you have any experience in coding? (Yes/No) ",
    "coding2":"What sort of programming language you use?",
    "like_python":"Do you like learning Python? (Yes/No)",
    "continue":"Do you wish to continue chatting (Yes/No)",
    "learn_together":"Can we start learning together? (Yes/No)",
    "editor":"Do you use any editor? (Yes/No)",
    "editor2":"What's the editor name that you are using?",
    "occupation":"What are your occupation? ",
    "marital_status":"Are you married? (Yes/No)",
    "hobby":"Whats your favorite hobby? ",
    "transport":"How type of transport you take to travel here "
}



positive_dic={
    "name":"Hi %s nice to meet you!",
    "age":"You are %s. That's Cool! You are young! Like Siri I am as old as the universe",
    "coding":"Great! I can learn from you",
    "coding2":"%s I love that language.\n Let's get going learning with Python now",
    "like_python":"It seems we have a lot in common",
    "continue":"I sure like chatting with you",
    "learn_together":"You are my buddy. We can help each other",
    "editor":"My favorite is Atom",
    "editor2":"Wow! you must be an expert using %s",
    "occupation":"%s ..that's a hot job",
    "marital_status":"You must have a lovely spouse",
    "hobby":"I love %s also",
    "transport":"You must like taking %s. Nice chatting with you.Bye"
}

negative_dic={
    "name":"Hi %s nice to meet you!",
    "age":"You are %s. That's Cool! You are young! Like Siri I am as old as the universe",
    "coding":"I see. It is not too late to start.\n Let's get going learning with Python now",
    "coding2":"%s I love that language.",
    "like_python":"You will grew to like it",
    "continue":"You must be busy. Next time then. Bye",
    "learn_together":"Do you wish to consider again. We can help each other",
    "editor":"You can start using VS Code. It is from Microsoft",
    "occupation":"%s ..that's a hot job",
    "marital_status":"I can introduce you a hot date",
    "hobby":"I love %s also",
    "transport":"You must like taking %s. Nice chatting with you.Bye"
}

user={
    "name":"",
    "age":"",
    "coding":"no",
    "coding2":"",
    "like_python":"",
    "editor":"",
    "learn_together":"",
    "occupation":"",
    "marital_status":"",
    "hobby":"",
    "transport":""
}

sequence= ["name",
    "age",
    "coding", #can skip
    "coding2",
    "like_python",
    "editor",
    "continue", #can break
    "learn_together",
    "occupation",
    "marital_status",
    "hobby",
    "transport"]

def printout (user):
    for k,v in user.iteritems():
        if v!="":
            print (questions_dic.get(k) + " " + v )

#sequence
skip=False
for k in sequence:
    v=questions_dic.get(k)
#for k,v in questions_dic #not in sequence.. anything goes
    response=raw_input(v)
    output=positive_dic.get(k)
    if (response.lower() =="yes" or response.lower()=='y'):
        print(output)
        if k=="editor":
            sequence.insert(sequence.index(k)+1,"editor2")
    elif (response.lower()=="no" or response.lower()=='n'):
        output= negative_dic.get(k)
        print(output)
        if k=="coding":
            sequence.pop(sequence.index(k)+1)
#             skip=True
        elif k=="continue": #skip all
            break
    else:
        print ( output % response)
    user[k]=responseå
#print user

printout(user)
