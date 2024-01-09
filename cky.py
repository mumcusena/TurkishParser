from typing import List, Dict
from test_data import sentence_data, expected_results
import json

class CKYParser:
    """This class implements the cky parsing algorithm for the given context free grammar and contains methods for generating and evaluating the parse table
    """
    
    def __init__(self, grammar: Dict):
        """The constructor for CKYParser class

        Args:
            grammar (Dict): context free grammar in the form of a dictionary
        """
        self.grammar = grammar
        
    def parse_sentence(self, sentence: str) -> List:
        """Function that parses the given sentence by using cky parsing algortihm and returns the parse table

        Args:
            sentence (str): the sentence to be parsed

        Returns:
            List: the parse table as a 2D array
        """
        
        sentence = sentence.split()
        if len(sentence) == 0:
            return []
        n = len(sentence)
        table = [[set() for _ in range(n + 1)] for _ in range(n)]
        
        for j in range(1, n + 1):
            for lhs, rhs in self.grammar.items():
                if sentence[j - 1] in rhs:
                    table[j - 1][j].add(lhs)

            for i in range(j - 2, -1, -1):
                for k in range(i + 1, j):
                    for lhs, rhs_list in self.grammar.items():
                        for rhs in rhs_list:  
                            if len(rhs) == 2 and rhs[0] in table[i][k] and rhs[1] in table[k][j]:
                                table[i][j].add(lhs)
                            else:
                                for item in table[i][k]: 
                                    table[i][j].add(item) 
        return table
    
    def evaluate_parse(self, table: List) -> bool:
        """Method for evaluating if the sentence can be parsed by checking if the last cell of parse table contains the start symbol, S,  of the grammar.

        Args:
            table (List): The parse table that is generated for the sentence using the cky algorithm.

        Returns:
            bool: returns True if the sentence can be parsed by the grammar, False otherwise.
        """
        
        return "S" in table[0][-1]
    
    
if __name__ == "__main__":
    turkish_grammar = ""
    with open('grammar.json', 'r') as file:
        turkish_grammar = json.load(file)
        
    cky_parser = CKYParser(turkish_grammar)

    test_results = []
    for sentence in sentence_data:
        parse_table = cky_parser.parse_sentence(sentence)
        result = cky_parser.evaluate_parse(parse_table)
        test_results.append(result)

    accuracy = sum([1 if result == expected_results[i] else 0 for i, result in enumerate(test_results)]) / len(test_results)
    print(f"Accuracy of the test data: {accuracy:.2f}")
