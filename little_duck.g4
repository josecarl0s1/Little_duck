grammar little_duck;
@parser::header {
from Interventions import *
}
programa: 'program' ID ';' {inter.setVariableScope('global')} vars  funcs 'main' body 'end' {inter.printGlobal()}EOF;
vars: 'var' vars_prime ':' type {inter.setTypes($type.text)} ';' l_vars | ;
vars_prime: ID {inter.addVariable($ID.text, $ID.line)}vars_prime_prime ;
vars_prime_prime: ',' vars_prime | ;
l_vars: vars_prime ':' type ';' l_vars {inter.setTypes($type.text)}| ;
type: 'int' | 'float' ;
funcs: 'void' ID {inter.setVariableScope($ID.text)} '(' funcs_prime ')' '[' vars body ']' ';'{inter.setVariableScope('global')} funcs | ;
funcs_prime: ID {inter.addVariable($ID.text, $ID.line)}':' type {inter.setTypes($type.text)} funcs_prime_prime | ;
funcs_prime_prime: ',' funcs_prime | ;
body: '{' l_statement '}' ;
statement: assign | condition | cycle | f_call | print ;
l_statement: statement l_statement |  ;
print: 'print' '(' print_prime l_print ')' ';';
print_prime: expression | STRING;
l_print: ',' print_prime l_print | ;
cycle: 'do' body 'while' '(' expression ')' ';';
condition: 'if' '(' expression ')' body condition_prime ';';
condition_prime: 'else' body | ;
cte: INT | FLOAT ;
expression: exp expression_prime;
expression_prime: oper {inter.keyPoint_OperationPush($oper.text)} exp {inter.keyPoint_CreateQuad(2)} | ;
oper: '>' | '<' | '!=';
assign: ID {inter.isNotDefined($ID.text, $ID.line)}'=' expression ';';
exp: termino {inter.keyPoint_CreateQuad(0)} l_exp;
l_exp: pm {inter.keyPoint_OperationPush($pm.text)} termino {inter.keyPoint_CreateQuad(0)}  l_exp | ;
pm: '+' | '-';
termino: factor {inter.keyPoint_CreateQuad(1)} l_termino;
l_termino: ad {inter.keyPoint_OperationPush($ad.text)} factor {inter.keyPoint_CreateQuad(1)} l_termino | ;
ad: '*' | '/';  
factor: '(' {inter.keyPoint_PushBottom()}  expression ')'{inter.keyPoint_PopFalse()} | factor_prime;
factor_prime: b_factor ic {inter.keyPoint_1($ic.text)} {# removed | pm}; 
b_factor: pm_const | ;
pm_const: '+' | '-';
ic: ID {inter.isNotDefined($ID.text, $ID.line)}| cte {# This rule chesk if this is ID or Constant}; 
f_call: ID '(' f_call_prime ')' ';' ;
f_call_prime: expression l_f_call_prime | ;
l_f_call_prime: ',' f_call_prime | ;


NEWLINE: [\r\n\t]+ -> skip;
WHITESPACE: ' ' -> skip;
INT: [0-9]+;
FLOAT: [-]?[0-9]+('.'[0-9]+)?;
ID: [a-z]+[a-z_0-9A-Z]*;
STRING: '"' ~["]* '"';
