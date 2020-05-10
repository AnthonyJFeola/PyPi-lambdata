# lambdata-AnthonyJFeola
Lambda School DSPT5 Unit 3 Sprint 1 Assignment

Hyperlink removal tool that takes a pandas series of text as an input and returns the text without hyperlinks

## Installation 
```py
pip install lambdata-AnthonyJFeola
```
## USAGE 
```py
from lambdata-AnthonyJFeola.hyperlink_handler import remove_hyperlinks
from pandas import DataFrame

example_df = DataFrame({'a': ['Check out https://www.wikipedia.org/', 'Go to https://www.google.com/']})

example_df['a'] = remove_hyperlinks(example_df['a'])

print(example_df)
```