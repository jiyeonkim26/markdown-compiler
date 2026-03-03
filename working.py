'''
Each of the functions in this file takes a single line of input and transforms the line in some way.
'''

def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.

    HINT:
    This is the simplest function to implement in this assignment.
    Use a slices to extract the first part of the line,
    then use if statements to check if they match the appropriate header markdown commands.

    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''
    if line[:2] == '# ':
        # why doesn't this line do anything?
        # answer: strings are *immutable* in python; i.e. they can never change
        # so functions that seem like they should change the string
        # actually just return a new string
        # without line = line.replace the replacement is not assigned to the line
        line = line.replace('# ', '<h1> ') + '</h1>'
    if line[:3] == '## ':
        line = line.replace('## ', '<h2> ') + '</h2>'
    if line[:4] == '### ':
        line = line.replace('### ', '<h3> ') + '</h3>'
    if line[:5] == '#### ':
        line = line.replace('#### ', '<h4> ') + '</h4>'
    if line[:6] == '##### ':
        line = line.replace('##### ', '<h5> ') + '</h5>'
    if line[:7] == '###### ':
        line = line.replace('###### ', '<h6> ') + '</h6>'
    return line


def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    # the reason this is harder than the previous function is that the markdown
    # code can appear anywhere in the string, not just hte beginning
    # also, there are two pieces of info we need to match:
    # the first * is the <i>
    # the second * is the </i>
    # all of these functions are easiest to implement with the acucmulator pattern
    
    accumulator = ''
    has_opened = False # meaning: have we seen a * yet?
    for char in line:
        # print is useful for debugging to help you understand what the code is doing
        #print(char)
        # super common mistake is to either put '' where they don't belong
        # or not use '' when needed
        if char == '*':
            if not has_opened:
                accumulator += '<i>'
                has_opened = True
            else:
                accumulator += '</i>'
                has_opened = False
            # clever way:
            # has_opened = not has_opened
        else:
            accumulator += char
    return accumulator
