# Articular Command of an RP Type Robotic Manipulator (Com_Rob)

This project focuses on simulating various control strategies for a simple RP-type robotic manipulator using MATLAB-SIMULINK. The objective is to develop and test control schemes for the joint variables of the robot to follow predefined trajectories. 

## Overview

The manipulator consists of:
- **Rotational Joint (R):** Allows the first link to rotate around the vertical axis.
- **Prismatic Joint (P):** Enables linear motion of the second link.

The goal is to control the variables q1(t) and q2(t) to follow predefined profiles combining uniform acceleration, constant velocity, and uniform deceleration. The desired configurations for the manipulator start at (q1(t0) = 0, q2(t0) = 0.5) and end at (q1(t1) = π/2, q2(t1) = 1).


## Key Components

1. **Dynamic Model:** Includes inertia, Coriolis, centrifugal, and gravitational effects.
2. **Actuators:** Represented with parameters like motor torque, reduction ratios, and effective inertia.
3. **Control Strategies:** 
   - **PD Control:** Evaluated for various reduction ratios to optimize system stability and performance.
   - **PID Control:** Enhanced precision through integral action.
   - **Nonlinear Centralized Control:** Incorporates feedforward strategies for better trajectory tracking.
   - **Decoupled Linearizing Control:** Implements nested loops for improved linearity and decoupling.

## Tasks Performed

- Implementation of different control laws under linear and nonlinear models.
- Simulation of system responses in MATLAB-SIMULINK under varying conditions (e.g., gravitational effects, perturbations).
- Analysis of the effects of different reduction ratios and controller parameters on system performance.

## Tools Used

- **MATLAB-SIMULINK:** For modeling and simulating the robotic manipulator.
- **Custom S-Functions:** Developed to implement advanced control laws, including centralized anticipation and decoupling.

## Outcomes

This project provides an in-depth understanding of joint control strategies for RP manipulators, highlighting the trade-offs between linear and nonlinear control approaches and their impact on precision, stability, and robustness.

---

Feel free to explore the simulation files and modify the control parameters to observe their effects on the manipulator's behavior.
