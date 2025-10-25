# Pygame Asteroids Clone

A classic arcade-style asteroids game built with Python and the Pygame library. This project was developed as part of the Boot.dev curriculum, focusing on object-oriented programming, game loop mechanics, and vector math.

## Features

* **OOP Design:** All game entities (Player, Asteroid, Shot) are encapsulated classes.
* **Game Loop Management:** Uses Pygame's `sprite.Group` to efficiently update and draw all objects.
* **Physics:** Player rotation, thrust, and bullet velocity are all delta-time-independent for smooth, consistent performance.
* **Collision Detection:** Accurate circle-based collision detection.
* **Asteroid Splitting:** Large asteroids split into two medium asteroids, and medium into two small, faster asteroids.
* **Scoring System:** A skill-based scoring system that rewards more points for destroying smaller, harder-to-hit targets.

## Controls

* **Move Forward:** `UP ARROW`
* **Move Backward:** `DOWN ARROW`
* **Rotate Left:** `LEFT ARROW`
* **Rotate Right:** `RIGHT ARROW`
* **Shoot:** `SPACEBAR`

## How to Run

This project requires Python 3 and Pygame.

1. **Clone the repository**:

```bash
git clone https://github.com/amitb-dev/pygame-asteroids.git
cd pygame-asteroids
```

2. **Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

(On Windows, use `.venv\Scripts\activate`)

3. **Install dependencies:**
```bash
python3 -m pip install -r requirements.txt
```

4. **Run the game:**
```bash
python3 main.py
```

## Tech Stack

* **Python 3**
* **Pygame**