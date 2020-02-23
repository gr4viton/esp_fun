from time import sleep
from machine import PWM
import math


class MixinZigzag:

    def zig(self, amin=0, amax=180, astep=10, tstep=0.5, reverse=False):
        if amin > amax:
            amin, amax = amax, amin
            reverse = not reverse
        rng = list(range(amin, amax, astep))
        if reverse:
            rng = list(reversed(rng))

        for the in rng:
            self.write_angle(degrees=the)
            sleep(tstep)

    def release(self):
        self.pwm.duty(0)

    def zig_duty(self, dmin=31, dmax=122, dstep=10, tstep=0.5, reverse=False):
        """d = duty_cycle, t = time."""
        rng = list(range(dmin, dmax, dstep))
        if reverse:
            rng = list(reversed(rng))

        for the in rng:
            self.write_duty(the)
            sleep(tstep)

    def zigzag_duty(self, dmin=31, dmax=122, dstep=10, tstep=0.5):
        # self._zigzag(self.zig_duty, dmin=dmin, dmax=dmax, dstep=dstep, tstep=tstep)
        self._zigzag(self.zig_duty, dmin, dmax, dstep, tstep)

    def zigzag(self, amin, amax, astep, tstep, direction=0, repetition=1):
        zigzag = direction == 0
        forward = direction > 0
        backward = direction < 0
        for i in range(repetition):
            if zigzag:
                self._zigzag(self.zig, amin, amax, astep, tstep)
            if forward:
                self.zig(amin, amax, astep, tstep)
            if backward:
                self.zig(amin, amax, astep, tstep, reverse=True)

    def _zigzag(self, method, *args):
        method(*args)
        method(reverse=True, *args)


class Servo(MixinZigzag):
    """
    A simple class for controlling hobby servos.

    Args:
        pin (machine.Pin): The pin where servo is connected. Must support PWM.
        freq (int): The frequency of the signal, in hertz.
        min_us (int): The minimum signal length supported by the servo.
        max_us (int): The maximum signal length supported by the servo.
        angle (int): The angle between the minimum and maximum positions.

    """
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.pwm = PWM(pin, freq=freq, duty=0)

    def write_duty(self, duty_cycle):
        self.pwm.duty(duty_cycle)

    def write_us(self, us):
        """Set the signal to be ``us`` microseconds long. Zero disables it."""
        if us == 0:
            self.pwm.duty(0)
            return
        us = min(self.max_us, max(self.min_us, us))
        duty = us * 1024 * self.freq // 1000000
        self.pwm.duty(duty)

    def write_angle(self, degrees=None, radians=None):
        """Move to the specified angle in ``degrees`` or ``radians``."""
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)
