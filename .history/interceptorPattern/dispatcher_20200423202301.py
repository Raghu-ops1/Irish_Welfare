#Triggers concrete interceptors



def registerInterceptors():
    add interceptors to a lists or something
    return interceptorList

def removeInterceptors():
    remove interceptors

def dispatch(cardNumber): #Dispatches interceptor method when event occurs
    for interceptor in interceptorList:
        interceptor.creditCardValidation(cardNumber)