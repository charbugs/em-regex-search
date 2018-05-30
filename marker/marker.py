from collections import defaultdict
import re

def create_report(matched_tokens, pattern):
    
    if len(matched_tokens) == 0:
        return "<div>No matches for <b>%s</b>.</div>" % (pattern)

    fd = create_freq_dist(matched_tokens)
    fd = sorted(fd, key=lambda record: record[1], reverse=True)
    list_items = ["<li>%s (%d)</li>" % (record[0], record[1]) for record in fd]

    return """
        <div>
            <b>%d</b> matches for <b>%s</b>:
            <ul>
                %s
            </ul>
        </div>""" % (len(matched_tokens), pattern, ''.join(list_items))


def create_freq_dist(tokens):
    fd = defaultdict(int)
    for token in tokens:
        fd[token] += 1
    return fd.items()

def get_setup():
    return {
        'title': 'Regular Expression Search',
        'description': "<div>Find words that match a regular expression.</div>",
        'inputs': [
            {
                'id': 'pattern',
                'type': 'text',
                'label': 'Regular Expression',
            }
        ],
	"supportedLanguages": "any",
	"homepage": "https://github.com/charbugs/em-regex-search"
    }

def get_markup(markup_request):


    tokens = markup_request['tokens']
    pattern = markup_request['inputs']['pattern']

    if not pattern:
        return { 'error': 'You should give me a regular expression.' }

    try:
        expression = re.compile(pattern)
    except:
        return { 'error': "Doesn't look like a valid regular expression." }        

    matched_tokens = []
    matched_indizes = []

    for i in range(len(tokens)):
        if re.search(expression, tokens[i]):
            matched_tokens.append(tokens[i])
            matched_indizes.append(i)
    
    return { 
        'markup': [ { 'tokens': matched_indizes } ], 
        'report' : create_report(matched_tokens, pattern)
    }

