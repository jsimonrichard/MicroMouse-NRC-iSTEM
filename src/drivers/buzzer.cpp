#include "Arduino.h"

namespace drivers {
  namespace buzzer {
    void setup() {
        pinMode(BUZZER_PIN, OUTPUT);
    }

    void playStartSound() {
        tone(BUZZER_PIN, 440, 500); // A4 for 0.5 seconds
        tone(BUZZER_PIN, 659.3, 500); // E5 for 0.5 seconds
    }

    void playMapCompleteSound() {
        tone(BUZZER_PIN, 987.8, 250); // B5 for 0.25 seconds
        tone(BUZZER_PIN, 659.3, 250); // E5 for 0.25 seconds
        tone(BUZZER_PIN, 493.9, 250); // B4 for 0.25 seconds
    }

    void playSprintSound() { // played at the beginning of the sprint
        tone(BUZZER_PIN, 493.9, 250); // B4 for 0.25 seconds
        delay(2);
        tone(BUZZER_PIN, 493.9, 250); // B4 for 0.25 seconds
        delay(2);
        tone(BUZZER_PIN, 659.3, 500); // E5 for 0.5 seconds
    }

    void playFinishSound() {
        tone(BUZZER_PIN, 329.6, 250); // E4 for 0.25 seconds
        tone(BUZZER_PIN, 493.9, 250); // B4 for 0.25 seconds
        tone(BUZZER_PIN, 659.3, 250); // E5 for 0.25 seconds
        tone(BUZZER_PIN, 830.6, 250); // G#5 for 0.25 seconds
        tone(BUZZER_PIN, 987.8, 250); // B5 for 0.25 seconds
    }
  }
}
