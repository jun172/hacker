#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>

#define TRIG 23
#define ECHO 24
#define LEFT1 17
#define LEFT2 18
#define RIGHT1 27
#define RIGHT2 22

void motor_forward() {
    gpioWrite(LEFT1, 1);
    gpioWrite(LEFT2, 0);
    gpioWrite(RIGHT1,1);
    gpioWrite(RIGHT2,0);
}

void motor_stop() {
    gpioWrite(LEFT1,0);
    gpioWrite(LEFT2,0);
    gpioWrite(RIGHT1,0);
    gpioWrite(RIGHT2,0);
}

float get_distance() {
    gpioWrite(TRIG,0);
    usleep(2);
    gpioWrite(TRIG,1);
    usleep(10);
    gpioWrite(TRIG,0);

    while(gpioRead(ECHO)==0);
    uint32_t start = gpioTick();
    while(gpioRead(ECHO)==1);
    uint32_t end = gpioTick();

    float distance = (end-start)/58.0; // cm
    return distance;
}

int main() {
    if (gpioInitialise()<0) {
        printf("GPIO初期化失敗\n");
        return 1;
    }

    while(1) {
        float front = get_distance();
        printf("前: %.1f cm\n", front);

        if(front>25) {
            motor_forward();
        } else {
            motor_stop();
            sleep(1);
        }
        usleep(100000);
    }

    gpioTerminate();
    return 0;
}
