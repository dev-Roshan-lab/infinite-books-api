from flask import Flask, jsonify
from libgen_api import LibgenSearch

app = Flask(__name__)

@app.route('/')
def home():
    return "working"

@app.route('/<path:data>')
def find_book(data):
    print('data')

    filters = list(data.split(','))
    print(filters)
    lb = LibgenSearch()

    title = filters[0]
    author = filters[1]
    year = filters[2]
    lang = filters[3]
    extension = filters[4]

    api_filters = {"Year":year, "Extension":extension, "Language":lang, "Author":author} #{"Title" : title, "Author" : author, "ID" : book_id, "Year" : year, "Language": lang}

    results = lb.search_title_filtered(title, api_filters, exact_match=False) #search_title_filtered(title, api_filters, exact_match = False)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True) 