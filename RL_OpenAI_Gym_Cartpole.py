# 라이브러리 설치 및 임포트
import gym
import numpy as np
import time, math, random
from typing import Tuple

# KBinsDiscretizer를 임포트하지 못하는 경우, 콘솔에서 conda update scikit-learn 실행
from sklearn.preprocessing import KBinsDiscretizer

# CartPole-v1
env = gym.make('CartPole-v1')
env

# 학습 전 에이전트의 동작 확인 및 실행환경 시각화 / Visualise Environment, Simulation
policy = lambda obs: 1

for _ in range(5):
    obs = env.reset()
    for _ in range(80):
        actions = policy(obs)
        obs, reward, done, info = env.step(actions)
        env.render()
        time.sleep(0.05)

env.close()

# 정책 입력 / Hard Coded Policy
#Simple policy function
policy = lambda _,__,___, tip_velocity : int( tip_velocity > 0 )

##Q-learning
# Cartpoles의 연속형 상태공간을 이산형 상태공간으로 변환
# Conver Cartpoles continues state space into discrete one
n_bins = ( 6 , 12 )
lower_bounds = [ env.observation_space.low[2], -math.radians(50) ]
upper_bounds = [ env.observation_space.high[2], math.radians(50) ]

def discretizer( _ , __ , angle, pole_velocity ) -> Tuple[int,...]:
    """Convert continues state intro a discrete state"""
    est = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy='uniform')
    est.fit([lower_bounds, upper_bounds ])
    return tuple(map(int,est.transform([[angle, pole_velocity]])[0]))

# Q 값의 테이블을 영행렬로 초기화 / Initialise the Q value with zeros
Q_table = np.zeros(n_bins + (env.action_space.n,))
Q_table.shape

# 정책 함수 생성 / Create a policy function
def policy( state : tuple ):
    """Choosing action based on epsilon-greedy policy"""
    return np.argmax(Q_table[state])

# Q 값의 갱신 / Update function
def new_Q_value( reward : float ,  new_state : tuple , discount_factor=1 ) -> float:
    """Temperal diffrence for updating Q-value of state-action pair"""
    future_optimal_value = np.max(Q_table[new_state])
    learned_value = reward + discount_factor * future_optimal_value
    return learned_value

# 학습효율 체감수준을 반영한 적응형 학습 / Decaying learning rate
# Adaptive learning of Learning Rate
def learning_rate(n : int , min_rate=0.01 ) -> float  :
    """Decaying learning rate"""
    return max(min_rate, min(1.0, 1.0 - math.log10((n + 1) / 25)))

# 탐색효율 체감수준을 반영한 적응형 학습 / Decaying exploration rate
def exploration_rate(n : int, min_rate= 0.1 ) -> float :
    """Decaying exploration rate"""
    return max(min_rate, min(1, 1.0 - math.log10((n  + 1) / 25)))

# 학습 후 에이전트의 동작 확인 및 실행환경 시각화
# 에피소드 횟수 :10,000회, 연속형 상태정보를 이산형화
n_episodes = 10000
for e in range(n_episodes):

    # Siscretize state into buckets
    current_state, done = discretizer(*env.reset()), False

    while done == False:

        # policy action
        action = policy(current_state)  # exploit

        # insert random action
        if np.random.random() < exploration_rate(e):
            action = env.action_space.sample()  # explore

        # increment environment
        obs, reward, done, _ = env.step(action)
        new_state = discretizer(*obs)

        # Update Q-Table
        lr = learning_rate(e)
        learnt_value = new_Q_value(reward, new_state)
        old_value = Q_table[current_state][action]
        Q_table[current_state][action] = (1 - lr) * old_value + lr * learnt_value

        current_state = new_state

        # Render the cartpole environment
        env.render()
