# This code is supported by <https://youtu.be/dZ4vw6v3LcA>

# Lecture 1 : Introduction of Reinforcement Learning
# Reinforcement Learning : Computational approach to learning from interaction

# Lecture 2 : Playing OpenAI GYM Games
import gym

# Setting environment for "Taxi-v1" game
env = gym.make("Taxi-v1") 

# Initialization (Caution)
observation = env.reset()

for _ in range(1000):
  env.render() # Output
  action = env.action_space.sample() # your agent is here (this takes random actions)
  observation, reward, done, info = env.step(action) # State, Reward, T/F, another info

# Lecture 3 : Q-learning & Dummy Q-learning (table)
# Policy using Q-function
# 1) Find Max Value 2) Something Value (Maybe, Max Value) <-- argmax(a')Q(s1, a)

# Initialize table with all zeros
Q = np.zeros([env.observation_space.n, env.action_space.n]) # <-- Create table

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

# Lecture 4 : Q-learning (table), exploit & exploration and discounted reward
# Using e-greedy
for i in range (num_episodes):
  e = 1./((i/100) + 1) 
  
# The Q-Table learning algorithm
while not done:
  # Choose an action by e-greedy
  if np.random.rand(1) < e:
    action = env.action_space.sample()
  
  else:
    action = np.argmax(Q[state,:])
    
# Exploit vs. Exploration : add random noise
for i in range (1000):
  a = argmax(Q(s,a) + random_values / (i + 1))
  
# Choose an action by greedy (with noise) picking from Q table
action = np.argmax(Q[state,:] + np.random.randn(1, env.action_space.n) / (i + 1))

# Discount factor
dis = .99

# Update Q-Table with new knowledgement using decay rate
Q[state.action] = reward + dis * np.max(Q[new_state, :])

# Lecture 5 : Q-learning on Nondeterministic worlds!
# Update Q-Table with new knowledgement using learning rate
Q[state,action] = (1 - learning_rate) * Q[state,action] + learning_rate * (reward + dis * np.max(Q[new_state, :]))

# Lecture 6 : Q-Network (with Deep Q-Learning algorithm)
# Q-Network for Frozen Lake

# Input and output size based in the env
input_size = env.observation_space.n # 16 <-- output
output_size = env.action_space.n # 4 <-- output

# These lines establish the feed-forward part of the network used to choose actions
X = tf.placeholder(shape=[1,input_size], dtype=tf.float32) # start input
W = tf.Variable(tf.random_uniform([input_size, output_size], 0, 0.01)) # weight
Qpred = tf.matmul(X,W) # Out Q prediction
Y = tf.placeholder(shape = [1, output_size], dtype = tf.float32) # Y label

loss = tf.reduce_sum(tf.square(Y-Qpred))
train = tf.train.GradientDescentOptimizer(learning_rate = learning_rate).minimize(loss)
Qs[0,a] = reward + dis * np.max(Qs1)

# Train our network using target (Y) and predicted Q (Qpred) values
sess.run(train, feed_dict = {X : one_hot(s), Y : Qs})

# Choose an action by greedily (with e chance of random action) from the Q-network
Qs = sess.run(Qpred, feed_dict = {X : one_hot(s)}) # table --> network
if np.random.rand(1) < e :
  a = env.action_space.sample()
  
else :
  a = np.argmax(Qs)
  
if done :
  # Update Q, and no Qs+1, since it/s a terminal state
  Qs[0,a] = reward
 
else :
  # Obtain the Q_s1 values by feeding the new state through our network
  Qs1 = sess.run(Qpred, feed_dict = {X : one_hot(s1)})
  # Update Q
  Qs[0,a] = reward + dis * np.max(Qs1)
  
# Q-Network for Cart Pole
import gym
env = 
  

