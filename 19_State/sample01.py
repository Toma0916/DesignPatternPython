from abc import ABCMeta, abstractmethod
import random
import time


class State(metaclass=ABCMeta):

    @abstractmethod
    def do_clock(self, context: 'Context', hour: int):
        pass

    @abstractmethod
    def do_use(self, context: 'Context'):
        pass

    @abstractmethod
    def do_alarm(self, context: 'Context'):
        pass

    @abstractmethod
    def do_phone(self, context: 'Context'):
        pass


class Singleton():

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class DayState(State, Singleton):  # Singletonで実装

    def do_clock(self, context: 'Context', hour: int):
        if (hour < 9 or 17 <= hour):
            context.change_state(NightState())
    
    def do_use(self, context: 'Context'):
        context.record_log('金庫使用（昼間）')
    
    def do_alarm(self, context: 'Context'):
        context.call_security_center('非常ベル（昼間）')

    def do_phone(self, context: 'Context'):
        context.call_security_center('通常の通話（昼間）')
    
    def to_string(self):
        return '【昼間】'


class NightState(State, Singleton):

    def do_clock(self, context: 'Context', hour: int):
        if (9 <= hour < 17):
            context.change_state(DayState())
        
    def do_use(self, context: 'Context'):
        context.call_security_center('非常 : 夜間の金庫使用！')
    
    def do_alarm(self, context: 'Context'):
        context.call_security_center('非常ベル（夜間）')

    def do_phone(self, context: 'Context'):
        context.record_log('夜間の通話録音')
    
    def to_string(self):
        return '【夜間】'
        

class Context(metaclass=ABCMeta):

    @abstractmethod
    def set_clock(self, hour: int):
        pass

    @abstractmethod
    def change_state(self, state: 'State'):
        pass

    @abstractmethod
    def call_security_center(self, msg: str):
        pass

    @abstractmethod
    def record_log(self, msg: str):
        pass


class SafeFrame(Context):

    def __init__(self):
        self.__state = DayState()
    
    def set_clock(self, hour: int):
        clock_string = '現在時刻は%02d:00' % hour
        print(clock_string)
        self.__state.do_clock(self, hour)
    
    def change_state(self, state: 'State'):
        print('%sから%sへ状態が変化しました.' % (self.__state.to_string(), state.to_string()))
        self.__state = state

    def call_security_center(self, msg: str):
        print('call! %s' % msg)

    def record_log(self, msg: str):
        print('record... %s' % msg)
    
    def perform(self, code: int):

        if code == 0:
            self.__state.do_use(self)
        elif code == 1:
            self.__state.do_alarm(self)
        elif code == 2:
            self.__state.do_phone(self)
        else:
            print('?')

if __name__ == '__main__':

    frame = SafeFrame()
    for hour in range(25):
        frame.set_clock(hour)
        frame.perform(random.randint(0, 2))
        time.sleep(1)


