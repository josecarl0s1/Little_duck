grammar little_duck;
@parser::header {
from Interventions import *
}
programa: 'program' ID ';' {inter.setVariableScope('global')} vars  funcs 'main' {inter.setMainQuad()} body 'end' EOF{inter.endQuad()}{inter.printGlobal()};
vars: 'var' vars_prime ':' type {inter.setTypes($type.text)} ';' l_vars | ;
vars_prime: ID {inter.addVariable($ID.text, $ID.line)}vars_prime_prime ;
vars_prime_prime: ',' vars_prime | ;
l_vars: vars_prime ':' type ';' l_vars {inter.setTypes($type.text)}| ;
type: 'int' | 'float' ;
funcs: 'void' ID {inter.setVariableScope($ID.text)} '(' funcs_prime ')' '[' vars body ']' ';'{inter.setVariableScope('global')}{inter.endFunc()} funcs | ;
funcs_prime: ID {inter.addVariable($ID.text, $ID.line)}':' type {inter.setTypes($type.text)} {inter.countParams()}funcs_prime_prime | ;
funcs_prime_prime: ',' funcs_prime | ;
body: '{' l_statement '}' ;
statement: assign | condition | cycle | f_call | print ;
l_statement: statement l_statement |  ;
print: 'print' {inter.keyPoint_OperationPush('PRINT')} '('  print_prime l_print ')'  ';'{inter.keyPoint_CreateQuad(4)};
print_prime: expression | STRING ;
l_print: ',' {inter.keyPoint_OperationPush(',')} print_prime {inter.keyPoint_CreateQuad(3)} l_print | ;
cycle: 'do' {inter.whileKeyOne()} body 'while' '(' expression ')' ';'{inter.endWhile()};
condition: 'if' '(' expression ')' {inter.createGoToF()} body condition_prime ';' {inter.if_Fill()};
condition_prime: 'else' {inter.else_Fill()} body | ;
cte: INT | FLOAT ;
expression: exp expression_prime;
expression_prime: oper {inter.keyPoint_OperationPush($oper.text)} exp {inter.keyPoint_CreateQuad(2)} | ;
oper: '>' | '<' | '!=';
assign: ID {inter.isNotDefined($ID.text, $ID.line)} {inter.keyPoint_1($ID.text)} '=' {inter.keyPoint_OperationPush('=')} expression ';'{inter.keyPoint_CreateQuad(3)};
exp: termino {inter.keyPoint_CreateQuad(0)} l_exp;
l_exp: pm {inter.keyPoint_OperationPush($pm.text)} termino {inter.keyPoint_CreateQuad(0)}  l_exp | ;
pm: '+' | '-';
termino: factor {inter.keyPoint_CreateQuad(1)} l_termino;
l_termino: ad {inter.keyPoint_OperationPush($ad.text)} factor {inter.keyPoint_CreateQuad(1)} l_termino | ;
ad: '*' | '/';  
factor: '(' {inter.keyPoint_PushBottom()}  expression ')'{inter.keyPoint_PopFalse()} | factor_prime;
factor_prime: b_factor ic  {# removed | pm}; 
b_factor: pm_const | ;
pm_const: '+' | '-' {inter.setMinusOne()};
ic: ID {inter.isNotDefined($ID.text, $ID.line)}{inter.keyPoint_1($ID.text)}| cte {inter.keyPoint_1($cte.text, $cte.stop.type)} {# This rule chesk if this is ID or Constant}; 
f_call: ID '(' f_call_prime ')' ';' ;
f_call_prime: expression l_f_call_prime | ;
l_f_call_prime: ',' f_call_prime | ;


NEWLINE: [\r\n\t]+ -> skip;
WHITESPACE: ' ' -> skip;
INT: [0-9]+;
FLOAT: [-]?[0-9]+('.'[0-9]+)?;
ID: [a-z]+[a-z_0-9A-Z]*;
STRING: '"' ~["]* '"';
