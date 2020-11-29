import os
import sys

#---------------------------------------------------------------
def word2dic(word):

    dic = {}
    for item in word:
        if item in dic:
            count = dic[item]
            dic[item] = count + 1
        else:
            dic[item] = 1

    return dic

#---------------------------------------------------------------
if __name__ == '__main__':

    #Words
    word1 = 'tester'
    word2 = 'restet'

    #To Dic
    wordDic1 = word2dic(word1)
    wordDic2 = word2dic(word2)

    #Is Anagram
    print(wordDic1 == wordDic2) 