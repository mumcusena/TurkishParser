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
                                # print(rhs, i, j, k, table[i][k], table[k][j], lhs)
                                table[i][j].add(lhs)
                            else:
                                for item in table[i][k]: 
                                    table[i][j].add(item) 
                                # for item in table[k][j]: 
                                #     table[i][j-1].add(item) 
        return table
    
    def evaluate_parse(self, table: List)->bool:
        return "S" in table[0][-1]
    
turkish_grammar = ""

with open('grammar.json', 'r') as file:
    turkish_grammar = json.load(file)
    
cky_parser = CKYParser(turkish_grammar)

# sentence = "sen yavaşça mama ye di n"
sentence = "yüksek ses le müzik dinle"

correct_tests_sentences = ["sen yavaşça mama ye di n",
                    "yüksek ses le müzik dinle me",
                    "kitap ı nı getir me sin",
                    "kitap ı aldı",
                    "ben kedi m le okul a git ti m",
                    "siyah kedi yarın gel ecek mi",
                    "bu agaç ın altında her gece mehtap ı izle r di k",
                    "destan lar milli kültür ümüz ü ve tarih imiz i anlat ır"
                   ]
false_tests_sentences = ["sen yavaşça mama ye di m",
                        "anne m bugün okul a git ti n"
                   ]

print("Correct sentences:")
for correct_sentence in correct_tests_sentences:
    parse_table = cky_parser.parse_sentence(correct_sentence.split())
    print(f"{correct_sentence}: {cky_parser.evaluate_parse(parse_table)}")

print("False sentences:")
for false_sentence in false_tests_sentences:
    parse_table = cky_parser.parse_sentence(false_sentence.split())
    print(f"{false_sentence}: {cky_parser.evaluate_parse(parse_table)}")


            
        

            