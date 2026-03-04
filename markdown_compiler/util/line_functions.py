'''
Each of the functions in this file takes a single line of input and
transforms the line in some way.
'''


def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.

    HINT:
    This is the simplest function to implement in this assignment.
    Use a slices to extract the first part of the line,
    then use if statements to check if they match the
    appropriate header markdown commands.

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
        # answer: strings are *immutable* in python; i.e. they can never
        # change so functions that seem like they should change the string
        # actually just return a new string
        # without line = line.replace the replacement is not assigned
        # to the line
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
    Italics require carefully tracking the beginning and
    ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that
    we implemented in class.
    It's a tiny bit more complicated since we are not just
    deleting substrings from the text,
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
    accumulator = ''
    has_opened = False  # meaning: have we seen a * yet?
    for char in line:
        # print is useful for debugging to help understand what code is doing
        # print(char)
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


def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    HINT:
    This function is almost exactly the same as `compile_italic_star`.

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''
    accumulator = ''
    has_opened = False  # meaning: have we seen a _ yet?
    for char in line:
        # print is useful for debugging
        # print(char)
        # super common mistake is to either put '' where they don't belong
        # or not use '' when needed
        if char == '_':
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


def compile_strikethrough(line):
    accumulator = ''
    has_opened = False
    for char in line:
        if char == '~~':
            if not has_opened:
                accumulator += '<ins>'
                has_opened = True
            else:
                accumulator += '</ins>'
                has_opened = False
        else:
            accumulator += char
    return accumulator


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    '''
    accumulator = ''
    has_opened = False
    for char in line:
        if char == '**':
            if not has_opened:
                accumulator += '<b>'
                has_opened = True
            else:
                accumulator += '</b>'
                has_opened = False
            # clever way:
            # has_opened = not has_opened
        else:
            accumulator += char
    return accumulator


def compile_bold_underscore(line):
    '''
    Convert "__bold__" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_underscore('__This is bold!__ This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_underscore('__This is bold!__')
    '<b>This is bold!</b>'
    >>> compile_bold_underscore('This is __bold__!')
    'This is <b>bold</b>!'
    >>> compile_bold_underscore('This is not __bold!')
    'This is not __bold!'
    >>> compile_bold_underscore('__')
    '__'
    '''
    accumulator = ''
    has_opened = False
    for char in line:
        if char == '__':
            if not has_opened:
                accumulator += '<b>'
                has_opened = True
            else:
                accumulator += '</b>'
                has_opened = False
            # clever way:
            # has_opened = not has_opened
        else:
            accumulator += char
    return accumulator


def compile_code_inline(line):
    accumulator = ''
    has_opened = False
    for char in line:
        if char == '`':
            if not has_opened:
                accumulator += '<code>'
                has_opened = True
            else:
                accumulator += '</code>'
                has_opened = False
        else:
            accumulator += char
    return accumulator


def compile_links(line):
    start_text = line.find("[")
    end_text = line.find("]", start_text + 1)
    end_link = line.find(')', end_text + 2)
    if end_link == -1:
        return line

    text = line[start_text + 1:end_text]
    link = line[end_text + 2:end_link]

    return (
        line[:start_text] + f'<a href="{link}">{text}</a>' + line
        [end_link + 1:]
    )


def compile_images(line):
    start_text = line.find("!")
    if start_text + 1 >= len(line) or line[start_text + 1] != "[":
        return line

    end_text = line.find("]", start_text + 2)
    if end_text + 1 >= len(line) or line[end_text + 1] != "(":
        return line

    end_link = line.find(')', end_text + 2)
    if end_link == -1:
        return line

    text = line[start_text + 2:end_text]
    link = line[end_text + 2:end_link]

    return (
        line[:start_text] + f'<img src="{link}" alt="{text}" />' + line
        [end_link + 1:]
    )
