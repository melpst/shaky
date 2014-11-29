from practicum import McuBoard

RQ_SET_LED    = 0
RQ_GET_SWITCH = 1
RQ_GET_LIGHT  = 2

####################################
class PeriBoard(McuBoard):

    ################################
    def setLed(self, led_no, led_val):
        '''
        Set status of LED led_no on peripheral board to led_val
        '''
        self.usbWrite(RQ_SET_LED,index=led_no,value=led_val)

    ################################
    def setLedValue(self, value):
        '''
        Display value's 3 LSBs on peripheral board's LEDs
        '''
       #return
        
        valueList=[]
        for i in range(3):
#               valueList=value[5+i]
                x=value%2
                value/=2
                self.usbWrite(RQ_SET_LED,index=i,value=x)
#        if (valueList[0]==1):
#                self.usbWrite(RQ_SET_LED,index=2,value=1)
#        if (valueList[1]==1): 
#                self.usbWrite(RQ_SET_LED,index=1,value=1)
#        if (valueList[2]==1):
#                self.usbWrite(RQ_SET_LED,index=0,value=1)

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
    def getLight(self):
        '''
        Return the current reading of light sensor on peripheral board
        '''
        
        list=self.usbRead(RQ_GET_LIGHT,length=2)
        return list[1]*256+list[0]
