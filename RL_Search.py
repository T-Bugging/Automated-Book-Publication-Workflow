import json

# Load feedback scores or create if it doesn't exist. This is a json file.
try:
    with open("feedback_scores.json", "r") as f:
        feedback_scores = json.load(f)
except FileNotFoundError:
    feedback_scores = {}

# Function to rank results based on feedback scores.
def rankResults(results):
    combined = list(zip(
    [doc_id[0] for doc_id in results["ids"]],  # ✅ flatten IDs
    results["documents"],
    results["metadatas"]
))
    ranked = sorted(combined, key=lambda x: feedback_scores.get(x[0], 0), reverse=True)
    return ranked

#Asks the user for feedback on the results and updates the feedback scores.
def giveFeedbackOnResults(results):
    if not results or not results.get("documents"):
        print("No results found.")
        return

    ranked = rankResults(results)

    for i, (doc_id, doc_text, metadata) in enumerate(ranked):
        print(f"\nResult {i+1}")
        print("ID:", doc_id)
        print("Title:", metadata[0].get("title"))
        print("Preview:\n", doc_text[:100],  "...\n" + "-"*60)

    choice = input("\nWhich result did you like most? (1/2/3 or skip): ").strip()

    if choice in {"1", "2", "3"}:
        selectedID = ranked[int(choice) - 1][0]
        feedback_scores[selectedID] = feedback_scores.get(selectedID, 0) + 1
        print(f"Feedback saved for ID: {selectedID}")
        with open("feedback_scores.json", "w") as f:
            json.dump(feedback_scores, f, indent=4)
    else:
        print("No feedback recorded.")
