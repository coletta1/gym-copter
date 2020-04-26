'''
gym-copter Environment superclass

Copyright (C) 2019 Simon D. Levy

MIT License
'''

from gym import Env
import numpy as np

from gym_copter.dynamics.djiphantom import DJIPhantomDynamics

class CopterEnv(Env):

    metadata = {
        'render.modes' : ['human', 'rgb_array'],
        'video.frames_per_second' : 30
    }

    def __init__(self, dt=0.001, disp='hud'):

        self.num_envs = 1
        self.display = None

        # We handle time differently if we're rendering
        self.dt = dt

        # Default to HUD display
        self.disp = disp

        # Also called by reset()
        self._reset()

    def _update(self, action):

        # Update dynamics and get kinematic state
        self.dynamics.setMotors(action)
        self.dynamics.update(self.dt)
        self.state = self.dynamics.getState()

        # Update timestep
        self.tick += 1

        # We're done when vehicle has crashed
        self.done = self.state[4]>0 and self.state[5]>1

        return self.done

    def reset(self):

        self._reset()
        return self.state

    def render(self, mode='human'):

        # Default to HUD display if start3d() wasn't called
        if self.display is None:
            from gym_copter.envs.rendering.hud import HUD
            self.display = HUD()
 
        return self.display.display(mode, self.state) if self.display.isOpen() else None

    def tpvplotter(self):

        from gym_copter.envs.rendering.tpv import TPV

        # Pass title to 3D display
        return TPV(self)

    def close(self):

        Env.close(self)        

    def time(self):

        return self.tick * self.dt

    def _reset(self):
        
        self.state = np.zeros(12)
        self.dynamics = DJIPhantomDynamics()
        self.tick = 0
        self.done = False
