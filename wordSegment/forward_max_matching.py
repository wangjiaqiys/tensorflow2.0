# _*_ coding:utf-8 _*_
def mmcut(sentence, wordsdict, RMM=True):
    """
    Func: Implemented the forward Maximum Match anc Reverse Maximum Match
    Para:
        sentence: The String to be segmented
        wordsdict: Dictionary
        RMM: Whether use the Reverse Maximum Match Method
    """
    result = []
    len_of_sentence = len(sentence)
    if not RMM: # 最大正向匹配
        while len_of_sentence > 0:
            word = sentence
            len_of_word = len(word)
            while len_of_word > 0:
                if word in wordsdict or len_of_word == 1:
                    result.append(word)
                    sentence = sentence[len_of_word:]
                    break
                else:
                    word = word[:len_of_word-1]
                len_of_word -= 1
            len_of_sentence = len(sentence)
    else: # 最大反向匹配
        while len_of_sentence > 0:
            word = sentence
            len_of_word = len(word)
            while len_of_word > 0:
                if word in wordsdict or len_of_word == 1:
                    result.append(word)
                    sentence = sentence[:len_of_sentence-len_of_word]
                    break
                else:
                    word = word[1:]
                len_of_word -= 1
            len_of_sentence = len(sentence)
    return result

if __name__ == "__main__":
    wordsdict = {'我们':5, '经常':2, '有':5, '有意见':3, '意见':4, '分歧':3}
    result = mmcut('我们经常有意见分歧', wordsdict, RMM=True)
    print('ok')