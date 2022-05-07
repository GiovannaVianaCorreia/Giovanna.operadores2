#Faça um programa que leia 4 notas de um aluno, salve as em uma lista e calcule a média das notas.
primeiroNome = input ( "Digite seu primeiro nome: " )
primeiraLetra = primeiroNome [ 0:1 ]. superior ()
restanteNome = primeiroNome [ 1 :]. inferior ()
nomeFormatado = primeiraLetra + restanteNome

ainput = input ( "Digite sua nota na primeira atividade: " )
binput = input ( "Digite sua nota na atividade: " )
cinput = input ( "Digite sua nota na terceira atividade: " )
dinput = input ( "Digite sua nota na quarta atividade: " )

a = float ( aentrada )
b = float ( binput )
c = float ( cinput )
d = float ( dinput )
mídia = ( a  +  b  +  c  +  d ) /  4

minhaLista = []
minhaLista . anexar ( ainput )
minhaLista . anexar ( binput )
minhaLista . anexar ( cinput )
minhaLista . anexar ( dinput )
imprimir ( minhaLista )

print ( "A média das notas de " + nomeformatado +   "é de" +  str ( media ) + "." )