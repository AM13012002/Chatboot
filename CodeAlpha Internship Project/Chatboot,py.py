def basic_chatbot():
    while True:
        # Get input from the user
        user_input = input("You: ").lower()  # Convert input to lowercase for easy comparison

        # Check user input and respond accordingly
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break  # Exit the loop and end the chat
        else:
            print("Bot: Sorry, I didn't understand that.")

# Call the chatbot function
basic_chatbot()