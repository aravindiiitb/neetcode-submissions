class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        resultMap = {}
        for strEle in strs:
            sortedStrElement = "".join(sorted(strEle))
            if sortedStrElement in resultMap:
                stringsList = resultMap[sortedStrElement]
                stringsList.append(strEle)
                resultMap[sortedStrElement] = stringsList
            else:
                resultMap[sortedStrElement] = [strEle]
        
        output = []        
        for value in resultMap.values():
            output.append(value)
        
        return output