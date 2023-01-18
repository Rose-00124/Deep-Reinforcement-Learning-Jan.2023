# Deep-Reinforcement-Learning-Jan.2023
2023년도 1월에 진행한 강화 학습 공부 자료

1월부터 진행한 강화 학습 공부 자료로 '파이썬과 케라스로 배우는 강화학습, 이웅원 저, 위키북스'를 통해 주로 공부하였다.
관련 논문을 읽으며 강화 학습의 기초를 다지고 있으며, 이를 하드웨어 구현에 적용하려고 한다.

# 1. 하기에 앞서..
아나콘다 라이브러리를 설치한다. (설치 : https://www.anaconda.com/products/individual)
설치는 default로 진행하면 된다.
아나콘다 설치가 완료되면 anaconda prompt를 켜서 'conda env list'를 입력한다. (env = environment)
*주의 :  맨 앞에 'conda'를 붙혀야 명령어 인식 가능*

# 2. 아나콘다 기본 환경 설정
'conda env list'를 입력하면 base만 존재하는 것을 확인할 수 있다.
새로운 가상 환경에서 진행할 수 있도록 (그것이 아나콘다의 목적임) 'conda create -n [가상환경 이름] python=3.7'를 입력한다.
그러면 가상환경 이름의 새로운 환경이 python 3.7 version으로 생성된다.
base에서 다시 'conda env list'를 입력하면 방금 생성산 가상환경 이름을 확인할 수 있다.
마지막으로, 'conda activate [가상환경 이름]'을 입력하면 base 디렉토리에서 생성한 가상환경 디렉토리로 들어갈 수 있다.

# 3. 학습에 필요한 라이브러리 및 패키지 다운로드
방금까지 가상환경을 만들고 들어가는 것이 완료된다면, 이제 학습에 필요한 것들을 다운로드 해야한다.
다운로드는 다음 검색창에 입력해 필요한 것을 다운받으면 된다. (다운 : https://anaconda.org/)
ex) tensorflow를 다운받기 위해 명령 프롬프트에 'conda install -c conda-forge tensorflow'를 입력하면 설치가 된다.
설치 중간에 'y/n'을 물을 때는 y 혹은 enter를 입력하면 된다.
학습에 따라 필요 라이브러리는 다르기 때문에, 학습 목적에 따라 라이브러리를 선택해 다운로드한다.
*주의 : 컴퓨터 환경에 따라 (혹은 GPU에 따라) 다르므로 version을 잘 보고 설치해야 함*

# 4. PyCharm IDE 설치
IDE는 통합 개발 환경이며, (https://en.wikipedia.org/wiki/Integrated_development_environment)를 통해 의미를 확인할 수 있다.
*공부를 하면서 최대한 영어 자료를 보는 것이 중요하며, 한 번 잘 읽어놓으면 개발에 도움이 많이 됨*
그 중에서 PyCharm은 많이 사용하는 환경 중 하나이다. (사실 Visual Studio Code를 더 많이 사용하는 것 같기도 한데, 상관은 없다.)
다운로드는 https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows 에서 진행하면 된다.
이 또한 아나콘다와 같이 default로 설치하면 된다.

# 5. PyCharm Interpreter 설정
설치가 완료되면 새롭게 프로젝트를 진행할 수 있는 페이지를 선택할 수 있다.
선택하는 단계에서 파이썬 인터프리터를 선택하게 되는데, 이 때 방금 설치했던 아나콘다를 통해 진행할 수 있으므로,
User의 envs 파일 내 만들어 놓은 가상환경 이름 파일을 선택하고 그 곳의 'python.exe'를 선택한다.
*가끔 진행하다가 인터프리터가 변경되어 라이브러리 인식이 안되서 코드가 동작하지 않기에 설정을 통해 확인해야 함*
이 단계가 끝나면 기초적인 사용을 위한 준비가 끝났다고 할 수 있다.
