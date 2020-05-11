# lambdata-AnthonyJFeola
Lambda School DSPT5 Unit 3 Sprint 1 Assignment

1. Hyperlink removal tool that takes a pandas series of strings as an input and returns the series without hyperlinks.

2. Punctuation removal tool that takes a pandas series of strings as an input and returns the series without punctuation.

## Installation 
```py
pip install -i https://test.pypi.org/simple/ lambdata-AnthonyJFeola
```
## USAGE 
```py
from lambdata_AnthonyJFeola.hyperlink_handler import remove_hyperlinks
from pandas import DataFrame

example_df = DataFrame({'a': ['Check out https://www.wikipedia.org/', 'Go to https://www.google.com/']})

example_df['a'] = remove_hyperlinks(example_df['a'])

print(example_df)

from lambdata_AnthonyJFeola.punctuation_handler import remove_punctuation
from pandas import DataFrame

example_df = DataFrame({'a': ["Hey! What's up? Check out https://www.wikipedia.org/", "Let's see what's at https://www.google.com/"]})

example_df['a'] = remove_punctuation(example_df['a'])

print(example_df)
```