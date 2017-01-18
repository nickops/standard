#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OCDS documentation build configuration file, created by
# sphinx-quickstart on Fri Dec 11 15:07:47 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.md'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'OCDS'
html_show_copyright = False
copyright = ''
author = 'OCDS'

html_show_sphinx = False

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'OCDSdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'OCDS.tex', 'OCDS Documentation',
   'OCDS', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ocds', 'OCDS Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'OCDS', 'OCDS Documentation',
   author, 'OCDS', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

source_parsers = {
    '.md': CommonMarkParser,
    }


import standard_theme

html_theme = "standard_theme"

html_theme_path = [standard_theme.get_html_theme_path()]


locale_dirs = ['../locale/', os.path.join(standard_theme.get_html_theme_path(), 'locale')]
gettext_compact = False     # optional.



from sphinx.directives.code import LiteralInclude
from docutils.parsers.rst import directives, Directive
from docutils.parsers.rst.roles import set_classes
from docutils.parsers.rst.directives.tables import CSVTable
from docutils import nodes, statemachine
import io
import re
import csv
import json
from jsonpointer import resolve_pointer
from collections import OrderedDict
import requests
import collections
from os.path import abspath, dirname, join


current_dir = dirname(abspath(__file__))

GIT_REF = "master"

location = "http://standard.open-contracting.org/extension_registry/{}/extensions.json".format(GIT_REF)
try:
    extension_json = requests.get(location, timeout=1).json()
except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
    print("**********  Internet connection not found *************") 
    extension_json = {"extensions": []}


class JSONInclude(LiteralInclude):
    option_spec = {
        'jsonpointer': directives.unchanged,
        'expand': directives.unchanged,
        'title': directives.unchanged,
    }

    def run(self):
        with open(self.arguments[0]) as fp:
            json_obj = json.load(fp, object_pairs_hook=OrderedDict)
        filename = str(self.arguments[0]).split("/")[-1].replace(".json","")
        try:
            title = self.options['title']
        except KeyError as e:
            title = filename
        pointed = resolve_pointer(json_obj, self.options['jsonpointer'])
        code = json.dumps(pointed, indent='    ')
        # Ideally we would add the below to a data-expand element, but I can't see how to do this, so using classes for now...
        class_list = self.options.get('class', [])
        class_list.append('file-'+title)
        expand = str(self.options.get("expand","")).split(",")
        class_list = class_list + ['expandjson expand-{0}'.format(s.strip()) for s in expand]
        literal = nodes.literal_block(code, code, classes=class_list)
        literal['language'] = 'json' 
        literal['caption'] = 'TEST'
        return [ literal ]



