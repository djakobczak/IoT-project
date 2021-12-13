#!/usr/bin/env python
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 720)
    camera.framerate = 24
    for filename in camera.record_sequence([
            'vid%02d.h264' % (h + 1)
            for h in range(24)
            ], quality=25):
        camera.wait_recording(60 * 60)
execfile('recorder.py')