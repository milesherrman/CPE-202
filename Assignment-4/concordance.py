from email.mime import nonmultipart
from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
from hash_quad import *
import string
import re
class Concordance:

    def __init__(self):
        self.stop_table = None  
        self.stop_list = None        # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table"""
        try:
            stop_file = open(filename)
        except:
            raise FileNotFoundError

        self.stop_table = HashTable(191)
        self.stop_list = [line.rstrip("\n") for line in stop_file.readlines()]
        stop_file.close()
        
        for i, word in enumerate(self.stop_list):
            self.stop_table.insert(word, i)


    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table"""
        try:
            input_file = open(filename)
        except:
            raise FileNotFoundError("issues opening file")
        
        lines = [line.lower().replace("'", "") for line in input_file.readlines()]
        words = []
        for num, line in enumerate(lines):
            cleanLine = line.translate(str.maketrans({key: " " for key in string.punctuation})).rstrip("\n")
            word1 = cleanLine.split(" ")
            nonRepeatingWords = []
            [nonRepeatingWords.append(x) for x in word1 if x not in nonRepeatingWords]
            words.extend(list(map(lambda i : [i, num+1], filter(lambda i : i.isalpha(), nonRepeatingWords))))
        
        input_file.close()
        
        self.concordance_table = HashTable(191)
        for word in words:
              if not(self.stop_table.in_table(word[0])):
                if self.concordance_table.in_table(word[0]):
                    val = self.concordance_table.get_value(word[0])
                    val.append(word[1])
                    self.concordance_table.insert(word[0], val)
                else:
                    self.concordance_table.insert(word[0], [word[1]])


    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)"""
        output_file = open(filename, "w")
        keys = self.concordance_table.get_all_keys()
        keys.sort()
        pairs = [[key, self.concordance_table.get_value(key)] for key in keys]
        output = ""
        for pair in pairs:
            lines = ""
            for num in pair[1]:
                lines += f" {num}"
            stripped = lines.lstrip(" ")
            output += f"{pair[0]}: {stripped}\n"
        output_file.write(output.rstrip("\n"))
        output_file.close()