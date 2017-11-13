""" Palindrome """

from itertools import permutations


class Palindrome:

    def get_words(self):
       # return a list of words 
       words = raw_input("Enter words to combine and check? ")
       while len(words) < 1:
            words = raw_input("Please try again:  Enter words to combine and check? ")
       return words

    def generate_permutations(self,words):
        # expand a string of words (with whitespace) into a list of all
        # permutations of the words
        # returns a list of lower case strings which are the words concatenated
        
        def permute(wordsL):
            permL = []
            for plength in range(1,len(words)+1):
                pL = permutations(wordsL,plength)
                for i in pL:
                    permL.append(i)
            return permL

        def make_string(permutedL):
            stringL = []
            for plength in permutedL:
                s = "".join(plength)
                stringL.append(s.lower())
            return stringL

        wordsL = words.split()   # use any whitespace to split the words
        return make_string(permute(wordsL))

    def check_palindrome(self,candidate):
        # check whethe; a candidate string is a palindrome or not.  
        # returns True or False
        
        nchar = len(candidate)
        max_offset = (nchar+1)/2   # if nchar =2, this should be 1
        for chidx in range(0,max_offset):
            if candidate[chidx] != candidate[nchar-1-chidx]:
                # not matching
                return False
        return True

    def look_for_palindromes(self,candidateL):
        # for each string in a list of candidates check whether it is a
        # palindrome.
        # returns a list of strings that are palindromes.
        
        palindromes = []
        for candidate in candidateL:
            if self.check_palindrome(candidate):
                palindromes.append(candidate)
        return palindromes
        
    def find_palindromes(self):
        # ask for an input string of words and generate a list of palindromes

        words = self.get_words()
        permutedL = self.generate_permutations(words) 
        palindromes = self.look_for_palindromes(permutedL)
    
        print "These are the palindromes:"
        if len(palindromes) == 0:
            print "  None"
        else:
            for palindrome in palindromes:
                print " ",palindrome

if __name__ == '__main__':

    checker = Palindrome()
    checker.find_palindromes()
