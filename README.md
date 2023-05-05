# cicadatoolz
Unsorted and unpolished tools and files for working with Cicada 3301's unsolved Liber Primus pages.


bpages- pages produced by buffers.py, see below

ppages- unsolved pages converted to 'pseudo-readable' alphabet

runepages- pages in original rune alphabet. Files starting with s are the original/solved pages. Files starting with sect are unsolved pages combined by apparent section, starting with that file's number. Don't remember where I got these from. Gee I do hope the transcription's correct

srpages- solved pages in rune form. Files ending in f are for vig length test, see below


00L, etc- unsolved sections in word length format


brutal.py- low-quality vignere brute force tester

buffers.py- autokey test

decribulator.py- comedy cribber, matches random words from solved 'runeglish' pages to words in unsolved pages by length. Currently has one special rule for the single '7' with a single-rune 'word' following it giving a chance for that rune to be changed to 'th' as in '7th'


lengths.py- code used to produce the L pages

sentencer.py- separate runeglish sections by sentences. will be used to create easier files for working with, eg for finding a given point of interest, eventually

vig length test.py- attempt to implement http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/ I think I might have gotten the math wrong, as the value climbs with larger skips/shorter strings regardless of key length. Will revise later

vignere solveds.py- re-solves the solved pages, both the original and the two last pages of the big dump.
