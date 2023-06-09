import os
from lib.interface import linha, cabecalho
from db.listar import listar


def listar_pessoa():
    pessoas = listar()
    cabecalho("PESSOAS CADASTRADAS")
    for pessoa in pessoas:
        print(f"\033[34mMatricula:\033[m {pessoa[1]}{os.linesep}"
              f"\033[34mNome:\033[m {pessoa[2]}{os.linesep}"
              f"\033[34mData de Nasc.:\033[m {pessoa[5]}{os.linesep}"
              f"\033[34mCPF:\033[m {pessoa[7]}{os.linesep}{linha()}")

