The Goblet of Fire

This project simulates Harry Potter navigating through a maze to reach the Cup while avoiding Death Eaters. The agent (Harry) uses the Q-Learning algorithm to learn the best path to take, iterating through multiple episodes to improve its decision-making process.

Requirements: 
    To run the project, you need Python 3.x installed along with the following libraries:
    - pygame: For rendering the environment and agent.
    - numpy: For handling the Q-table and mathematical operations.
    - matplotlib: For plotting the results.

How to Run:
1. Prepare the Maze:
    Create or download a maze file in .txt format. Each maze file consists of a grid where walls are represented by X and free spaces by <space>.
2. Train the Agent:
    Run train.py to start the training process. During training, the harry will interact with the maze and learn how to navigate towards the Cup while avoiding Death Eaters.
    You will be prompted to input:
    - Number of Death Eaters (1 or more).
    - Path to the maze file (e.g., maze.txt).
    Harry will train for a specified number of episodes, and you will see the maze and agent movements visualized.
3. Visualize the Training Process:
    During the training, the environment will be displayed using pygame with:
    - Black boxes representing walls (X in the maze).
    - Green square for Harry.
    - Red squares for Death Eaters.
    - Yellow square for the Cup.
4. Track Results
    Training will log:
    Rewards per episode: Stored in rewards.csv.
    Success rate per episode: Stored in success_rate.csv.
5. Evaluate Results:
    Once the agent completes training, you can plot the results using results.py.
    This will generate plots showing:
    - The total reward per episode.
    - The agent’s success rate in escaping the maze.
6. Test the trained agent - Harry:
    After training, the agent’s Q-table is saved as q_table.npy. You can load this file to run the trained agent in the maze or test the agent's performance on new mazes.

Note: 
Q-Learning Algorithm
The agent - Harry uses Q-learning, a reinforcement learning algorithm, to navigate the maze. The agent updates its Q-values based on the rewards it receives and the state-action pairs it encounters.

The Q-values are updated using this formula: Q(s, a) = Q(s, a) + α * (reward + γ * max(Q(s', a')) - Q(s, a)).
    where s: Current state
        a: Action taken
        s': Next state
        α: Learning rate
        γ: Discount factor
        reward: The reward received for the action
