# Generated from /Users/adamkisala/Documents/Projects/DGDL/project/adamantium/ebnf/dgdl.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dgdlParser import dgdlParser
else:
    from dgdlParser import dgdlParser

# This class defines a complete generic visitor for a parse tree produced by dgdlParser.

class dgdlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by dgdlParser#game.
    def visitGame(self, ctx:dgdlParser.GameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#store.
    def visitStore(self, ctx:dgdlParser.StoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#turns.
    def visitTurns(self, ctx:dgdlParser.TurnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#players.
    def visitPlayers(self, ctx:dgdlParser.PlayersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#player.
    def visitPlayer(self, ctx:dgdlParser.PlayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#roles.
    def visitRoles(self, ctx:dgdlParser.RolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#principles.
    def visitPrinciples(self, ctx:dgdlParser.PrinciplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#principle.
    def visitPrinciple(self, ctx:dgdlParser.PrincipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#scope.
    def visitScope(self, ctx:dgdlParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#moves.
    def visitMoves(self, ctx:dgdlParser.MovesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#move.
    def visitMove(self, ctx:dgdlParser.MoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#content.
    def visitContent(self, ctx:dgdlParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#conditions.
    def visitConditions(self, ctx:dgdlParser.ConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#effects.
    def visitEffects(self, ctx:dgdlParser.EffectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#expr.
    def visitExpr(self, ctx:dgdlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dgdlParser#param.
    def visitParam(self, ctx:dgdlParser.ParamContext):
        return self.visitChildren(ctx)



del dgdlParser