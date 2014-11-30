from practicum import McuBoard

RQ_GET_SWITCH = 0
RQ_GET_ACCELERO_X   = 1
RQ_GET_ACCELERO_Y   = 2

####################################
class PeriBoard(McuBoard):

    ################################
    def getSwitch(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        if (self.usbRead(RQ_GET_SWITCH,length=1)[0]==0):
                 return False
        else :
                 return True

    ################################
    def getAcceleroX(self):
        '''
        Return the current reading of accelerometer x-Axis on peripheral board
        '''
        x = self.usbRead(RQ_GET_ACCELERO_X,length=1)[0]
        x = (x*4)-512
        return x
    ################################
    def getAcceleroY(self):
        '''
        Return the current reading of accelerometer x-Axis on peripheral board
        '''
        y = self.usbRead(RQ_GET_ACCELERO_Y,length=1)[0]
        y = (y*4)-512
        return y
