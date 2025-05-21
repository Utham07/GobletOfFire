import numpy as np
import matplotlib.pyplot as plt

def plot_results():
    rewards = np.loadtxt("rewards.csv", delimiter=",")
    success_rate = np.loadtxt("success_rate.csv", delimiter=",")
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(rewards, label="Reward per Episode", color='blue')
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Reward Curve')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(success_rate, label="Success Rate per Episode", color='green')
    plt.xlabel('Episode')
    plt.ylabel('Success Rate')
    plt.title('Success Rate Curve')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_results()
