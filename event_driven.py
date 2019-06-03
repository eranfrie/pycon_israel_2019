from threading import Thread
from queue import Queue
import simpy

time_tick = 1
sim = True

class EventDrivenQueue(Queue):
    def __init__(self, env, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if sim:
            env.process(self._sim_join(env))

    def _sim_join(self, env):
        while True:
            self.join()
            yield env.timeout(time_tick)

class EventDrivenComponent:
    def run(self):
        while True:
            msg = q.get()
            print(f"Got {msg}")
            q.task_done()

class SimRobot:
    def work(self, env):
        i = 1
        while True:
            q.put(f"msg {i}")
            i += 1
            yield env.timeout(time_tick)

env = simpy.Environment()
# q = EventDrivenQueue(env)
q = Queue()
Thread(target=EventDrivenComponent().run, daemon=True).start()
env.process(SimRobot().work(env))
env.run(until=50)
