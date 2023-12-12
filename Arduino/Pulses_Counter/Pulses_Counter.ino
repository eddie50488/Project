unsigned short ydir = 0;

int directionPin = 12;
int pwmPin = 3;
int brakePin = 9;

boolean flag = true;

void setup()
{
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(2), ydirCounter, RISING);
  pinMode(directionPin, OUTPUT);
  pinMode(pwmPin, OUTPUT);
  pinMode(brakePin, OUTPUT);
}

void loop()
{
  while (flag == true)
  {
    if (Serial.available())
    {
      delay(1000);
      move();
      delay(5000);
      stop();
      Serial.println(ydir);
      Serial.flush();
      flush();
    }
  }
}

void ydirCounter()
{
  ydir++;
}

void move()
{
  digitalWrite(directionPin, 0);
  digitalWrite(brakePin, 0);
  analogWrite(pwmPin, 255);
}

void stop()
{
  digitalWrite(directionPin, 0);
  digitalWrite(brakePin, 1);
  analogWrite(pwmPin, 0);
}

void flush()
{
  while (Serial.available())
    Serial.read();
}