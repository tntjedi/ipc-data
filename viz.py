#!/usr/bin/env python3

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

run_number = "INSERT NUMBER HERE ---"

folder = os.path.expanduser("~/Desktop/plots")

## CHANGE THE FOLDER NAME HERE ---

summary_file = os.path.join(folder, f"ipc_noisy_high_{run_number}_summary.csv")
path_file    = os.path.join(folder, f"ipc_noisy_high_{run_number}_path.csv")
motion_file  = os.path.join(folder, f"ipc_noisy_high_{run_number}_motion.csv")

if not os.path.exists(summary_file):
    print("Missing:", summary_file)
    sys.exit(1)

if not os.path.exists(path_file):
    print("Missing:", path_file)
    sys.exit(1)

if not os.path.exists(motion_file):
    print("Missing:", motion_file)
    sys.exit(1)

summary = pd.read_csv(summary_file)
path = pd.read_csv(path_file)
motion = pd.read_csv(motion_file)

path = path.apply(pd.to_numeric, errors="coerce")
motion = motion.apply(pd.to_numeric, errors="coerce")

print("\n========== RUN {} ==========".format(run_number))

for i in range(len(summary)):
    print("{} : {}".format(summary["metric"][i], summary["value"][i]))

print("============================\n")

t_path = path["time_sec"].to_numpy()
x = path["x"].to_numpy()
y = path["y"].to_numpy()
z = path["z"].to_numpy()
goal_dist = path["goal_distance"].to_numpy()

t_motion = motion["time_sec"].to_numpy()
speed = motion["speed"].to_numpy()
acc = motion["acceleration"].to_numpy()
omega_pitch = motion["omega_y_pitch"].to_numpy()
omega_yaw = motion["omega_z_yaw"].to_numpy()

plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.plot(x, y, linewidth=2)
plt.scatter(x[0], y[0], s=80, marker='o', label="Start")
plt.scatter(x[-1], y[-1], s=80, marker='x', label="End")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("XY Trajectory")
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(t_motion, speed, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Linear Speed")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(t_motion, omega_pitch, linewidth=2, label="Pitch Rate")
plt.plot(t_motion, omega_yaw, linewidth=2, label="Yaw Rate")
plt.xlabel("Time (s)")
plt.ylabel("Angular Rate (rad/s)")
plt.title("Angular Velocities")
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(t_motion, acc, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration Curve")
plt.grid(True)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(t_path, goal_dist, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Distance to Goal (m)")
plt.title("Goal Distance vs Time")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(x, z, linewidth=2)
plt.xlabel("X (m)")
plt.ylabel("Z (m)")
plt.title("Depth Profile (X-Z)")
plt.grid(True)
plt.show()