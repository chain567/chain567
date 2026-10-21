[← Back to profile](../README.md)

# VibeGuide · Haptic Navigation

![Purpose](https://img.shields.io/badge/Purpose-Haptic_navigation-555555?style=flat)
![Android](https://img.shields.io/badge/Android-3DDC84?style=flat&logo=android&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat&logo=kotlin&logoColor=white)
![Jetpack Compose](https://img.shields.io/badge/Jetpack_Compose-4285F4?style=flat&logo=jetpackcompose&logoColor=white)
![Bluetooth](https://img.shields.io/badge/Bluetooth_Classic-0082FC?style=flat&logo=bluetooth&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat&logo=arduino&logoColor=white)

**Fall 2025 · NYU Tandon EG 1004 team project · Updated for my portfolio in 2026**

## The idea

I came up with the idea of supplementing on-screen navigation with vibration cues from a connected wearable. VibeGuide's Android app finds a route, follows the phone's location, and sends commands to left and right Arduino-based vibration units. The active side indicates the turn direction, and the vibration level changes with distance to the waypoint.

This was a four-person course project in Fall 2025. I am now organizing it for my portfolio. [Explore the Android source and Arduino firmware →](https://github.com/chain567/Haptic-Navigation-Software)

## My role

I originated the concept and served as the software/coding lead. I planned the features, researched Bluetooth options, sourced components from the lab, and guided development step by step. My focus was making the app and hardware work together, testing each addition, and refining the prototype's behavior.

I also participated hands-on throughout circuit assembly, completed approximately half the soldering, and delivered the main technical explanation in our presentation.

I was responsible for the final simple functional test. We checked the connected prototype and confirmed that the basic navigation-to-vibration workflow worked.

## The prototype

![Original VibeGuide prototype, including circuit assembly and wearable strap](../assets/haptic-prototype.jpg)

*Our team's 2025 prototype, with an Arduino Uno-class controller, Bluetooth serial module, coin-style motor, enclosure, and wearable strap.*

## Distance, direction, and commands

The Android app combines straight-line distance to the next waypoint with a left/right turn instruction. During normal approach, it sends low (`1`) or high (`2`) intensity to the turn side and off (`0`) to the other side.

Both sides receive a warning pulse (`3`) on first entering 50 m, and again at an intermediate waypoint within 10 m. Arrival requests `2` on both sides, followed by stop (`0`). The receiver's `3` command produces two brief pulses and returns to off.

The firmware uses 9600-baud serial input and PWM pin 10, with low/high duty values of 120 and 255. The app includes separate Bluetooth connection controls, a command display, and a wall-test mode with 5 m simulated movement steps.

## System architecture

![Our original VibeGuide system flowchart from 2025](../assets/haptic-system-flow.png)

*Our original 2025 team flowchart.*

## What I took from the project

This was an early hands-on project that brought together feature planning, Android-to-Arduino communication, physical assembly, and a working demonstration. I learned through building and refining the system, and through explaining how the software and hardware fit together.

For a future version, I'd focus on handling GPS noise, structured turn instructions, and reconnect behavior. The current version is a functional course-project prototype with simple testing.

My other projects include a [Visio automation utility](https://github.com/chain567/visio-batch-image), an [AV operations demo](https://github.com/chain567/nyu-av-sample-app), and [algorithm notes](https://github.com/chain567/leetcode-notes).
