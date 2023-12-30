# TurkishParser

## Parts of Speech in Turkish
- noun (isim or ad "name");
- pronoun (zamir "inner being", or adıl from ad);
- adjective (sıfat "role, quality", or önad "front-noun");
- verb (fiil "act, deed", or eylem "action" from eyle- "make, do");
- adverb (zarf "envelope", or belirteç from belir- "determine");
- postposition (ilgeç from ilgi "interest, relation");
- conjunction (bağlaç from bağ "bond");
- particle (edat, or ilgeç);
- interjection (nidâ, or ünlem from ün "fame, repute, sound").

## Terminals:
Det : Determiners like "bir", "bu", "o"
Noun : Nouns like "kitap", "ev", "kedi"
Pron : Personal pronouns like "ben", "sen", "o"
Verb : Verbs in their base form like "yaz", "oku", "git"
AUX : Auxiliary verbs like "ol", "git"
Suffixes : Various suffixes (e.g., "-im", "-sin", "-dir", "-iyor", "-di")

## Non-terminals:
S : Sentence
NP : Noun Phrase
VP : Verb Phrase
V : Verb
A : Auxiliary Verb

## Rules:
Sentence:
- S -> NP VP
Noun Phrase:
- NP -> Det Noun
- NP -> Pron
Verb Phrase:
- VP -> V
- VP -> A VP
- VP -> V Suffix
- VP -> A Suffix
- VP -> V Suffix Suffix
- VP -> A Suffix Suffix
Verbs:
- V -> "yaz"
- V -> "oku"
- ... 
Auxiliary Verbs:
- A -> "ol"
- A -> "git"
- ... 
Suffixes: (suffix may be recursive)
- Suffix -> "-im"
- Suffix -> "-sin"
- Suffix -> "-di"
- Suffix -> "-iyor"
- ... 
Tenses:
- Suffix -> "-er" (present continuous)
- Suffix -> "-di" (past)
- Suffix -> "-acak" (future)
