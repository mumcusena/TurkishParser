from typing import List, Dict
import json


class CKYParser:
    def __init__(self, grammar):
        self.grammar = grammar
        
    def parse_sentence(self, sentence: str) -> List:
        if len(sentence) == 0:
            return []
        n = len(sentence)
        table = [[set() for _ in range(n + 1)] for _ in range(n)]
        
        #add each terminal to the table
        for j in range(1, n + 1):
            for lhs, rhs in self.grammar.items():
                if sentence[j - 1] in rhs:
                    table[j - 1][j].add(lhs)

            for i in range(j - 2, -1, -1):
                for k in range(i + 1, j):
                    for lhs, rhs_list in self.grammar.items():
                        for rhs in rhs_list:  
                            if len(rhs) == 2 and rhs[0] in table[i][k] and rhs[1] in table[k][j]:
                                print(rhs, i, j, k, table[i][k], table[k][j])
                                table[i][j].add(lhs)
                            else:
                                for item in table[i][k]: 
                                    table[i][j].add(item) 
        return table
    
    def evauate_parse(self, table: List)->bool:
        parse_result = table[0][-1]
        return 'S' in parse_result
    
turkish_grammar = ""

with open('Turkish_grammar.json', 'r') as file:
    turkish_grammar = json.load(file)
    
cky_parser = CKYParser(turkish_grammar)

sentence = "beyaz kedi yavaşça mama ye"
parse_table = cky_parser.parse_sentence(sentence.split())

#parse_table_output = [[list(cell) for cell in row] for row in parse_table]
print(parse_table)
print(cky_parser.evauate_parse(parse_table))

            
        

            