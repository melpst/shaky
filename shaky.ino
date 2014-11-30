#include <Practicum.h>
#include <AcceleroMMA7361.h>
extern "C" {
#include "usbdrv.h"
}

#define RQ_GET_SWITCH 0
#define RQ_GET_ACCELERO_X 1
#define RQ_GET_ACCELERO_Y 2

#define PIN_X PIN_PC1
#define PIN_Y PIN_PC0
#define PIN_Z PIN_PC2
#define PIN_SW PIN_PC3

AcceleroMMA7361 accelero;

//////////////////////////////////////////////////////////////////////
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
  usbRequest_t *rq = (usbRequest_t*)data;
  static uint8_t switch_state; 
  static uint8_t accelero_x; 
  static uint8_t accelero_y; 

  if (rq->bRequest == RQ_GET_SWITCH)
  {
    if (digitalRead(PIN_SW) == LOW) /* switch is pressed */ 
      switch_state = 1;
    else
      switch_state = 0;

    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &switch_state;

    /* return the number of bytes of data to be returned to host */
    return sizeof(switch_state);
  }

  else if (rq->bRequest == RQ_GET_ACCELERO_X)
  {
    accelero_x = (uint8_t)((accelero.getXAccel()+512)/4);
    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &accelero_x;

    /* return the number of bytes of data to be returned to host */
    return sizeof(accelero_x);
  }
  
  else if (rq->bRequest == RQ_GET_ACCELERO_Y)
  {
    accelero_y = (uint8_t)((accelero.getYAccel()+512)/4);
    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &accelero_y;

    /* return the number of bytes of data to be returned to host */
    return sizeof(accelero_y);
  }
  return 0;   /* nothing to do; return no data back to host */
}

//////////////////////////////////////////////////////////////////////
void setup()
{
  pinMode(PIN_SW, INPUT_PULLUP);

  usbInit();

  accelero.begin(13, 12, 11, 10, PIN_X, PIN_Y, PIN_Z);
  accelero.setARefVoltage(5); //sets the AREF voltage to 3.3V
  accelero.setSensitivity(LOW); //sets the sensitivity to +/-6G
  accelero.calibrate();
  /* enforce re-enumeration of USB devices */
  usbDeviceDisconnect();
  delay(300);
  usbDeviceConnect();
}

//////////////////////////////////////////////////////////////////////
void loop()
{
  usbPoll();
}

