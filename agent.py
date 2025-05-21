import numpy as np
import random

class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_q_value(self, state, action):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        return self.q_table[state][action]

    def choose_action(self, state):
        if random.random() < self.epsilon: 
            return random.choice(self.actions)
        else:  
            if state not in self.q_table:
                self.q_table[state] = np.zeros(len(self.actions))  
            return np.argmax(self.q_table[state])

    def update_q_value(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(len(self.actions))

        future_rewards = np.max(self.q_table[next_state]) 
        self.q_table[state][action] += self.alpha * (reward + self.gamma * future_rewards - self.get_q_value(state, action))

    def save_q_table(self, filename):
        np.save(filename, self.q_table)

    def load_q_table(self, filename):
        self.q_table = np.load(filename, allow_pickle=True).item()
