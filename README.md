# Projectile Motion Simulator

An interactive web application built with Python and Streamlit that simulates the parabolic motion of a projectile under the effects of gravity. Visualize the trajectory in real time by adjusting the launch parameters.

---

## Features

- Supports all 5 cases of projectile motion (horizontal launch, from ground level, with initial height, negative angle, and vertical launch)
- Automatic calculation of flight time, maximum range, and maximum height
- Interactive trajectory chart with dark theme
- Mathematical formulas rendered in LaTeX
- Wide responsive layout

---

## Screenshots

> Add screenshots of your app here
<img width="1806" height="473" alt="image" src="https://github.com/user-attachments/assets/210685d3-e7e1-4c68-af28-edfe697a4a5b" />

<img width="1771" height="1012" alt="image" src="https://github.com/user-attachments/assets/71d79f8d-7728-4565-8aba-aa50c39c66ea" />


---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DavidProgrammer11/projectile-motion-simulator.git
cd projectile-motion-simulator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

---

## Dependencies

```
streamlit
numpy
matplotlib
```

Or install them with:
```bash
pip install streamlit numpy matplotlib
```

---

## Usage

| Parameter | Description | Range |
|---|---|---|
| Angle (°) | Launch angle relative to the horizontal | -90° to 90° |
| Initial velocity (m/s) | Magnitude of the launch velocity | ≥ 0 |
| Initial height (m) | Height from which the projectile is launched | ≥ 0 |

The app automatically calculates:
- **Flight time** using the quadratic formula
- **Maximum range** using horizontal uniform motion
- **Maximum height** at the instant when vertical velocity equals zero

---

## Physics

Projectile motion combines two simultaneous movements:

**Horizontal (uniform motion):**
$$x(t) = v_0 \cos(\theta) \cdot t$$

**Vertical (uniformly accelerated motion):**
$$y(t) = h_0 + v_0 \sin(\theta) \cdot t - \frac{1}{2} g t^2$$

**Flight time** (root of the quadratic equation):
$$t = \frac{-b - \sqrt{b^2 - 4ac}}{2a} \quad \text{where } a=-\frac{g}{2},\ b=v_0\sin\theta,\ c=h_0$$

**Maximum height** (when $v_y = 0$):
$$t_{peak} = \frac{v_0 \sin(\theta)}{g} \qquad y_{max} = h_0 + v_0 \sin(\theta) \cdot t_{peak} - \frac{1}{2} g \cdot t_{peak}^2$$

---

## Project Structure

```
projectile-motion-simulator/
│
├── app.py               # Main application
├── requirements.txt     # Dependencies
└── README.md            # This file
```

---

## Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

---

## Author

Developed by [@DavidProgrammer11](https://github.com/DavidProgrammer11) as a computational physics project.

---

## License

MIT License — free to use, modify, and distribute.
