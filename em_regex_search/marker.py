import re

def get_setup():
    return {
        'title': 'Regular Expression Search',
        'description': "<div>Find words that match a regular expression.</div>",
        'inputs': [
            {
                'id': 're',
                'type': 'text',
                'label': 'Regular Expression',
            }
        ]
    }

def get_markup(markup_request):


    tokens = markup_request['tokens']
    pattern = markup_request['inputs']['re']

    if not pattern:
        return { 'error': 'You should give me a pattern.' }

    tokens_to_mark = []

    for i in range(len(tokens)):
        if re.search(pattern, tokens[i]):
            tokens_to_mark.append(i)  
    
    report = '%d of %d tokens match the pattern: %s' % (
        len(tokens_to_mark), 
        len(tokens), 
        pattern
    )

    return { 
        'markup': [ { 'tokens': tokens_to_mark } ], 
        'report' : report 
    }
