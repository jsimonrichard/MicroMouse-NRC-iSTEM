#include "config.h"
#include "common.h"
#include "actors/robot.h"

void standByLoop() {
    if(button->isPressed()) {
        buzzer->play(SOUND_CRAWL);
        robot->set_state(Crawl);
    }
}

void crawlLoop() {
    // If at intersection
        // create node
        // connect it with previous
        // pick new direction
    // Else If at deadend
        // go back to last node
        // (do not create node)

    // If moved another unit
        // log in squares visited
}

void homingLoop() {
    
}

void dashLoop() {

}

void Robot::loop() {
    switch (state) {
        case StandBy:
            standByLoop();
            break;
        case Crawl:
            crawlLoop();
            break;
        case Homing:
            homingLoop();
            break;
        case Dash:
            dashLoop();
            break;
    }
}