"""Implements the ANTLR listener pattern for the VBA parser"""

from .vbaListener import vbaListener
from .vbaParser import vbaParser


class VBADictListener(vbaListener):
    """Custom VBA listener which produces a dictionary of VBA output"""
    def __init__(self) -> None:
        super().__init__()
        self.data = {
            'modules': {}
        }

   # Enter a parse tree produced by vbaParser#module.
    def enterModule(self, ctx: vbaParser.ModuleContext):
        self.data['modules'][ctx] = {
            'name': ctx.getText(),
            'attributes': {},
            'declarations': {},
            'comments': {},
            'functions': {},
            'subroutines': {}
        }
        self._module = ctx

    # Exit a parse tree produced by vbaParser#module.
    def exitModule(self, ctx: vbaParser.ModuleContext):
        self._module = None

    # Enter a parse tree produced by vbaParser#moduleHeader.
    def enterModuleHeader(self, ctx: vbaParser.ModuleHeaderContext):
        self._module_header = ctx

    # Exit a parse tree produced by vbaParser#moduleHeader.
    def exitModuleHeader(self, ctx: vbaParser.ModuleHeaderContext):
        self._module_header = None

    # Enter a parse tree produced by vbaParser#subStmt.
    def enterSubStmt(self, ctx:vbaParser.SubStmtContext):
        self._sub = ctx

    # Exit a parse tree produced by vbaParser#subStmt.
    def exitSubStmt(self, ctx:vbaParser.SubStmtContext):
        self._sub = None

    # Enter a parse tree produced by vbaParser#ambiguousIdentifier.
    def enterAmbiguousIdentifier(self, ctx:vbaParser.AmbiguousIdentifierContext):
        self._identifier = ctx

    # Exit a parse tree produced by vbaParser#ambiguousIdentifier.
    def exitAmbiguousIdentifier(self, ctx:vbaParser.AmbiguousIdentifierContext):
        self._identifier = None

    # Enter a parse tree produced by vbaParser#certainIdentifier.
    def enterCertainIdentifier(self, ctx:vbaParser.CertainIdentifierContext):
        self._identifier = ctx

    # Exit a parse tree produced by vbaParser#certainIdentifier.
    def exitCertainIdentifier(self, ctx:vbaParser.CertainIdentifierContext):
        self._identifier = None

    # Enter a parse tree produced by vbaParser#remComment.
    def enterRemComment(self, ctx:vbaParser.RemCommentContext):
        pass

    # Exit a parse tree produced by vbaParser#remComment.
    def exitRemComment(self, ctx:vbaParser.RemCommentContext):
        pass

    # Enter a parse tree produced by vbaParser#comment.
    def enterComment(self, ctx:vbaParser.CommentContext):
        pass

    # Exit a parse tree produced by vbaParser#comment.
    def exitComment(self, ctx:vbaParser.CommentContext):
        pass

    # Enter a parse tree produced by vbaParser#endOfLine.
    def enterEndOfLine(self, ctx:vbaParser.EndOfLineContext):
        pass

    # Exit a parse tree produced by vbaParser#endOfLine.
    def exitEndOfLine(self, ctx:vbaParser.EndOfLineContext):
        pass

    # Enter a parse tree produced by vbaParser#endOfStatement.
    def enterEndOfStatement(self, ctx:vbaParser.EndOfStatementContext):
        pass

    # Exit a parse tree produced by vbaParser#endOfStatement.
    def exitEndOfStatement(self, ctx:vbaParser.EndOfStatementContext):
        pass

