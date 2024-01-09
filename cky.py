from typing import List, Dict
import json
from test_data import sentence_data, expected_results

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
                                # print(rhs, i, j, k, table[i][k], table[k][j], lhs)
                                table[i][j].add(lhs)
                            else:
                                for item in table[i][k]: 
                                    table[i][j].add(item) 
        return table
    
    def evaluate_parse(self, table: List)->bool:
        return "S" in table[0][-1]
    
turkish_grammar = ""
with open('grammar.json', 'r') as file:
    turkish_grammar = json.load(file)
    
cky_parser = CKYParser(turkish_grammar)

test_results = []
for sentence in sentence_data:
    parse_table = cky_parser.parse_sentence(sentence.split())
    result = cky_parser.evaluate_parse(parse_table)
    test_results.append(result)

accuracy = sum([1 if result == expected_results[i] else 0 for i, result in enumerate(test_results)]) / len(test_results)
print(f"Accuracy of test data: {accuracy:.2f}")

#problematic:
correct_sentence = "tarihi bir roman lar oku du m"
parse_table = cky_parser.parse_sentence(correct_sentence.split())
result = cky_parser.evaluate_parse(parse_table)       
print(result)
                    