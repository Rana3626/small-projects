def clean_word(word):
    return word.lower().strip(".,!?;:")

def lines_counter(text):
    counter=0
    for line in text:
        counter+=1
    return counter

def words_counter(text):
    counter=0
    for word in text:
        for i in word.split():
            counter+=1
    return counter


def character_counter(text):
    counter=0
    for word in text:
        for i in word:
            counter+=1
    return counter
    
def unique_words_counter(text):
    unique_words=set()
    for word in text:
        for i in word.split():
            i = clean_word(i)
            unique_words.add(i)
    return len(unique_words) 

def most_frequent_word(text):
    word_freq={}
    for line in text:
            for i in line.split():
                i = clean_word(i)
                if i not in word_freq:
                    word_freq[i]=1
                else:
                    word_freq[i]+=1
                    
    max_frequency=0
    most_frequent=""
    for i in word_freq:
       if word_freq[i]>max_frequency:
           max_frequency=word_freq[i]
           most_frequent=i
    return most_frequent
        

def count_word_frequency(text,user_word):
    counter=0
    user_word = clean_word(user_word)
    for word in text:
            for i in word.split():
                i = clean_word(i)
                if user_word==i:
                    counter+=1
    return counter
                
    
with open ("sample.txt" , 'r') as file:
    text = file.readlines()
    
print("Text file analyzer") 
print("--------------------------------------------")  
print("The number of lines: ", lines_counter(text))   
print("The number of words: ", words_counter(text) ) 
print("The number of characters : ", character_counter(text) ) 
print("The number of unique words: ", unique_words_counter(text) ) 
print("The most frequent word: ", most_frequent_word(text) ) 


res=input("Do you want to ask about a certain word frequency? answer with yes or no : ")

if res.strip().lower()=="yes" :
    user_word=input("What is the word? ")
    print("The frequency of the word is: ", count_word_frequency(text,user_word))
    
    
