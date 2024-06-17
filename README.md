# Machine Learning & IoT-Powered Driver Monitoring System for Drowsiness & Alcohol Detection

## Overview

This project focuses on developing a real-time, low-cost, and non-intrusive system to monitor driver drowsiness and alcohol levels using machine learning (ML) and Internet of Things (IoT) technologies. The primary objective is to reduce traffic accidents caused by driver fatigue and alcohol intake.

## Features

1. **Drowsiness Detection:**
   - Utilizes facial recognition and behavior analysis to detect signs of driver fatigue.
   - Employs a steering pressure sensor to measure the driver’s grip strength.
   - If the driver's eyes are closed for more than 3 seconds, a buzzer sounds to alert and awaken the driver.

2. **Alcohol Detection:**
   - Incorporates an MQ3 alcohol sensor to detect the presence of alcohol.
   - When the blood alcohol concentration (BAC) detected by the MQ3 sensor exceeds 0.30, the vehicle’s ignition is automatically disabled.
   - The system then sends the driver's real-time location to the nearest police station using the NEO6M GPS module.
   - The police can verify the situation, administer punishment, and provide a secure four-digit PIN. The driver can only restart the vehicle using this PIN, ensuring the car will not start without it.

3. **System Components:**
   - **Arduino Board:** Central processing unit that interfaces with sensors and modules.
   - **LCD Display:** Provides real-time feedback to the driver.
   - **Sensors:** MQ3 alcohol sensor, steering pressure sensor, and additional sensors for enhanced accuracy.
   - **GPS Module (NEO6M):** Tracks the vehicle's real-time location.
   - **Microcontroller (ESP8266):** Manages the IoT integration and communication.

4. **Safety and Privacy:**
   - Ensures the safety of interventions without compromising vehicle control.
   - Adheres to strict privacy policies to protect user data.

## Methodology

- **Data Collection and Preprocessing:**
  - Collected diverse datasets of facial images and driving behaviors.
  - Preprocessed data for training ML models.

- **Model Development:**
  - Developed ML models for detecting drowsiness and alcohol levels.
  - Integrated IoT sensors with the ML models to create a cohesive system.

- **System Integration:**
  - Real-time integration within the vehicle to alert drivers promptly.
  - User-friendly interface for ease of use.

## Future Scope

- **Advanced Detection:** Implementing more sophisticated ML algorithms for higher accuracy.
- **Broader Application:** Expanding the system to detect other driver impairments and integrating with autonomous driving technologies.
- **Enhanced User Experience:** Improving the interface and feedback mechanisms for better user interaction.

## Conclusion

The developed driver monitoring system aims to enhance road safety by addressing two critical causes of traffic accidents—drowsiness and alcohol consumption. By leveraging ML and IoT, this project provides a proactive solution to reduce accident rates and save lives.

## Contribution
Contributions are welcome! If you have any suggestions, bug fixes, or feature enhancements, feel free to submit a pull request.

---

For more details, refer to the full project report by Mohammad Shahid Raza from Amity University, Ranchi.
