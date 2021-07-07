## Merge CSV
Merge spreadsheets
Can be done manually or using (Unix)

	cat FILE1.csv FILE2.csv FILE3.csv FILE4.csv > FILE_MERGED.csv

## Deduplicate

Remove leading and trailing spaces, sort the spreadsheet and remove adjacent duplicates.
	
	cat INPUT.csv | sed 's/,[ \t]*/,/g' | sed 's/[ \t]*,/,/g' | sort -u --field-separator=',' --key=3 > OUTPUT.csv

The command is made of the following parts:
* open file `cat INPUT.csv`
* remove leading spaces `sed 's/,[ \t]*/,/g'`
* remove trailing spaces `Sed 's/[ \t]*,/,/g'`
* sort by column, removing adjacent duplicates (-u) `sort -u --field-separator=',' --key=3`
* print to new file `> OUTPUT.csv`
