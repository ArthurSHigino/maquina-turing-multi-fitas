# maquina-turing-multi-fitas

Projeto realizado como trababalho final da disciplina Linguagens Formais e Autômatos em dezembro de 2023, visa a criação de um programa que recebe uma máquina de turing com múltiplas fitas no formato Json e uma palavra como entrada dessa máquina, e então retorna se a palavra pertence ou não a aquela linguagem descrita pela máquina de turing.

As especificações completas desse projeto podem ser acessadas em: http://rimsa.com.br/documents/lectures/decom035/homeworks/2023_2/TP.pdf

## Instruções
Para executar o programa basta abrir o terminal na pasta que contenha o código "mt.py" e máquina de turing no formato JSON que deseja executar. 
Em seguida executar python3 mt.py maquina_no_formato.json "palavra de entrada"
ex:
python3 mt.py mt1.json "011110011"

## Linguagens representadas por cada máquina

mt.json - Retorna sim se a palavra possuir pelo menos um "0".

mt1.json - Retorna sim para a linguagem composta por uma palavra x concatenada com x de trás pra frente concetenada com x
(obs: x só pode conter 1s e 0s). Ex: 001100001, 000, 100110.

q1.json - Retorna não se a palavra for "a".

xx.json - Retorna sim para a linguagem composta por uma palavra x concatenada a uma palavra x (obs: x só pode conter a's e b's). Ex: aa, bb, aaabbb, abab, ababaababa.

![image](https://github.com/ArthurSHigino/maquina-turing-multi-fitas/assets/167269789/5fd31402-93e7-47e9-b169-5ea5e650a132)


