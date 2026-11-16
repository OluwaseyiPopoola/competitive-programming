"""
http://leetcode.com/discuss/post/1879225/google-l3-l4-l3-passed-by-anonymous_user-srco/

You have a dictionary of string, example - 
[string, sring, sing, wording, ing,ng, g]
You need to tell the maximum longest word in the dictionary that is valid.
Definiton of valid string , 
if you remove only one character from the string and it should be in the dictionary and by doing so if you able to reach at the end with length as 1, it will be valid.
Example - ( string-> sring->sing->ing->ng->g) [as all the intermediate string are present in the dictionary this will be a valid string and longest lenght is 6]

"""
def main():
    # dict = ["string", "sring", "sing", "wording", "ing","ng", "g"]
    # dict = ["planet", "plant", "pant", "pan", "pa", "p"]
    # dict = ["abcd", "abc", "ab"]
    # dict = ["hello", "hell", "he", "h"]
    # dict = ["a", "b", "c"]
    # dict = []

    res = findLongestValidWord(dict)
    print(res)

def helper(word, adyWords) -> bool: 
    if adyWords[word] is not None:
        return adyWords[word]

    if len(word) == 1:
        adyWords[word] = True if word in adyWords else False
        return adyWords[word]

    adyWords[word] = False
    for i in range(len(word)):
        if adyWords[word]:
            break

        posWord = word[:i] + word[i + 1:]

        if posWord not in adyWords:
            continue

        adyWords[word] = adyWords[word] or helper(posWord, adyWords) 


    return adyWords[word]

        


def findLongestValidWord(dict):

    longestWord = ""
                     
    adyWords = { string : None for string in dict }

    for word in dict:
        helper(word, adyWords)
      
        if adyWords[word] and len(word) > len(longestWord):
            longestWord = word

    return longestWord



if __name__ == "__main__":
    main()