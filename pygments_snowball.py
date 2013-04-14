import re
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

class SnowballLexer(RegexLexer):
    """
    For Snowball source code.
    Note that this lexer assumes stringescapes brackets are {}.
    """

    name = 'Snowball'
    aliases = ['snowball']
    filenames = ['*.sbl']

    mimetypes = ['text/x-snowball']

    flags = re.MULTILINE | re.DOTALL

    tokens = {
        'root': [
            (r'[^\S\n]+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'(get)\b', Keyword.Namespace),
            (r'(stringescapes)(\s+)(\{)(\s*)(\})',
                bygroups(Keyword.Declaration,
                    Text, Punctuation, Text, Punctuation)),
            include('declaration'),
            (r'(backwardmode)\b', Keyword.Declaration),
            (r'(stringdef)(\s+)(\S+)',
                bygroups(Keyword.Declaration, Text, Name)),
            (r'(define)\b', Keyword.Declaration),
            (r'(true|false)\b', Keyword.Constant),
            (r"'", String, 'string'),
            (r'[\(\)\[\]]', Punctuation),
            (r'[0-9]+?', Number),
            (r'[+-<>=\*!/\$]', Operator),
            (r'hex\b', Number.Hex),
            (r'decimal\b', Number.Integer),
            include('command'),
            (r'(maxint|minint|cursor|limit|size|sizeof)\b',
                Operator.Word),
            (r'(among|for|as)\b', Keyword),
            (r'([a-zA-Z][a-zA-Z0-9_]*)', Name),
            (r'\n', Text),
        ],
        'declaration' : [
            (r'(strings|integers|booleans|routines|externals|'
             r'groupings)\b', Keyword.Declaration),
        ],
        'command': [
            (r'(or|and|not|test|try|do|fail|goto|gopast|'
             r'repeat|loop|atleast|insert|attach|delete|'
             r'hop|next|setmark|tomark|atmark|tolimit|'
             r'atlimit|setlimit|backwards|reverse|substring|'
             r'set|unset|non\-|non|\?)\b',
             Operator.Word),
        ],
        'string': [
            (r'\{\S*?\}', String),
            (r"[^'^\{]+", String),
            (r".*?'", String, '#pop'),
            (r'\n', Text, '#pop'),
        ],
    }
