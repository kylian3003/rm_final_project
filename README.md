# rm_final_project

The repository:
1. count_racist_tweets.py
2. sample_data.gz
3. collected_data.txt
4. README.md

Versions:
- Linux version used: 5.8.0-45-generic
- Python version used: Python 3.8.5 (default, Jan 27 2021, 15:41:15)

count_racist_tweets.py:

This is a program that counts the number of Tweets, racist Tweets and the percentage of racist Tweets in the standard input of the Linux terminal. Keep in mind that this program is designed to analyse a dataset of Dutch tweets, how to change that will be explained below under 'Changing language'.

Getting started:
1. Put the repository on your PC by either downloading it as a compressed zip file or by typing 'git clone https://www.github.com/kylian3003/rm_final_project' into your Linux terminal.
2. To use the program, you need any type of text file containing Tweets. These Tweets need to each be on a separate line. The text file format doesn't matter, as long as you can get the Tweets into the standard input, it works. (The data I used was in archive files (.gz).)

How to use:
1. (You can skip this step if you only want to use one file) Make sure all the files/data you want to analyse is in the same folder. This way, all the files can be analysed at once, rather than one by one.
2. Get the contents of the files into the standard input using cat, or any different tool, as long as it gets the data into the standard input, it works. (Since my data was in compressed gz files, I used a tool provided by the university to put the data into the standard input.) An example command line argument for text files would be cat 'data/*.txt | python3 count_racist_tweets.py'
3. The program will now collect all the data, which might take a while, depending on the size of your dataset. The results will be printed to a convenient table.
(In the program, you can find additional comments on what each part of the code is for.)

Changing language:

If you wish to change the language the program analyses, you must do this manually by changing the elements in the list in line 20 of count_racist_tweets.py to a list of words in a different language.

Data:

The source of my data is the corpus from the University of Groningen (Rijksuniversiteit Groningen), which collects all Dutch Tweets per data and stores them on their servers as .gz files.
In terms of files, as mentioned before, it doesn't matter what the file type is.
A sample file can be found in the repository.

List of racist keywords:

The main source for the list of racist words can be found on https://www.github.com/clips/hades/blob/master/cleaned.csv Although I have made some adjustments to the list, so that it would only contain keywords that express racism towards black people specifically. I also made added a few plurals, as they were not included in the original list. On top of that, I have added a few of the most common English racist terms.
