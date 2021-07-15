import sys

from os import PathLike
from pathlib import Path
from typing import List, Union


from antlr4 import FileStream, CommonTokenStream, InputStream
from antlr4.Parser import Parser
from antlr4.RuleContext import RuleContext
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.tree.Trees import Trees, ParseTree

from .vbaLexer import vbaLexer
from .vbaParser import vbaParser


class Antlr4VbaParser:
    """A simple VBA parser class"""
    def __init__(self, file_or_string: Union[PathLike, str]):
        if Path(file_or_string).exists():
            input_stream = FileStream(file_or_string)
        else:
            input_stream = InputStream(file_or_string)

        lexer: vbaLexer = vbaLexer(input_stream)
        stream: CommonTokenStream = CommonTokenStream(lexer)
        self.parser: vbaParser = vbaParser(stream)
        self.tree: ParseTree = self.parser.startRule()

    def __repr__(self):
        return Trees.toStringTree(self.tree, None, self.parser)
