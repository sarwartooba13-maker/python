import tkinter as tk
import random
import math

# Window setup
WIDTH, HEIGHT = 800, 600
root = tk.Tk()
root.title("Achaaaa Wala Fireworks Project by You!")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 10)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.color = color
        self.life = 100
        self.id = canvas.create_oval(x-2, y-2, x+2, y+2, fill=color, outline="")

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15  # gravity
        self.life -= 2
        canvas.coords(self.id, self.x-2, self.y-2, self.x+2, self.y+2)
        if self.life <= 0:
            canvas.delete(self.id)
            return False
        return True

class Firework:
    def __init__(self):
        self.x = random.randint(100, WIDTH-100)
        self.y = HEIGHT
        self.target_y = random.randint(100, HEIGHT//2)
        self.vy = -8
        self.color = random.choice(["#ff00ff", "#00ffff", "#ffff00", "#ff4444", "#44ff44"])
        self.id = canvas.create_oval(self.x-3, self.y-3, self.x+3, self.y+3, fill=self.color, outline="white")
        self.exploded = False
        self.particles = []

    def update(self):
        if not self.exploded:
            self.y += self.vy
            canvas.coords(self.id, self.x-3, self.y-3, self.x+3, self.y+3)
            if self.y <= self.target_y:
                self.explode()
        else:
            # update all particles
            self.particles = [p for p in self.particles if p.update()]
            if not self.particles:
                return False
        return True

    def explode(self):
        self.exploded = True
        canvas.delete(self.id)
        for _ in range(60): # 60 particles
            self.particles.append(Particle(self.x, self.y, self.color))

fireworks = []

def animate():
    # Kabhi kabhi new firework launch karo
    if random.random() < 0.08:
        fireworks.append(Firework())
    
    # Sab ko update karo
    for fw in fireworks[:]:
        if not fw.update():
            fireworks.remove(fw)
            
    root.after(16, animate) # 60 FPS

animate()
root.mainloop()