message = []
input_text = ''


def sentence_checker(sentence):
    if(len(message)>0):    
        if sentence.startswith(('what', 'why', 'where', 'who', 'how')):
            return "{}?".format(sentence.capitalize())
        else:
            return "{}.".format(sentence.capitalize())
    else:
        message

def sentence_merger(sentence):
    message.append(sentence_checker(sentence))

while input_text != '..end':
    sentence_merger(input_text)
    input_text = input(" Say something (Type '/end' to exit): ")

print(message)
