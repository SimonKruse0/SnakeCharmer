from typing import Optional

import numpy as np

from src.enums.direction import Direction
from playingfield import PlayingField
from Directors.base_director import BaseDirector

#states:
# l1 distance vector to the apple.         dist(head, apple) = (apple_x-head_x, apple_y-head_y)
# l1 distance vector to nearst snakebody.   dist(head, body) = (body_x-head_x, body_y-head_y)
# l1 distance vector to nearst border.   dist(head, obsticle) = (apple_x-head_x, apple_y-head_y)
#  

class Director(BaseDirector):
    def __init__(self) -> None:
        self.eat_reward = 10
        self.die_reward = -20
        self.move_reward = -0.1
        self.q_table = self.init_q_tabel()
        self.epsilon = 0.1
        self.learning_rate = 0.1
        self.discount = 0.95
        
    def init_q_tabel(self):
        q_table = {}
        distance_1_range = [-1,1]
        distance_2_range = [-2,-1,1,2]
        for x_apple in distance_2_range:
            for y_apple in distance_2_range:
                for x_body in distance_2_range:
                    for y_body in distance_2_range:
                        for x_obsticle in distance_1_range:
                            for y_obsticle in distance_1_range:
                                q_table[((x_apple, y_apple), (x_body,y_body), (x_obsticle, y_obsticle))] = np.random.uniform(-5, 0, 4)

    def dist_to_nearest_body_part(playing_field: PlayingField, snake_head):
        #body is 1's in self.playing_area
        pass

    def dist_to_nearest_boundary(snake_head):
        pass

    def clip_observations(observation):
        #To fint the limited state space -> smaller q-tabel
        pass

    def get_direction(
        self, playing_field: PlayingField
    ) -> Direction:
        snake_head = playing_field.snake_head
        apple = playing_field.apple

        self.observation = (snake_head-apple,self.dist_to_nearest_body_part(playing_field, snake_head), self.dist_to_nearest_boundary())
        if np.random.random() > self.epsilon:
            # GET THE ACTION
            obs = self.clip_distances(self.observation)
            action = np.argmax(self.q_table[obs])
        else:
            action = np.random.choice([Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT])
        # Take the action!
        return action


    def update_q_tabel(self):
        reward = self.get_reward()
        current_q = self.q_table[self.observation][action]
        if self.termination():
            new_q = reward
        else:
            new_obs = (snake_head-apple,self.dist_to_nearest_body_part(playing_field, snake_head), self.dist_to_nearest_boundary())
            new_obs = self.safe_guard(new_obs)
            max_future_q = np.max(self.q_table[new_obs])
            new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (reward + self.discount * max_future_q)
        self.q_table[self.observation][action] = new_q
