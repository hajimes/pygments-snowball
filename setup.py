from setuptools import setup
setup(
    name="Pygments Snowball Plugin",
    version = "1.0",
    scripts = ['pygments_snowball.py'],
    entry_points = """
        [pygments.lexers]
        snowball_lexer = pygments_snowball:SnowballLexer
    """,
    description = 'Pygments Lexer Plugin for Snowball',
    license = 'BSD 2-Clause License',
    author = 'Hajime Senuma',
    author_email = 'hajime.senuma@gmail.com',
)    
