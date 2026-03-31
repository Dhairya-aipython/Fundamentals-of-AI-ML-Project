# ============================================================
# Sentiment Analyzer for Product Reviews
# Author: Dhairya
# Course: Fundamentals of AI & ML (Vityarthi - CO5 BYOP)
# A simple tool I built to check customer reviews - positive, negative, or neutral.
# Handles basic negations like "not good" too.
# ============================================================

# Word lists - added these based on common review words I see online
positive_words = [
    "good", "great", "excellent", "amazing", "awesome", "fantastic", "love", "loved",
    "best", "perfect", "happy", "wonderful", "superb", "brilliant", "nice", "recommended",
    "worth", "satisfied", "pleasant", "impressive", "beautiful", "fast", "quick",
    "easy", "helpful", "reliable", "durable", "quality", "value", "comfortable"
]

negative_words = [
    "bad", "worst", "terrible", "horrible", "awful", "hate", "hated", "poor", "useless",
    "broken", "disappointed", "disappointing", "waste", "slow", "difficult", "cheap",
    "damaged", "defective", "pathetic", "annoying", "ugly", "noisy", "expensive",
    "unreliable", "boring", "return", "refund", "fake", "misleading", "fragile"
]

negation_words = ["not", "never", "no", "don't", "doesn't", "didn't", "isn't", "wasn't"]  # Common negations

def clean_text(text):
    """
    Cleans the review text - keeps only letters, spaces, and apostrophes.
    Makes everything lowercase for matching.
    """
    cleaned = ""
    for char in text.lower():
        if char.isalpha() or char == " " or char == "'":
            cleaned += char
    return cleaned.strip()  # Remove extra spaces

def analyze_sentiment(review):
    """
    Main logic: splits words, checks for positive/negative, flips if negated.
    Compares scores to decide sentiment.
    """
    cleaned_review = clean_text(review)
    words = cleaned_review.split()

    pos_count = 0
    neg_count = 0

    # Loop through words, check for negation from previous word
    for i in range(len(words)):
        current_word = words[i]

        # Is there a negation before this word?
        is_negated = i > 0 and words[i-1] in negation_words

        if current_word in positive_words:
            if is_negated:
                neg_count += 1  # "not good" -> negative
            else:
                pos_count += 1
        elif current_word in negative_words:
            if is_negated:
                pos_count += 1  # "not bad" -> positive
            else:
                neg_count += 1

    # Decide final sentiment
    if pos_count > neg_count:
        return "POSITIVE", pos_count, neg_count
    elif neg_count > pos_count:
        return "NEGATIVE", pos_count, neg_count
    else:
        return "NEUTRAL", pos_count, neg_count

def print_result(review, sentiment, positives, negatives):
    print("\n" + "=" * 50)
    print("REVIEW:   ", review)
    print("SENTIMENT:", sentiment)
    print(f"Scores:   +{positives} Positive | -{negatives} Negative")
    print("=" * 50)

def print_history(analysis_history):
    if not analysis_history:
        print("\nNo reviews analyzed yet.")
        return
    print("\n--- Review History ---")
    for idx, item in enumerate(analysis_history):
        short_review = item['review'][:60] + "..." if len(item['review']) > 60 else item['review']
        print(f"{idx + 1}. [{item['sentiment']}] {short_review}")
    print("---------------------")

def print_summary(analysis_history):
    if not analysis_history:
        print("\nNo data to summarize.")
        return

    pos = sum(1 for h in analysis_history if h['sentiment'] == 'POSITIVE')
    neg = sum(1 for h in analysis_history if h['sentiment'] == 'NEGATIVE')
    neu = len(analysis_history) - pos - neg

    total_reviews = len(analysis_history)
    print("\n===== SESSION SUMMARY =====")
    print(f"Total Analyzed: {total_reviews}")
    print(f"Positive:        {pos}")
    print(f"Negative:        {neg}")
    print(f"Neutral:         {neu}")
    print("==========================")

# Main menu loop
def main():
    past_reviews = []  # Store all analyses here

    print("=" * 50)
    print("Sentiment Analyzer for Product Reviews")
    print("Fundamentals of AI & ML - BYOP Project")
    print("=" * 50)

    while True:
        print("\nMENU OPTIONS:")
        print("1. Analyze Review")
        print("2. Show History")
        print("3. Show Summary")
        print("4. Quit")

        user_choice = input("\nPick 1-4: ").strip()

        if user_choice == "1":
            new_review = input("\nEnter review: ").strip()
            if not new_review:
                print("Can't be empty! Try again.")
                continue

            sent, p_score, n_score = analyze_sentiment(new_review)
            print_result(new_review, sent, p_score, n_score)

            # Save to history
            past_reviews.append({
                'review': new_review,
                'sentiment': sent,
                'positive_score': p_score,
                'negative_score': n_score
            })

        elif user_choice == "2":
            print_history(past_reviews)

        elif user_choice == "3":
            print_summary(past_reviews)

        elif user_choice == "4":
            print("\nThanks for using the analyzer! Bye!")
            break

        else:
            print("Wrong choice - pick 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
