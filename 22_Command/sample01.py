from abc import ABCMeta, abstractmethod

# 命令を`モノ`として表現する
class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


class MacroCommand(Command):

    def __init__(self):
        self.__commands = []
    
    def execute(self):
        for cmd in self.__commands:
            cmd.execute()
    
    def append(self, cmd: 'Command'):
        if (cmd is not self):
            self.__commands.append(cmd)
    
    def undo(self):
        if len(self.__commands) != 0:
            self.__commands.pop(-1)
    
    def clear(self):
        self.__commands.clear()


class StringPrintCommand(Command):

    def __init__(self, string: str):
        self.__string = string
    
    def execute(self):
        print(self.__string)


class PrintCanvas():

    def __init__(self, history: 'MacroCommand'):
        self.__history = history
    
    def print_strings(self):
        self.__history.execute()


if __name__ == '__main__':
    print('add command')
    history = MacroCommand()
    canvas = PrintCanvas(history)
    
    print('add StringPrintCommand')
    history.append(StringPrintCommand('command1'))
    print('call print_strings')
    canvas.print_strings()
    print()

    print('add StringPrintCommand')
    history.append(StringPrintCommand('command2'))
    print('call print_strings')
    canvas.print_strings()
    print()

    print('add MacroCommand')
    sub_command = MacroCommand()
    sub_command.append(StringPrintCommand('sub-command1'))
    sub_command.append(StringPrintCommand('sub-command2'))
    history.append(sub_command)
    print('call print_strings')
    canvas.print_strings()
    print()

    print('pop last command')
    history.undo()
    print('call print_strings')
    canvas.print_strings()
    print()

    print('clear all command')
    history.clear()
    print('call print_strings')
    canvas.print_strings()
    print()
