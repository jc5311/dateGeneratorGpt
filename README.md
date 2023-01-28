# dateGeneratorGpt

The script dateGenerator.py generates 4-6 random dates for all 12 months of a 
year. A user may specify a year for which to produce the dates. If a year is
not specified, the current year is used by default.

Note: This script was produced primarily by the openAI "chatGPT" bot with
edits from myself to allow user input and format printed output.

Prompts used:
"Can you write a python script which produces 4 to 6 random dates for each month of the year?"
"Can you rewrite the previous date script such that no overlapping dates are produced?"
The last prompt produced the two functions which were ultimately used.