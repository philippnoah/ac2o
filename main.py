#include <Event.h>
#include <Timer.h>
#include <BMP180MI.h>

#define I2C_ADDRESS 0x77

BMP180I2C bmp180(I2C_ADDRESS);

Timer t;

int serial;
int pumpport = 7;
int pumpperiod = 30000;
int pumpdelay = 5000;
int pumpevent;
int h1 = 8;
int h2 = 9;
int h3 = 10;
int sw = 0;
double pressure = 0;
double temperature = 0;

void setup() {

  Serial.begin(9600);

  pinMode (pumpport , OUTPUT);
  pinMode (h1, OUTPUT);
  pinMode (h2, OUTPUT);
  pinMode (h2, OUTPUT);

  heatersoff();

  pumpevent = t.every(pumpperiod, pump);



  Wire.begin();

  //begin() initializes the interface, checks the sensor ID and reads the calibration parameters.
  if (!bmp180.begin())
  {
    Serial.println("begin() failed. check your BMP180 Interface and I2C Address.");
    while (1);
  }

  //reset sensor to default parameters.
  bmp180.resetToDefaults();

  //enable ultra high resolution mode for pressure measurements
  bmp180.setSamplingMode(BMP180MI::MODE_UHR);

  Serial.println ("Ready to go");
}

void loop() {
  // put your main code here, to run repeatedly:
  serial = int(Serial.read());

  delay(100);

  //start a temperature measurement
  if (!bmp180.measureTemperature())
  {
    Serial.println("could not start temperature measurement, is a measurement already running?");
    return;
  }

  //wait for the measurement to finish. proceed as soon as hasValue() returned true.
  do
  {
    delay(100);
  } while (!bmp180.hasValue());

  pressure = bmp180.getPressure()/101325;



  //start a pressure measurement. pressure measurements depend on temperature measurement, you should only start a pressure
  //measurement immediately after a temperature measurement.
  if (!bmp180.measurePressure())
  {
    Serial.println("could not start perssure measurement, is a measurement already running?");
    return;
  }

  //wait for the measurement to finish. proceed as soon as hasValue() returned true.
  do
  {

    delay(100);

  } while (!bmp180.hasValue());

  temperature = bmp180.getTemperature();


  if (temperature < 25 && sw == 0){
    heaterson();
    sw = 1;
  }

  else if (temperature >= 25 && temperature < 30 && sw == 0){
    heatersoff();
  }

  else if (temperature >= 25 && temperature < 30 && sw == 1){
    heaterson();
  }
  else if (temperature >= 30){
    heatersoff();
    sw = 0;
  }

  Serial.println (String(temperature) + "," + String(pressure));


  if (serial == 49){
    Serial.println ("Stopped");
    Serial.println (serial);
    delay(5000);
  }

  else if (serial != -1){
    Serial.println (serial);
  }

  t.update();
}



void pump(){

  pumphigh();
  t.after(pumpdelay, pumplow);

}

void pumphigh(){
 digitalWrite (pumpport,HIGH);
}

void pumplow(){
  digitalWrite (pumpport, LOW);
}

void heaterson(){

  digitalWrite (h1,HIGH);
  digitalWrite (h2,HIGH);
  digitalWrite (h3,HIGH);

}

void heatersoff(){

  digitalWrite (h1,LOW);
  digitalWrite (h2,LOW);
  digitalWrite (h3,LOW);

}
