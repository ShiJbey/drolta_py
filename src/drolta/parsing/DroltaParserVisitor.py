# Generated from DroltaParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DroltaParser import DroltaParser
else:
    from DroltaParser import DroltaParser

# This class defines a complete generic visitor for a parse tree produced by DroltaParser.

class DroltaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DroltaParser#prog.
    def visitProg(self, ctx:DroltaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#drolta_stmt_list.
    def visitDrolta_stmt_list(self, ctx:DroltaParser.Drolta_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#drolta_stmt.
    def visitDrolta_stmt(self, ctx:DroltaParser.Drolta_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#declare_alias_stmt.
    def visitDeclare_alias_stmt(self, ctx:DroltaParser.Declare_alias_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#declare_rule_stmt.
    def visitDeclare_rule_stmt(self, ctx:DroltaParser.Declare_rule_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#define_clause.
    def visitDefine_clause(self, ctx:DroltaParser.Define_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#result_var_list.
    def visitResult_var_list(self, ctx:DroltaParser.Result_var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#query_stmt.
    def visitQuery_stmt(self, ctx:DroltaParser.Query_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#find_clause.
    def visitFind_clause(self, ctx:DroltaParser.Find_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#result_var.
    def visitResult_var(self, ctx:DroltaParser.Result_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#variable_alias.
    def visitVariable_alias(self, ctx:DroltaParser.Variable_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#where_clause.
    def visitWhere_clause(self, ctx:DroltaParser.Where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#order_by_clause.
    def visitOrder_by_clause(self, ctx:DroltaParser.Order_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#ordering_term_list.
    def visitOrdering_term_list(self, ctx:DroltaParser.Ordering_term_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#ordering_term.
    def visitOrdering_term(self, ctx:DroltaParser.Ordering_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#group_by_clause.
    def visitGroup_by_clause(self, ctx:DroltaParser.Group_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#variable_list.
    def visitVariable_list(self, ctx:DroltaParser.Variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#limit_clause.
    def visitLimit_clause(self, ctx:DroltaParser.Limit_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#where_stmt.
    def visitWhere_stmt(self, ctx:DroltaParser.Where_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#ComparisonFilterStmt.
    def visitComparisonFilterStmt(self, ctx:DroltaParser.ComparisonFilterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#MembershipFilterStmt.
    def visitMembershipFilterStmt(self, ctx:DroltaParser.MembershipFilterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#AndFilterStmt.
    def visitAndFilterStmt(self, ctx:DroltaParser.AndFilterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#OrFilterStmt.
    def visitOrFilterStmt(self, ctx:DroltaParser.OrFilterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#NotFilterStmt.
    def visitNotFilterStmt(self, ctx:DroltaParser.NotFilterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#atom_list.
    def visitAtom_list(self, ctx:DroltaParser.Atom_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#comparison_operator.
    def visitComparison_operator(self, ctx:DroltaParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#predicate_neg_stmt.
    def visitPredicate_neg_stmt(self, ctx:DroltaParser.Predicate_neg_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#predicate_stmt.
    def visitPredicate_stmt(self, ctx:DroltaParser.Predicate_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#positional_param_list.
    def visitPositional_param_list(self, ctx:DroltaParser.Positional_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#named_param_list.
    def visitNamed_param_list(self, ctx:DroltaParser.Named_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#named_param.
    def visitNamed_param(self, ctx:DroltaParser.Named_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#variable_atom.
    def visitVariable_atom(self, ctx:DroltaParser.Variable_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#int_literal.
    def visitInt_literal(self, ctx:DroltaParser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#float_literal.
    def visitFloat_literal(self, ctx:DroltaParser.Float_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#string_literal.
    def visitString_literal(self, ctx:DroltaParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#null_literal.
    def visitNull_literal(self, ctx:DroltaParser.Null_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#bool_literal.
    def visitBool_literal(self, ctx:DroltaParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DroltaParser#variable.
    def visitVariable(self, ctx:DroltaParser.VariableContext):
        return self.visitChildren(ctx)



del DroltaParser