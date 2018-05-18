from collections import defaultdict
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
        ],
	"supportedLanguages": "any",
	"homepage": "https://github.com/charbugs/em-regex-search"
    }

def get_markup(markup_request):


    tokens = markup_request['tokens']
    pattern = markup_request['inputs']['re']

    if not pattern:
        return { 'error': 'You should give me a pattern.' }

    tokens_to_mark = []
    matching_types_fd = defaultdict(int)

    for i in range(len(tokens)):
        if re.search(pattern, tokens[i]):
            tokens_to_mark.append(i)
            matching_types_fd[tokens[i]] += 1
    
    report = """
        <div>
            <ul>
                <li><b>%d</b> of %d tokens match the pattern: %s</li>
		<li>Matching tokens consist of <b>%d</b> different types</li>
                <li>Most common type is <b>%s</b></li>
            </ul>
        </div>
    """ % (
        len(tokens_to_mark), 
        len(tokens), 
        pattern,
        len(matching_types_fd),
        get_most_common_type(matching_types_fd)
    )

    return { 
        'markup': [ { 'tokens': tokens_to_mark } ], 
        'report' : report 
    }

def get_most_common_type(matching_types_fd):
    sorted_items = sorted(matching_types_fd.items(), key=lambda item: item[1])
    return sorted_items[-1][0] if sorted_items else ''

