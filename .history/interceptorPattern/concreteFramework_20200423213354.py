#Defines app services
#integrate dispatcher that allows applications to intercept events
# exposes events
# interceptor has methods that is invoked by this class via dispatcher when the event occurs
from interceptorPattern.dispatcher import Dispatcher
class ConcreteFramework():

    def notifyDispatcher(self,cardNumber):
        # co = contextObject() #In this case the context object can contain information related to the event that triggered its creation.
        # cardNumber = co.getValue()
        dispatcher = Dispatcher()
        print("Concrete Framework")
        return dispatcher.dispatch(cardNumber)