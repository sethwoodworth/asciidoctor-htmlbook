HTMLBook Backends
=================

This repo holds the backend templates for converting `.asciidoc` files into `.html` files in the htmlbook flavor. The repo ships with 2 backends:

- `htmlbook` - a set of templates that can be used directly with the `asciidoctor` gem. This is a direct source conversion
- `htmlbook-autogen` - a set of templates that can only be used with the `orm_asciidoctor` gem. This provides some autogeneration abilities.

One-time Conversion of Books
----------------------------

In this folder there's a script that helps you convert book files written in asciidoc into htmlbook. Before you run it, it assumes you have installed the `asciidoctor` gem.

Convert a book by running the script like this:

```bash
$ ruby scripts/convert_folder PATH_TO_BOOK_REPO
```

So If my book repo exists in `/Documents/MyBook`, you would do the following:

```bash
$ ruby scripts/convert_book.rb /Documents/MyBook
```

Use Jinja2 to merge in metadata
----------------------------
The 'machine' directory contains a python script that will read a gitenberg yaml file and merge it with a template file using the Jinja2 template engine. A hook for this has been inserted into the htmlbook-autogen conversion. Assumes installation of ./machine/requirements.txt

run the command like this:
```bash
$ python ./gitberg-machine/machine.py -m /Documents/MyBook/metadata.yaml /Documents/MyBook/book.html
```