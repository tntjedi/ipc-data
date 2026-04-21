# IPC Test Results 

## Structure

```text
plots/
├── baseline runs/
├── water_current_plots/
│   ├── head_current_plots/
│   └── tail_current_plots/
└── sensor_noise_plots/
    ├── mild_sensor_noise_plots
    ├── moderate_sensor_noise_plots
    └── high_sensor_noise_plots
```

**3 runs per scenario**

---

# Baseline Runs

Reference for **both** water-current and sensor-noise tests.

Conditions:

```text
Current = 0
Sonar noise stddev = 0.027
```

Folder:

```text
baseline runs/
```

---

# Water Current Tests

## Head Current (Opposing Flow)

```text
Horizontal angle = 3.14159
Vertical angle = 0
Noise = 0
```

| Case     | Mean Current (m/s) |
| -------- | ------------------ |
| Mild     | 0.5                |
| Moderate | 1.0                |
| Harsh    | 1.6                |

## Tail / Assisting Current

```text
Horizontal angle = 0.7854
Vertical angle = 0
Noise = 0
```

| Case     | Mean Current (m/s) |
| -------- | ------------------ |
| Mild     | 0.5                |
| Moderate | 1.0                |

---

# Sensor Noise Tests

No water current.



| Case     | Sonar Noise Stddev |
| -------- | ------------------ |
| Baseline | 0.027              |
| Mild     | 0.034              |
| Moderate | 0.041              |
| High     | 0.054              |

---

# Metrics Logged

* Time to goal
* Total path distance
* Goal distance vs time
* Speed
* Acceleration
* Pitch rate
* Yaw rate
* XY trajectory
* Depth profile

---

# Source Topic

```text
/rexrov/pose_gt
```

Obstacle sensing via multibeam sonar pipeline.

---

