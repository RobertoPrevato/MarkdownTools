from typing import List
from collections import OrderedDict
import urllib.parse


class Header:

    __slots__ = ('level', 'name')

    def __init__(self, level, name):
        self.level = level
        self.name = name

    def __repr__(self):
        return f'<H{self.level} {self.name}>'


header_types = OrderedDict([(str('#') * x, x) for x in reversed(range(1, 7))])


def get_headers_from_lines(lines: List[str]) -> List[Header]:
    headers = []

    for line in lines:
        if 'Table of contents' in line:
            continue
        for k, v in header_types.items():
            if line.startswith(k):
                headers.append(Header(v, line.lstrip('# ').strip()))
                break

    return headers


def get_headers_from_file(source_file: str) -> List[Header]:
    with open(source_file, mode='rt', encoding='utf-8') as input_md:
        return get_headers_from_lines(input_md.readlines())


def link_name(value):
    if not value:
        return ''

    return urllib.parse.quote(value.replace(' ', '-')).lower().replace('%0a', '')


def header_link(header: Header):
    return f'[{header.name}](#{link_name(header.name)})'


def generate_index(headers: List[Header]) -> str:
    lines = []

    for header in headers:
        lines.append((((header.level - 1) * 4) * ' ') + f'1. {header_link(header)}')

    return '\n'.join(lines)


def get_level_description(current_level: int, counts: dict) -> str:
    parts = []
    level = 1
    while level <= current_level:
        parts.append(str(counts[level]))
        level += 1
    return '.'.join(parts)


def generate_table_of_contents(headers: List[Header], separator=None, indent=None) -> str:
    if separator is None:
        separator = '&ensp;'
    if indent is None:
        indent = 4
    lines = []
    counts = {x: 0 for x in range(1, 7)}
    last_level = -1

    for header in headers:
        counts[header.level] += 1

        if last_level > header.level:
            # going back from lower to upper level (2 -> 1; 3 -> 2)
            # reset levels below
            for x in range(1, 7):
                if header.level < x:
                    counts[x] = 0
        else:
            last_level = header.level

        if header.level == 1:
            # use bold
            lines.append(f'<b>{counts[header.level]}. {header_link(header)}</b><br/>')
        else:
            indentation = separator * indent * (header.level - 1)
            lines.append(f'{indentation} {get_level_description(header.level, counts)} {header_link(header)}<br/>')

    return '\n'.join(lines)


def generate_table_of_contents_from_file(file_path: str, separator=None, indent=None):
    return generate_table_of_contents(get_headers_from_file(file_path), separator, indent)