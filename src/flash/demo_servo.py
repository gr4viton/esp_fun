from time import sleep
from flash.servo import Servo
from flash.peripherals import pwm_d5, led_blue

from machine import Pin


def hrkadlo_1():
    pwm_d5 = Pin(5)
    pin = pwm_d5
    servo = Servo(pin)
    while True:

        # for args in args_list:
        #     servo.zigzag_duty(*args)
        tstep = 0.1
        astep = 5

        for i in range(4):
        # for i in range(1, 1):
            # tstep = i / 100

            twait1 = 0.3
            # twait2 = 4.5
            twait2 = 4.3
            a_list = [
                # [0, 180, 10, 0.5],
                # [0, 180, 10, 0.2],
                [0, 180, astep, tstep, 1],
                twait2,
                # [180, 140, astep, tstep, 0],
                # twait1,
                [0, 180, astep, tstep, -1],
                twait2,
                # [0, 40, astep, tstep, 0],
                # twait1,
            ]

            for args in a_list:
                if isinstance(args, list):
                    servo.zigzag(*args)
                    continue
                servo.release()
                sleep(args)

        sleep(10)

        # args = args_list[2]
        # servo.zig(*args, reverse=False)

        # for it in range(0, 20):
        #     deg = it * 9
        #     servo.write_angle(deg)
        # for it in range(51, 102):
        #     print(it)
        #     servo.pwm.duty(it)
        #     sleep(3)
        #     tog = it % 2
        #     led_blue.value(tog)


def demo_servo():
    while True:
        args_list = [
            [31, 122, 1, 0.05],
            [31, 122, 10, 0.5],
        ]
        args = args_list[2]
        servo.zig(*args, reverse=False)
