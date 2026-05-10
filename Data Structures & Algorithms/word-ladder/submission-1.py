class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        strNeighMap = {i: [] for i in wordList}    
        strNeighMap[endWord] = []

        
        for i in range(len(wordList)):
            for j in range(i, len(wordList)):
                if len(wordList[i]) != len(wordList[j]):
                    continue
                editDistance = 0
                for k in range(len(wordList[i])):
                    if wordList[i][k] != wordList[j][k]:
                        editDistance += 1
                
                if editDistance == 1:
                    strNeighMap[wordList[i]].append(wordList[j])
                    strNeighMap[wordList[j]].append(wordList[i])


        q = deque()
        q.append(beginWord)
        
        dist = 1
        while q:
            nextQueue = deque()
            while q:
                closeStrs = q.popleft()
                if closeStrs == endWord:
                    return dist
                for nei in strNeighMap[closeStrs]:
                    nextQueue.append(nei)

            q = nextQueue
            dist += 1
        
        return 0

