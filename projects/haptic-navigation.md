[← Back to profile](../README.md)

# VibeGuide · Haptic Navigation

![VibeGuide: Android navigation to left/right haptic cues](../assets/haptic-overview.svg)

**Fall 2025 · NYU Tandon EG 1004 team project · Portfolio write-up updated in 2026**

Kotlin · Jetpack Compose · Google Maps · Bluetooth Classic SPP · Arduino Uno · PWM

## The idea

I came up with the idea of supplementing on-screen navigation with vibration cues from a connected wearable. VibeGuide's Android app finds a route, follows the phone's location, and sends commands to left and right Arduino-based vibration units. The active side indicates the turn direction, and the vibration level changes with distance to the waypoint.

This was a four-person course project in Fall 2025. I am now organizing it for my portfolio. The Android and Arduino source repository is currently private.

## My role

I originated the concept and served as the software/coding lead. I planned the features, researched Bluetooth options, sourced components from the lab, and guided development step by step. My focus was making the app and hardware work together, testing each addition, and refining the prototype's behavior.

I also participated hands-on throughout circuit assembly, completed approximately half the soldering, and delivered the main technical explanation in our presentation.

I was responsible for the final simple functional test. We checked the connected prototype and confirmed that the basic navigation-to-vibration workflow worked.

## The prototype

![Original VibeGuide prototype, including circuit assembly and wearable strap](../assets/haptic-prototype.jpg)

*Our team's 2025 prototype, with an Arduino Uno-class controller, Bluetooth serial module, coin-style motor, enclosure, and wearable strap.*

## Distance, direction, and commands

![Distance bands, left/right outputs, and command events](../assets/distance-commands.svg)

The Android app combines straight-line distance to the next waypoint with a left/right turn instruction. During normal approach, it sends low (`1`) or high (`2`) intensity to the turn side and off (`0`) to the other side.

Both sides receive a warning pulse (`3`) on first entering 60 m, and again at an intermediate waypoint within 10 m. Arrival requests `2` on both sides, followed by stop (`0`). The receiver's `3` command produces two brief pulses and returns to off.

The firmware uses 9600-baud serial input and PWM pin 10, with low/high duty values of 120 and 255. The app includes separate Bluetooth connection controls, a command display, and a wall-test mode with 5 m simulated movement steps.

## System architecture

![Our original VibeGuide system flowchart from 2025](../assets/haptic-system-flow.png)

*Our original 2025 team flowchart. The app uses a 60 m warning threshold; this drawing shows 50 m.*

## What I took from the project

This was an early hands-on project that brought together feature planning, Android-to-Arduino communication, physical assembly, and a working demonstration. I learned through building and refining the system, and through explaining how the software and hardware fit together.

For a future version, I'd focus on command sequencing, Bluetooth recovery, and smoother waypoint handling under GPS noise. The current version is a functional course-project prototype with simple testing.

My other projects include a [Visio automation utility](https://github.com/chain567/visio-batch-image), an [AV operations demo](https://github.com/chain567/nyu-av-sample-app), and [algorithm notes](https://github.com/chain567/leetcode-notes).
