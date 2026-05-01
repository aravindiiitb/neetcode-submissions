class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        if len(strs) == 0:
            return 'encoded_str'

        for str_item in strs:
            encoded_str_item = ''
            for c in str_item:                
                encoded_str_item = encoded_str_item + str(ord(c)) + '-'
            encoded_str_item = encoded_str_item[:-1]
            encoded_str  = encoded_str + encoded_str_item + '|'          
        return encoded_str[:-1]

    def decode(self, s: str) -> List[str]:
        if s == 'encoded_str':
            return []
            
        encoded_strs = s.split("|")        
        output = []
        if len(encoded_strs) == 0:
            return output

        for encoded_str in encoded_strs:
            temp_str = ''
            for charectar in encoded_str.split('-'):
                if charectar:
                    temp_str = temp_str + chr(int(charectar))
            output.append(temp_str)
        
        return output