class ExtensionList(Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {'class': directives.class_option,
                   'name': directives.unchanged,
                   'list': directives.unchanged}


    def run(self):
        extension_list_name = self.options.pop('list', '')
        set_classes(self.options)

        admonition_node = nodes.admonition('', **self.options)
        self.add_name(admonition_node)

        title_text = self.arguments[0]

        textnodes, _ = self.state.inline_text(title_text,
                                              self.lineno)

        title = nodes.title(title_text, '', *textnodes)
        title.line = 0
        title.source = 'extension_list_' + extension_list_name
        admonition_node += title
        if not 'classes' in self.options:
            admonition_node['classes'] += ['admonition', 'note']

        admonition_node['classes'] += ['extension_list']
        admonition_node['ids'] += ['extensionlist-' + extension_list_name]

        definition_list = nodes.definition_list()
        definition_list.line = 0

        num = 0
        for num, extension in enumerate(extension_json['extensions']):
            if not extension.get('core'):
                continue
            category = extension.get('category')
            if extension_list_name and category != extension_list_name:
                continue

            name = extension['name']['en']
            description = extension['description']['en']

            some_term, _ = self.state.inline_text(name,
                                                  self.lineno)

            some_def, _ = self.state.inline_text(description,
                                                  self.lineno)

            link = nodes.reference(name, '', *some_term)
            path_split = self.state.document.attributes['source'].split('/')
            root_path = "../" * (len(path_split) - path_split.index('docs') - 2)

            link['refuri'] = root_path + 'extensions/' + extension.get('slug', '')
            link['translatable'] = True
            link.source = 'extension_list_' + extension_list_name
            link.line = num + 1

            term = nodes.term(name, '', link)

            definition_list += term

            text = nodes.paragraph(description, '', *some_def)
            text.source = 'extension_list_' + extension_list_name
            text.line = num + 1
            definition_list += nodes.definition(description, text)

        admonition_node += definition_list

        community = "The following are community extensions and are not maintained by Open Contracting Partnership."
        community_text, _ = self.state.inline_text(community,
                                              self.lineno)

        community_paragraph = nodes.paragraph(community, *community_text)
        community_paragraph['classes'] += ['hide']
        community_paragraph.source = 'extension_list_' + extension_list_name
        community_paragraph.line = num + 2

        admonition_node += community_paragraph

        return [admonition_node]

def format(text):
    return re.sub(r'\[([^\[]+)\]\(([^\)]+)\)', r'`\1 <\2>`__', text.replace("date-time","[date-time](#date)"))

def gather_fields(json, path="", definition=""): 

    definitions = json.get('definitions')
    if definitions:
        for key, value in definitions.items():
            yield from gather_fields(value, definition=key)

    properties = json.get('properties')
    if properties:
        for field_name, field_info in properties.items():
            yield from gather_fields(field_info, path+'/'+field_name, definition=definition)
            for key, value in field_info.items():
                if isinstance(value, dict):
                    yield from gather_fields(value, path+'/'+field_name, definition=definition)

            types = field_info.get('type','')
            if isinstance(types, list):
                types = format(", ".join(types).replace(", null","").replace("null,",""))
            else:
                types = format(types)

            description = field_info.get("description")
            if description:
                yield [(path+'/'+field_name).lstrip("/"), definition, format(description), types]



class ExtensionTable(CSVTable):

    option_spec = {'widths': directives.positive_int_list,
                   'extension': directives.unchanged,
                   'schema': directives.unchanged,
                   'ignore_path': directives.unchanged,
                  }

    def get_csv_data(self):
        headings = ["Field", "Definition", "Description", "Type"]
        extension = self.options.get('extension')
        if not extension:
            raise Exception("No extension configuration when using extensiontable directive") 

        if not extension_json['extensions']:
            return [",".join(headings)], "Extension {}".format(extension)

        for num, extension_obj in enumerate(extension_json['extensions']):
            if not extension_obj.get('core'):
                continue
            if extension_obj['slug'] == extension:
                break
        else:
            raise Exception("Extension {} does not exist in the registry".format(extension)) 

        extension_patch = requests.get(extension_obj['url'].rstrip("/") + "/" + "release-schema.json").json()
        data = []
        for row in gather_fields(extension_patch):
            data.append(row)

        data.sort(key=lambda a: (a[1], tuple(a[0].split('/'))))
        ignore_path = self.options.get('ignore_path')
        if ignore_path:
            for row in data:
                row[0] = row[0].replace(ignore_path, "")

        data.insert(0, headings)

        output = io.StringIO()
        output_csv = csv.writer(output)
        for line in data:
            output_csv.writerow(line)
        self.options['header-rows'] = 1

        return output.getvalue().splitlines(), "Extension {}".format(extension)

    def parse_csv_data_into_rows(self, csv_data, dialect, source):
        # csv.py doesn't do Unicode; encode temporarily as UTF-8
        csv_reader = csv.reader([self.encode_for_csv(line + '\n')
                                 for line in csv_data],
                                dialect=dialect)
        rows = []
        max_cols = 0
        for row_num, row in enumerate(csv_reader):
            row_data = []
            for cell_num, cell in enumerate(row):
                if row_num == 0 or (cell_num != 0 and cell_num != 3):
                    new_source = source
                else:
                    new_source = ""
                # decode UTF-8 back to Unicode
                cell_text = self.decode_from_csv(cell)
                cell_data = (0, 0, 0, statemachine.StringList(
                    cell_text.splitlines(), source=new_source))
                row_data.append(cell_data)
            rows.append(row_data)
            max_cols = max(max_cols, len(row))
        return rows, max_cols


directives.register_directive('jsoninclude', JSONInclude)
directives.register_directive('extensionlist', ExtensionList)
directives.register_directive('extensiontable', ExtensionTable)


# app setup hook
def setup(app):
    app.add_transform(AutoStructify)


