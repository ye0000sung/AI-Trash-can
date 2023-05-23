// LED 핀 번호
const int led1 = 13;
const int led2 = 12;
const int led3 = 11;

void setup() {
  // 시리얼 통신 초기화
  Serial.begin(9600);

  // LED 핀 모드 설정
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    // 시리얼 통신으로부터 문자열 받기
    String color = Serial.readStringUntil('\n');

    // 색상에 따라 LED 켜고 끄기
    if (color == "1") {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
      digitalWrite(led3, LOW);
    } else if (color == "2") {
      digitalWrite(led1, LOW);
      digitalWrite(led2, HIGH);
      digitalWrite(led3, LOW);
    } else if (color == "3") {
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
      digitalWrite(led3, HIGH);
    }
  }
}
