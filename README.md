# -POLYMORPHISM-Traffic-Management-System.

## Case Study: Smart Traffic Management System

### Introduction

This project demonstrates the concept of **polymorphism** in Object-Oriented Programming (OOP) using Python.

A smart city uses intelligent traffic devices. Each device receives the same `activate()` command, but each device performs a different task when activated.

The project demonstrates how different objects can respond differently to the same method call.

## Requirements

The system contains:

### Parent Class
- `TrafficDevice`

### Child Classes
- `TrafficLight`
- `SpeedCamera`
- `PedestrianSignal`
- `EmergencySiren`

Each child class overrides the `activate()` method inherited from the parent class.

## Concepts Demonstrated

### 1. Inheritance

The child classes inherit from the `TrafficDevice` parent class. This allows them to share a common structure and method.

### 2. Method Overriding

Each child class provides its own implementation of the `activate()` method.

For example:
- `TrafficLight` changes the traffic light.
- `SpeedCamera` monitors vehicle speed.
- `PedestrianSignal` displays a pedestrian crossing signal.
- `EmergencySiren` sounds an emergency warning.

### 3. Polymorphism

Polymorphism allows objects of different classes to be treated in the same way. In this project, all traffic devices are stored in a list and the same `activate()` method is called on each object without checking its type.

### 4. Extensibility

The `EmergencySiren` class can be added to the system without modifying the activation loop. This demonstrates how polymorphism makes the system easier to extend.

## Program Structure

```text
POLYMORPHISM-Traffic-Management-System/
│
├── traffic_management.py
└── README.md
