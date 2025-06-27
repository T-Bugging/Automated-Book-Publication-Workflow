#Import necessary modules from other files.
from scraper import scrape
from Writer_Agent import aiWriter
from Reviewer_agent import aiReviewer
from ChromaDB import search
from RL_Search import giveFeedbackOnResults

#Assking user for input to choose between AI writer or ChromaDB.
print("---------------------------------------------------")
print("What would you like to do? (1-2) ")
choice = input("1. Access AI writer \n2. Access ChromaDB : ")
print("---------------------------------------------------")

#If user chooses AI writer, scrape the page and generate a story using AI writer.
if choice == "1":
# Sample URL = https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1
    url = input("Enter the URL of the page to scrape: ")

    scrape(url)
    writerResponse=aiWriter()
    aiReviewer(writerResponse)

#If user chooses ChromaDB, search for a story in the database.
elif choice == "2":
    query = input("Enter a story to search for: ")
    results = search(query, top_k=3)

    for i in range(len(results["documents"])):
        print(f"\nResult {i+1}")
        print("ID:", results["ids"][i])
        print("Metadata:", results["metadatas"][i])
        print("Content (preview):", results["documents"][i][:300], "...")
    #The Reinforcement Learning will ask for feedback on the results and change feedback score accordinly.
    ranked =giveFeedbackOnResults(results)

#Error handling for invalid input.
else:
    print(" Invalid choice. Please enter 1 or 2.")