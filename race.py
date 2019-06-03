from random import randint
import simpy

num_robots = 3
sim_time = 5  # seconds
time_tick = 0.5

class Robot:
    def move(self, env, id):
        pos = 0
        while True:
            pos += randint(1,2)
            print(f"{env.now} r_{id} moved to {pos}")
            yield env.timeout(time_tick)

env = simpy.Environment()

for i in range(num_robots):
    r = Robot()
    env.process(r.move(env, id=i))

env.run(until=sim_time)
