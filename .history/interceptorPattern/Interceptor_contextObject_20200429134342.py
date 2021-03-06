from abc import ABCMeta, abstractstaticmethod
import sys
import logging
from contextlib import contextmanager ,ContextDecorator

class State(ContextDecorator):
    def __enter__(self):
        print('Logging started')
        return self

    def __exit__(self, *exc):
        print('Logging finished')
        return False 

class ContextObject(object):
    def __init__(self, user): 
         self.user = user 
      
    # getter method 
    def get_value(self): 
        return self.user 
      
    # setter method 
    def set_value(self, username): 
        self.user = username

class IInterceptor(metaclass=ABCMeta):
    @abstractstaticmethod
    def log():
        pass
        #Donation Interface

class ConcreteInterceptor(IInterceptor):
    @State()
    def log(self,obj):
        # create logger

        logger = logging.getLogger(__name__)   #instance of logger
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        logger.info('User has logged'+obj)


class Dispatcher:
    inter = []
    def __init__(self):
        self.inter=[]

    def register(self,interceptor):
        self.inter.append(interceptor)


    def remove(self,interceptor):
        self.inter.remove(interceptor)

    def dispatch(self,obj):
        for i in self.inter:
            i.log(obj)

class ConcreteFramework:
    co = None
    def event(self,user):
        self.co = ContextObject(user)
        #co.set_value(user)
        #obj=ContextObject.get_value(self) 
        disp = Interceptor_contextObject.Dispatcher()
        disp.dispatch(self.co)
