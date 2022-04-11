class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        word_list = list(word)  # create a list of chars
        if word_list[0].islower():
            return all(char.islower() for char in word_list)  # return true if all other are lower too
        if all(char.islower() for char in word_list[1:]):  # if the first is upper and rest are lower return True
            return True
        else:
            return all(
                char.isupper() for char in word_list)  # if the first is upper as well as all others return True
                # otherwise return False
