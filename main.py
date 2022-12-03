from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

print("Bem vindo ao Chatbot")

pergunta = input("Faça sua pergunta!"\n)
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")

while (intencao[0]['intent']!="despedida"):
    pergunta = input("Mais alguma pergunta?"\n)
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
