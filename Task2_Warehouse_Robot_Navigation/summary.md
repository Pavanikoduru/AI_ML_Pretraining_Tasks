# Task 2 – Robotics: Warehouse Robot Navigation

Problem Description:

Warehouses need robots that can swiftly - yet carefully - navigate rows, grabbing things then setting them down.

When things crash into each other, or deliveries take the long way around, work grinds to a halt - meaning expenses climb.

Target Users: Warehouse operators, robotics engineers

Bumps into things, takes a wonky path, late arrivals – that’s the trouble

Proposed AI/ML Solution:

Robots gather details about surroundings - employing both laser scanners alongside cameras.

Handle information with small computers at the source - they link up via either AWS or Azure systems.

Cameras will spot hurdles using a visual system modeled on how brains work. It analyzes pictures to find things blocking the way.

Figure out how to get where you need to go without bumping into things by learning from trial alongside error. It’s about finding the quickest route through practice.

Get robots thinking for themselves - put the smarts right where they are, so they react instantly.

For keeping tabs on how things run, ship system records alongside notifications about trouble spots directly to online watchdogs.

Cloud & Tech Stack:

|   Component             |   Technology Used                       |
|-------------------------|-----------------------------------------|
| Sensor Data Source      | LIDAR, Camera (IoT)                     |
| Edge Processing         | AWS Greengrass / Azure IoT Edge         |
| Model Training          | CNN + RL on AWS SageMaker / Azure ML    |
| Deployment              | Edge Inference on Robots                |
| Monitoring              | AWS CloudWatch / Azure Monitor          |


Expected Outcome:

Robots move through warehouse rows - no bumps, quick like anything.

Fewer crashes, resources stretched further.

Tasks run smoother, systems grow easily, operations become more secure.
