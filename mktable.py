"""
 * MarkdownTools 1.0.0
 * https://github.com/RobertoPrevato/MarkdownTools
 *
 * Copyright 2018, Roberto Prevato
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
"""
import argparse
from core.markdowntable import generate_table_of_contents_from_file

separator = ('*' * 50) + '\n'

parser = argparse.ArgumentParser(description= 'Markdown Table Of Contents Generator.',
                                 epilog = '{}\n{}'.format('author: Roberto Prevato roberto.prevato@gmail.com', separator))

parser.add_argument('-f', '--filepath', dest='filepath', required=True,
                    help='path to file from which generate a table of contents')

parser.add_argument('-s', '--separator', dest='separator', required=False,
                    help='separator for indentation')

parser.add_argument('-i', '--indent', dest= 'indent', required=False,
                    help='indentation size')

def main(options):
    print(generate_table_of_contents_from_file(options.filepath, options.separator, options.indent))

main(parser.parse_args())