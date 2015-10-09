Pygments Snowball Plugin
========================

`Pygments <http://pygments.org/>`_ Lexer Plugin
for `Snowball <http://snowballstem.org/>`_,
a domain-specific language for
`stemming words <http://en.wikipedia.org/wiki/Stemming>`_.

Note that strictly this lexer is incomplete,
since it assumes ``stringescapes`` brackets are ``{}``.
Practically it will not matter considering
all official Snowball codes thus far use ``{}`` brackets
(or do not use the ``stringescapes`` directive).

Usage
-----

Sample Usage::

    #pip install pygments
    #python setup.py install
    $pygmentize -O full=True -l snowball -f html -o porter.html porter.sbl

Actually, this plugin recognizes ``.sbl`` extension, so you can write::

    $pygmentize -O full=True -f html -o porter.html porter.sbl

For more information, see `the official pygments documentation
<http://pygments.org/docs/>`_.

License
=======

BSD 2-Clause License

See ``LICENSE``


All Snowball codes under the directory ``./sample_output`` are
licensed by BSD 2-Clause License with
Copyright (c) 2001, Dr Martin Porter and
Copyright (c) 2002, Richard Boulton.

See ``./sample_output/license.php``

Authors
=======

`Hajime Senuma <mailto:hajime.senuma@gmail.com>`_
