# This code is supported by <https://youtu.be/dZ4vw6v3LcA>

# Lecture 1 : Introduction of Reinforcement Learning
# Reinforcement Learning : Computational approach to learning from interaction

# Lecture 2 : Playing OpenAI GYM Games
import gym

# Setting environment for "Taxi-v1" game
env = gym.make("Taxi-v1") 

# Initialization (Caution)
observation  = env.reset()

for _ in range(1000):
  env.render() # Output
  action = env.action_space.sample() # your agent is here (this takes random actions)
  observation, reward, done, info = env.step(action) # State, Reward, T/F, another info

# Lecture 3 : Q-learning & Dummy Q-learning (table)
# Policy using Q-function
# 1) Find Max Value 2) Something Value (Maybe, Max Value) <-- argmax(a')Q(s1, a)

# Initialize table with all zeros
Q = np.zeros([env.observation_space.n, env.action_space.n]) # <=- Create table

# Set learning parameters
num_episodes = 2000 # count

# Create lists to contain total rewards and steps per episode
rList = []
for i in range (num_episodes):
  # Reset environment and get first new observation
  state = env.reset() # Initialization and get the first state
  rAll = 0
  done = False # Setting to False value for end game
  
  # The Q-Table learning algorithm
  while not done:
    action = rargmax(Q[state, :]) # random + argmax
    
    # Get new state and reward from environment
    new_state, reward, done, _ = env.step(action)
    
    # Update Q-Table with new knowledge using learning rate
    Q[state,action] = reward + np.max(Q[new_state, :])
    
    state = new_state
