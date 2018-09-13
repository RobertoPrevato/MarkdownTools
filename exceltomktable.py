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
from lib.exceltomarkdown import generate_tables_from_excel_file
from lib.exceltomarkdown import generate_tables_from_ods_file

separator = ('*' * 50) + '\n'

parser = argparse.ArgumentParser(description= 'Excel to Markdown tables generator.',
                                 epilog = '{}\n{}'.format('author: Roberto Prevato roberto.prevato@gmail.com', separator))

parser.add_argument('-f', '--filepath', dest='filepath', required=True,
                    help='path to file from which generate a table of contents')

def main(options):
    if options.filepath.endswith('.ods'):
        print(generate_tables_from_ods_file(options.filepath))
    else:
        print(generate_tables_from_excel_file(options.filepath))

main(parser.parse_args())