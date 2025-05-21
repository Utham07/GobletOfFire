import pygame
import time
import numpy as np
from maze_env import MazeEnvironment
from agent import QLearningAgent
import csv

NUM_DEATH_EATERS = int(input("No.of Death Eaters : "))

maze = input("Enter path to maze (.txt file) : ")
env = MazeEnvironment(maze, num_death_eaters=NUM_DEATH_EATERS)
agent = QLearningAgent(actions=[0, 1, 2, 3]) 

pygame.init()
screen = pygame.display.set_mode((env.width * 40, env.height * 40))
pygame.display.set_caption("Harry Potter - Goblet of Fire Maze")

episodes = 500
consecutive_successes = 0
max_successes = 10

rewards_log = []
success_log = []

for episode in range(episodes):
    state = env.reset()
    total_reward = 0

    for _ in range(200):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.update_q_value(state, action, reward, next_state)
        state = next_state
        total_reward += reward

        env.render(screen)
        pygame.display.flip()
        time.sleep(0.05)

        if done:
            if reward == 10:
                consecutive_successes += 1
                success_log.append(1)
            else:
                consecutive_successes = 0
                success_log.append(0)
            break

    rewards_log.append(total_reward)
    print(f"Episode {episode + 1}, Reward: {total_reward}, Success Streak: {consecutive_successes}")

    if consecutive_successes >= max_successes:
        print(f"✅ Harry escaped successfully {max_successes} times in a row.")
        break

agent.save_q_table("q_table.npy")
np.savetxt("rewards.csv", np.array(rewards_log), delimiter=",")
np.savetxt("success_rate.csv", np.array(success_log), delimiter=",")

pygame.quit()
