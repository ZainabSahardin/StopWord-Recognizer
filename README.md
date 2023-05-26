# StopWord-Recognizer
This program is a DFA-based recognizer specifically to find English stop words.
Stop words are commonly used words in a language that are often considered irrelevant or carry little meaning in certain text analysis or natural language processing tasks. 
In this program, only English article (a, an, the) and some auxiliary verbs with length at most 3 (are, be, can, etc) are accepted. While auxiliary verbs with more than 3 letters (being, could, etc) and other types of stop words (pronouns, prepositions, conjunctions) are rejected, considering more than 100 stop words exist which can affect the complexity of the DFA structure.
