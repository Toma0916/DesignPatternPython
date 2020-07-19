from abc import ABCMeta, abstractmethod

class Node(metaclass=ABCMeta):

    @abstractmethod
    def parse(self, context: 'Context'):
        pass

    @abstractmethod
    def to_string(self):
        pass


# <program> ::= program <command list>
class ProgramNode(Node):

    def __init__(self):
        self.__command_list_node = CommandListNode()
    
    def parse(self, context: 'Context'):
        context.skip_token('program')
        self.__command_list_node.parse(context)
    
    def to_string(self):
        return '[program %s]' % self.__command_list_node.to_string()


# <command list> ::= <command>* end
class CommandListNode(Node):

    def __init__(self):
        self.__command_list = []
    
    def parse(self, context: 'Context'):
        while True:
            if (context.current_token == None):
                raise SyntaxError()
            elif (context.current_token == 'end'):
                context.skip_token('end')
                break
            else:
                command_node = CommandNode()
                command_node.parse(context)
                self.__command_list.append(command_node)
    
    def to_string(self):
        string = '' 
        for command in self.__command_list:
            string += command.to_string() + ', '
        string = '[ %s ]' % string
        return string


# <command> :== <repeat command> | <primitive command>
class CommandNode(Node):

    def __init__(self):
        self.__node = None

    def parse(self, context: 'Context'):
        if (context.current_token == 'repeat'):
            self.__node = RepeatCommandNode()
            self.__node.parse(context)
        else:
            self.__node = PrimitiveCommandNode()
            self.__node.parse(context)
    
    def to_string(self):
        return self.__node.to_string()


# <repeat command> ::= repeat <number> <command list>
class RepeatCommandNode(Node):

    def __init__(self):
        self.__number = None
        self.__command_list_node = None
    
    def parse(self, context: 'Context'):
        context.skip_token('repeat')
        self.__number = context.current_number()
        context.next_token()
        self.__command_list_node = CommandListNode()
        self.__command_list_node.parse(context)

    def to_string(self):
        return '[repeat %d %s]' % (self.__number, self.__command_list_node.to_string())
    

# <primitive command> :== go | right | left
class PrimitiveCommandNode(Node):

    def __init__(self):
        self.__name = None
    
    def parse(self, context: 'Context'):
        self.__name = context.current_token
        context.skip_token(self.__name)
        if not (self.__name == 'go' or self.__name == 'right' or self.__name == 'left'):
            raise SyntaxError()
    
    def to_string(self):
        return self.__name
    



