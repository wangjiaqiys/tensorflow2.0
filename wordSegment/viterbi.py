# _*_ coding:utf-8 _*_

def buildDAG(sentence, refDict):
    """
    构建有向无环图
    """
    result = {}
    len_of_sentence = len(sentence)
    for i in range(len_of_sentence): # 每次取一句话的的一个字符进行判断
        tmp = []
        flag = i 
        word = sentence[i]
        tmp.append(flag)
        while flag < len_of_sentence:
            if word in refDict.keys() and flag not in tmp:
                tmp.append(flag)
            flag += 1
            word = sentence[i:flag+1]
        result[i] = tmp
    return result

def viterbi(sentence, dag, wordsdict):
    """
    使用Viterbi算法找出最优切词结果<本质是动态规划>
    """
    len_of_sentence = len(sentence)
    route = {} # 存储最大路径
    route[len_of_sentence] = (0, 0)
    for idx in range(len_of_sentence-1, -1, -1): # 倒着取值 [6, 5, 4, 3, 2, 1, 0]
        # 列表推倒求最大概率对数路径
        # route[idx] = max([ (概率值，词语末字位置) for x in DAG[idx] ])
        # 以idx:(概率最大值，词语末字位置)键值对形式保存在route中)
        # route[x+1][0] 表示 词路径[x+1,N-1]的最大概率值,
        # [x+1][0]即表示取句子x+1位置对应元组(概率对数，词语末字位置)的概率对数
        tmp = []
        for x in dag[idx]:
            tmp.append((wordsdict.get(sentence[idx:x+1]) or 100 + route[x+1][0]))
        route[idx] = (min(tmp), x)
        # route[idx] = min(uy ((wordsdict.get(sentence[idx:x+1]) or 100) + route[x+1][0], x) for x in dag[idx]) # x 表示词的位置信息        

    x = 0
    segs = []
    while x < len_of_sentence:
        y = route[x][1]+1
        word = sentence[x:y]
        segs.append(word)
        x = y
    return route, segs

if __name__ == '__main__':
    sentence = '经常有意见分歧'
    wordsdict ={
        '北京': 5.058893689053568, '的': 3.643856189774725, '天': 7.643856189774724, '气': 7.643856189774724, 
        '天气': 4.058893689053568, '真': 4.643856189774724, '好': 4.321928094887363, '真好': 4.643856189774724, 
        '啊': 6.643856189774724, '真好啊': 5.643856189774724, '今': 6.643856189774724, '今天': 3.8365012677171206, 
        '课程': 4.058893689053568, '内容': 4.058893689053568, '有': 4.321928094887363, '很': 5.058893689053568, 
        '很有': 4.643856189774724, '意思': 4.058893689053568, '有意思': 7.643856189774724, '课': 6.643856189774724, 
        '程': 7.643856189774724, '经常': 3.643856189774725, '意见': 3.643856189774725, '意': 6.643856189774724, 
        '见': 7.643856189774724, '有意见': 5.643856189774724, '分歧': 4.643856189774724, '分': 5.643856189774724, 
        '歧': 7.643856189774724
        }
    result = buildDAG(sentence, wordsdict)
    # result = {0: [0, 1], 1: [1], 2: [2, 4], 3: [3, 4], 4: [4], 5: [5, 6], 6: [6]}
    route, segs = viterbi(sentence, result, wordsdict)
    print('ok')