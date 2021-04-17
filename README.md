# infinite-books-api
infinite books api is api created in python to search book from libgen

## End points
The API accepts a string seperated by comma this string is split into a list of 4 filters need by the [libgen-api](https://pypi.org/project/libgen-api/)

**example** : **rich dad poor dad,Kiyosaki,2017,english**

## Rules
- The first entry should the title name of the book
- second entry follows the author name
- third looks for year of publication in libgen database
- finally the language you want the book to be

## Result
`
[{"Author":"Kiyosaki,Robert T","Edit":"https://library.bz/main/edit/2E428F0A338D6A8866D4469F13F727DB","Extension":"epub","ID":"2603381","Language":"English","Mirror_1":"http://library.lol/main/2E428F0A338D6A8866D4469F13F727DB","Mirror_2":"http://libgen.lc/ads.php?md5=2E428F0A338D6A8866D4469F13F727DB","Mirror_3":"https://3lib.net/md5/2E428F0A338D6A8866D4469F13F727DB","Mirror_4":"https://libgen.pw/item?id=2603381","Mirror_5":"http://bookfi.net/md5/2E428F0A338D6A8866D4469F13F727DB","Pages":"","Publisher":"Perseus Books, LLC;Plata Publishing","Size":"5 Mb","Title":"Rich dad poor dad: Rich dad's prophecy: why the biggest stock market crash in history is still coming-- and how you can prepare yourself and profit from it!","Year":"2017"}]
`

### made with python 3.6
