def get_chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How are you doing?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day ahead!"
    elif "your name" in user_input:
        return "I am the CodeAlpha Rule-Based Chatbot."
    else:
        return "I'm sorry, I don't understand that command. Try saying 'hello', 'how are you', or 'bye'."

def run_chatbot():
    print("--- Welcome to CodeAlpha Basic Chatbot ---")
    print("Type your message below to chat. Type 'bye' to exit.")
    print("-" * 50)

    while True:
        user_message = input("You: ")
        bot_reply = get_chatbot_response(user_message)
        print(f"Chatbot: {bot_reply}")
        if "bye" in user_message.lower().strip() or "goodbye" in user_message.lower().strip():
            break

if __name__ == "__main__":
    run_chatbot()
