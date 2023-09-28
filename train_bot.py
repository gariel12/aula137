import nltk
from nltk.chat.util import Chat, reflections

# Defina os padrões de respostas do chatbot
respostas = [
    ["Oi", ["Olá!", "Oi!", "Como posso ajudar você?"]],
    ["Qual é o seu nome?", ["Meu nome é ChatGPT.", "Você pode me chamar de ChatGPT."]],
    ["Como você está?", ["Estou bem, obrigado por perguntar!", "Estou sempre pronto para ajudar."]],
    ["O que você pode fazer?", ["Posso responder a algumas perguntas simples. Tente me perguntar algo."]],
    ["Sair", ["Até logo!", "Tenha um ótimo dia!"]],
]

# Crie um objeto Chat com os padrões de respostas
chatbot = Chat(respostas, reflections)

# Função principal do chatbot
def chat_with_bot():
    print("Olá! Eu sou o ChatGPT. Digite 'Sair' para encerrar o chat.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("ChatGPT: Até logo!")
            break
        response = chatbot.respond(user_input)
        print("ChatGPT:", response)

# Inicie o chatbot
if __name__ == "__main__":
    nltk.download("punkt")  # Certifique-se de que o NLTK tenha os recursos necessários baixados
    chat_with_bot()
