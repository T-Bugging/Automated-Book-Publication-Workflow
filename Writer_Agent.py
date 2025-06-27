def aiWriter():
    import os 
    import google.generativeai as googleAI
    from dotenv import load_dotenv

    # Load environment variables.
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    # Configure the Gemini client with your API key.
    googleAI.configure(api_key=api_key)

    # Load the model.
    model = googleAI.GenerativeModel("gemini-2.0-flash")

        #Provides user with options to choose the style of writing.
    print("---------------------------------------------------")
    print(" Welcome to the AI Writer!")
    print("Choose the style in which you want your story to be written:")
    print("1.Summarize : Summarize the story in a few sentences.")
    print("2.Simplify : Simplify the story to make it easier to understand.")
    print("3.Poetic : Write the story in a poetic style.")
    print("4.Rewrite : Rewrite the story with different endings, new characters, etc.")
    print("5.Custom : Select to customize the content according to you.")
   
    print("---------------------------------------------------")

    
    print("---------------------------------------------------")
        # Ask user for their choice.
    promptStyle = input("Enter your choice (1-5): ")
        
        # Maps prompt styles to their corresponding prompts.
    promptMapping = {
            "1": "Summarize the story in a few sentences.Output should be under 300 words.",
            "2": "Simplify the story to make it easier to understand. Use simple language and short sentences.",
            "3": "Write the story in a poetic style.",
            "4": "Rewrite the story in a different style.You can change the ending, add new characters, or change the plot.",
        }

    
            
        # Handling custom prompt input.
    if promptStyle == "5":
            customPrompt = input("Enter your custom prompt: ")
            userPrompt = customPrompt
        # Handling predefined prompt styles.
    elif promptStyle in promptMapping:
            userPrompt = promptMapping[promptStyle]
        # Handling invalid input.
    else:
            print("Invalid choice. Please select a valid option.")
            
        # Read the story content from the file.
    with open("output/Raw_text/text_1.txt", "r", encoding="utf-8") as file: # This is currently hardcoded to read the first text file. This is done for the sake of demonstration. In the future, this could be made dynamic to read the specified text file.
            story_content = file.read()

        # Combine user prompt and story content.
    WriterPrompt = userPrompt + "\n\n" + story_content

        # Generate content
    writerResponse = model.generate_content(WriterPrompt)
    print(writerResponse.text)
    return writerResponse.text

