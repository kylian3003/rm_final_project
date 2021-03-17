# File name: count_racist_tweets.py
# Description: This program will take text containing Tweets from the standard
# input, which can be done by using the 'cat' command in your terminal. The
# text will be tokenized and then checked for any racist words. Finally, the
# program will print a table containing the total number of Tweets, number of
# racist Tweets and the percentage of Tweets that are racist.
# Author: Kylian de Rooij
# Date: 17/02/2021


import sys
from nltk.tokenize import TweetTokenizer


def tweet_counter():
    """This function counts Tweets, tokenizes them and then counts the racist
    Tweets. This function does all three things for efficiency purposes."""
    tweet_tokenizer = TweetTokenizer()
    # Setting variables for counters, and list of racist keywords
    racist_words = ["bruin", "bruinen", "neger", "negers", "negerin", "negerinnen", "nikker", "nikkers", "zwart", "zwarten", "cappuccin", "cappuccino",  "chocolademelk", "chocomel", "chocomelk", "donkerbruin", "kleurboek", "kleurboeken", "kleurling", "kleurpotloden", "koffie", "lichtbruin", "rascist", "rascisten", "nigger", "niggers", "nigga", "niggas", "negro", "negroes"]

    total_tweets = 0
    racist_tweets = 0
    # Iteration over all lines (tweets)
    for tweet in sys.stdin:
        # Racist is set to False, as the program is unsure yet whether the
        # Tweet is racist or not, thus it is safer to assume that it is not.
        racist = False
        # For each iteration, 1 is added to the total Tweets.
        total_tweets += 1
        # Creates a list with all the tokens in the Tweet.
        tweet_tokens = tweet_tokenizer.tokenize(tweet)
        # Iteration over the token list
        for token in tweet_tokens:
            for element in racist_words:
                # If the word is racist, 1 is added to the racist Tweet
                # counter and the racst condition is set to True.
                if element.lower() == token.lower():
                    racist_tweets += 1
                    racist = True
                # If the Tweet is racist, the iteration over the Tweet ends
                # using two break statements. This is so that Tweets with
                # several racist words are not counted more than once.
                if racist is True:
                    break
            if racist is True:
                break
    # Takes the total number of Tweets and the number of racist Tweets and
    # sends them back to the main function.
    return total_tweets, racist_tweets


def print_table(total_tweets, racist_tweets, racist_percentage):
    """This function creates a table containing all the data the program
    collected."""
    # Changes the number of decimal points of the percentage to 2.
    racist_percentage = format(racist_percentage, '.2f')
    # Converts the percentage into a string value and adds a '%' character.
    racist_percentage = str(racist_percentage) + " %"
    # Creates a table containing the data collected.
    print(" ________________________________________________________ ")
    print("|{0:^18}|{1:^18}|{2:^18}|"
          .format("Tweets", "Racist Tweets", "Percentage racist"))
    print("|__________________|__________________|__________________|")
    print("|{0:^18}|{1:^18}|{2:^18}|"
          .format(total_tweets, racist_tweets, racist_percentage))
    print("|__________________|__________________|__________________|")
    print()


def main():
    # Created two variables created by the tweet_counter() function.
    total_tweets, racist_tweets = tweet_counter()
    # Calculates the percentage of Tweets that are racist.
    racist_percentage = racist_tweets / total_tweets * 100
    # Calls the function to create the table of the data collected.
    print_table(total_tweets, racist_tweets, racist_percentage)


# If the program is executed, the main function will be called.
if __name__ == "__main__":
    main()
