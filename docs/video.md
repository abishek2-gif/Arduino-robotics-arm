# Robotic arm animated explainer
[Watch / download the MP4](../media/robotic-arm-explainer.mp4). If GitHub shows a file page, use the raw/download control and open it in your video player.

64 seconds • 1280×720 • 24 fps • H.264 • silent with burned-in captions.
[Separate subtitles](../media/robotic-arm-explainer.srt)

| Time | Chapter |
|---|---|
| 00:00 | Meet the four-axis arm |
| 00:08 | Base rotation |
| 00:16 | Shoulder movement |
| 00:24 | Elbow reach |
| 00:32 | Gripper opening and closing |
| 00:40 | Joystick input, Arduino logic and separate servo power |
| 00:48 | Simulated reach, grip, lift, turn and place |
| 00:56 | Calibration and planned camera upgrade |

This is a stylized 3D animation, not real hardware footage or a verified mechanical model. The gripper orientation and geometry are illustrative. The scripted sequence is not implemented in the current joystick firmware. Camera control remains planned.

## Regenerate
Requires Python 3, Pillow, NumPy, FFmpeg with libx264, and DejaVu Sans fonts.
On Linux with those dependencies installed, run from the repository root:

```sh
python3 tools/render_video.py
```

The renderer writes the MP4 and preview JPGs into media/. The font paths near the top may need updating on Windows or macOS. Subtitles are supplied separately; update them if changing chapter timing.

## Validation
The output was checked with ffprobe for duration, codec, resolution and frame rate, and representative frames were visually inspected. Physical hardware remains untested.
