import os

from context import Context
from node import ProgramNode

if __name__ == '__main__':

    with open(os.path.dirname(__file__) + '/program.text', 'r') as f:
        programs = [t.rstrip('\n') for t in f.readlines()]
    
    for program in programs:
        print('text = %s' % program)
        node = ProgramNode()
        node.parse(Context(program))
        print('node = %s' % node.to_string())
        print()