# StopWord-Recognizer
This program is a DFA-based recognizer specifically to find English stop words.
Stop words are commonly used words in a language that are often considered irrelevant or carry little meaning in certain text analysis or natural language processing tasks. 
In this program, only English article (a, an, the) and some auxiliary verbs with length at most 3 (are, be, can, etc) are accepted. While auxiliary verbs with more than 3 letters (being, could, etc) and other types of stop words (pronouns, prepositions, conjunctions) are rejected, considering more than 100 stop words exist which can affect the complexity of the DFA structure.

Figure a: DFA diagram for a stop words finder
![image](https://github.com/ZainabSahardin/StopWord-Recognizer/assets/62138875/21ab4bc0-11e8-4f3d-8bbd-d37a916096e8)


The program read through a text file and extract the words while excluding non-word characters such as punctuation or whitespace. By iterating over the extracted words, DFA process is performed and accepted strings will be highlighted. The letter in the words are transformed to small letter before sent to DFA function ensuring all strings are being processed regardless the small or capital letter. Lastly, the original text will be printed with the accepted words highlighted as shown in sample output below;

Figure b: Sample Output
![image](https://github.com/ZainabSahardin/StopWord-Recognizer/assets/62138875/89e82e31-4574-4b11-85f6-215924db3379)

