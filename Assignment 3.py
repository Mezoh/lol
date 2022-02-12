import glob 
import tkinter as tk
from tkinter.filedialog import askdirectory

def getDirectory():
    '''
    gets the directory of the books file through user input

    returns: a list of text files
    '''
    data_directory_books = askdirectory(initialdir = "/CISC 121/Assignments/Assignment 3")
    text_files = glob.glob(data_directory_books + '/' + "*.txt")

    return text_files

def letters_only(w):
    '''
    removes any character that is not a letter

    arguments: w (most likely will be a word)

    returns: the fixed word with all proper characters
    '''
    new_word = ""
    for c in w:
        if c.isalpha():
            new_word += c
    return new_word
    

def countWords(book, stopwords):
    '''
    takes each book and counts all the words besides the stopwords

    arguments: book (a text file of the book), stopwords(a set of stop words that should not be counted)

    returns: a dictonary including the amount of times each word was used
    '''
    word_counts = {}
    for line in book:
        line_words = line.split()
        for word in line_words:
            word = word.lower()
            word = letters_only(word)
            if word not in stopwords:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    #the code to return a list of pairs in the form: [('word', integer value amount)]

    #words_and_frequencies = []

    #for w,c in iter(word_counts.items()):
        #words_and_frequencies.append((w,c))

    #words_and_frequencies.sort(key = lambda x: x[1], reverse = True)
    #return words_and_frequencies

    # instead of using a list for the word count I decided to use a dictionary
    word_counts_sorted = {i: j for i, j in sorted(word_counts.items(), key =lambda x: x[1],  reverse = True)}
    return word_counts_sorted

def top_25_words(words):
    '''
    creates a dictionary of the top 25 used words in the books

    argument: a dictionary of the words of the book

    returns: a dictionary containing the top 25 used words
    '''
    top_25 = {}
    for key, value in words.items():
        if len(top_25) != 25:
            top_25[key] = value
        else:
            break
    return top_25


def stop_words_convert(txt):
    '''
    converts the stopwords.txt file into a set of stop words

    arguments: the directory to the specific txt file of stop words

    returns: stop words in the form of a set
    '''
    stop_words_file = open(txt, 'r', encoding = 'UTF-8')
    stop_words = set()

    for line in stop_words_file:
        word = letters_only(line)
        stop_words.add(word)
    return stop_words

def jaccardSimilarity():
    pass

def main():

    files = getDirectory() 
    stop_words = stop_words_convert("C:/Users/famou/Desktop/School/CISC 121/Assignments/Assignment 3/stopwords.txt")

    # creates the empty dictionary 
    book_top_25 = {}

    # for loop which iterates through each file in the directory
    for f in files:
        # sets the variable 'infile' to open and read the file
        infile = open(f,'r',encoding="UTF-8")
        # calls the function which removes unusable characters and counts the words
        book = countWords(infile, stop_words)
        # adds the file name and top 25 most frequent words to the empty dictionary
        book_top_25[f] = top_25_words(book)



main() 
