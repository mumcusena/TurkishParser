# TurkishParser
An implementation of the CKY parsing algorithm for the Turkish language using our custom Context-Free Grammar (CFG)

The details for the CFG are as follows: 
## Terminals for Turkish grammar:
- ADV past: d ̈un
- ADV future: seneye, yarın
- ADV: yava ̧s ̧ca, epeyce
- POSPRON first singular: m, um, im, ım
- POSPRON second singular: n, sin
- SUFFIX imp third singular: sin, sın, sun, s ̈un
- POSPRON first plural: k
- POSPRON second plural: niz
- SUFFIX possessive: ım,  ̈um ̈uz, imiz, ın, in, nun, nin, im, m, i, ı
- SUFFIX accusative:  ̈u, i, ı
- SUFFIX dative: a, ya, e
- SUFFIX imp second singular: [Empty string for suffix]
- SUFFIX location: da, ta
- SUFFIX source: tan, ten, nden, den, dan
- SUFFIX with: le
- CONJ: ve
- ADJ: beyaz, siyah, y ̈uksek, milli, tarihi, her
- SUFFIX plural: ler, lar
- TENSE future: acak, ecek, yecek, yacak
- TENSE continuous: uyor, yor
- TENSE simple: ır, r, sınız
- TENSE past: dı, di, ti, du
- QUESTION suffix: mı
- QUESTION word: nezaman
- SUFFIX negation: me, ma
- SUFFIX copular: dir
- PRON first singular: ben
- PRON second singular: sen
- PRON third singular: o
- PRON first plural: biz
- PRON second plural: siz
- PRON third plural: onlar

## Non-terminals for Turkish Grammar:
- S
- VP past
- VP future
- VP
- VP first singular
- VP second singular
- SUFFIX past
- SUFFIX future
- SUFFIX continuous
- SUFFIX simple
- NP first singular
- NP second singular
- NP third singular
- SUFFIX past first singular
- SUFFIX past second singular
- NP future
- NP past
- VERB imperative second singular
- VERB imperative third singular
- NP