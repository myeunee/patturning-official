import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# 이미지 불러오기
pageIcon = Image.open("image/page_icon.png")
mainIcon= Image.open("image/main_icon.png")
patturning_bg = Image.open("image/patturning_bg.png")
guideline = Image.open("image/guideline.png")
issues = Image.open("image/issues.png")
mit = Image.open("image/mit.jpg")
graph = Image.open("image/graph.png")
filtering = Image.open("image/filtering.png")

#Layout
st.set_page_config(
    page_title="PatTurning",
    layout="wide",
    page_icon=pageIcon,
    initial_sidebar_state="expanded")

#Data Pull and Functions
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

#Options Menu
with st.sidebar:
    selected = option_menu('PatTurning', ["Intro", 'About','How To Contribute', 'Commit Convention', 'Members'], 
                           menu_icon="cast", default_index=0)

# Intro 페이지
if selected == "Intro":
    # Header
    st.image(patturning_bg, use_column_width=True, width=300)
    st.markdown("""
## 현명한 소비의 시작, PatTurning

##### 당신의 합리적인 소비를 위해, PatTurning이 다크패턴을 필터링합니다!

- 1️⃣ 온라인 쇼핑 중 혼란이나 압박을 유발할 수 있는 잘못된 요소들을 필터링
- 2️⃣ 최근 가격 변동을 분석하여 거짓 할인 전략을 판별해 소비자에게 합리적인 구매 근거 제공
- 3️⃣사용자는 다크 패턴이 의심되는 텍스트를 직접 리포트할 수 있으므로, 다크 패턴 탐지 정확도를 높일 수 있음
                
  """)
    
    st.write("")
    st.divider()
    st.markdown("""
### ⚒️ Tech
PatTurning이 사용하는 대표 오픈소스는 다음과 같다.
- **[Airflow]** - 데이터 파이프라인을 자동화, 워크플로우 관리
- **[BeautifulSoup4]** - 크롤링하여 데이터 수집
- **[FastAPI]** - 모델 서빙
- **[TensorFlow]** - 딥러닝 모델 학습 및 추론
- **[Scikit-Learn]** - 모델 훈련 및 평가
- **[Spring Boot]** - 백엔드 서버 개발
- **[Chart.js]** - 직관적이고 반응형 그래프 UI
- **[Docker]** - 컨테이너
- **[Nginx]** - 리버스 프록시 및 로드 밸런서 기능 제공
- **[Pika]** - RabbitMQ와의 통신
- **[GCP]** - 클라우드 환경에 인프라 구축과 및 배포
  """)
    
    st.write("")
    st.divider()
    st.markdown("""                 
### ✅ Install
[**Chrome 웹스토어 링크**](https://chromewebstore.google.com/detail/patturning/nlldmjdghbedjmnbkpgjnnanpecmmpad)
   """)          
                    
    st.write("")
    st.divider()
    st.markdown("""        
### 👉 Contact
[**PatTurning GitHub**](https://github.com/HyejiYu/PatTuning)
  """)

    st.write("")
    st.divider()
    st.markdown("""                     
### ⚕️ License
Patturning is distributed under the terms of the Apache License (Version 2.0).  
See [LICENSE](https://github.com/HyejiYu/PatTuning/blob/main/LICENSE) for details.

""")
    
    st.write("")
    st.divider()


#Intro Page
if selected=="About":
    st.markdown("""
# Patturning의 기능

#### 1️⃣ 다크패턴 탐지 기능

Patturning의 **다크 패턴 탐지 기능**을 통해 웹사이트에서 특정 문구가 등장할 때 해당 문구를 자동으로 블러 처리하여 사용자가 쉽게 인지할 수 있도록 한다.
  """)
    st.image(filtering, width=600)
    st.write("")
    st.divider()
    st.markdown("""
##### 다크 패턴 문구 예시
  """)
    st.image(guideline, caption="공정거래위원회 가이드라인", width=600)
    st.markdown("""


| 다크패턴              | 유형                             |
|-----------------------|----------------------------------|
| 오도형                | 아니요, 정가를 지불하고 싶습니다 |
| 압박형(소비유도)      | 45개 남음                        |
| 압박형(다른사람행동알림) | 월간 구매 34,422개              |
| 압박형(긴급성)         | 품절임박! 딱 4개 남았어요        |

---
                

#### 2️⃣ 온라인 쇼핑몰 상품 가격 추적

Patturning은 온라인 쇼핑몰의 상품 가격을 추적하여 소비자가 다크 패턴에 쉽게 영향을 받지 않도록 지원한다.
""")
    st.image(graph, width=600)
    st.markdown("""

---

#### 3️⃣ 다크패턴 문구 신고 기능

Patturning은 사용자가 직접적으로 불편함을 느끼는 다크패턴 요소를 신고 기능을 통해 수집한다.
이를 통해, 서비스가 기반을 두고 있는 필터링 모델의 신뢰도를 지속적으로 보완하여 소비자 불편을 제거하는 것을 목표로 한다.

---

### 💡 Patturning의 기대 효과

- **소비자 보호 강화**: 비합리적인 구매 유도 행위를 차단하여 소비자의 권익을 보호한다.
- **윤리적인 웹 디자인**: 기업들이 윤리적인 웹 디자인을 추구하도록 유도한다.
- **사회적 가치 창출**: 투명한 커뮤니케이션 촉진을 통해 소비 환경 개선을 목표로 한다.
""")
    st.divider()


if selected == "How To Contribute":
    st.markdown("""
**Patturning은 [MQ Producer](#Producer), [Airflow DAG](#Airflow-DAG), [Model](#Model-학습-및-사용-방법) 에 대한 contribution이 가능하다.**

### Producer

Contributors는 직접 크롤링 코드를 작성하여 특정 사이트, 상품의 지속적인 가격 정보를 수집할 수 있다.  
본 서비스의 경우 크롤링 코드는 Cloud Run에 배포하였고, Airflow DAG에서 Cloud Run으로 HTTP `POST` 요청을 보낸다.  
Contributors는 Airflow에서 제공하는 Operator로 연결되는 모든 종류의 크롤링 코드를 작성할 수 있다.  
`contribute/mq_producer_template.py` 파일에 `RabbitMQProducer` 클래스를 참고해 `contribute/crawl_template.py` 파일에 크롤링할 코드를 작성할 수 있다.  
크롤링할 정보는 다음과 같다. 크롤링 코드에서 RabbitMQProducer를 이용해 produce할 때 전달해야 하는 데이터는 다음과 같은 형태의 dict형태와 dict로 이루어진 list이 가능하다.

```json
{
  "category_name": category_name,
  "product_id": product_id,
  "price": price
}
```

위와 같은 `json` 형태로 RabbitMQ로 전송한다. 만약 어떤 필드에 해당하는 값이 없다면 None(python)으로 정의한다.  
RabbitMQ의 username, password, hostname, port, vhost 정보는 서버의 환경변수 파일로 존재한다. 다음은 `python`에서 RabbitMQ 호스트와 연결하기 위한 정보를 가져오는 방식이다.

```python
username=os.getenv('RABBITMQ_USERNAME')
password=os.getenv('RABBITMQ_PASSWORD')
hostname=os.getenv('RABBITMQ_HOSTNAME')
port=os.getenv('RABBITMQ_PORT')
vhost=os.getenv('RABBITMQ_VHOST')
```

Contributors가 사용하고자 하는 `queue` 이름과 환경변수명을 Issues에 요청하면 해당 내용을 바탕으로 환경변수를 생성한다.  
이슈가 `Close as Completed`되면 RabbitMQ 객체들이 정상적으로 생성되었고 문제없이 실행된다는 의미이며, `Close as not planned`되면 임의의 이유로 객체들을 생성하지 않겠다는 의미이다.  
Issues를 생성할 때에는 [RabbitMQ Queue request] 템플릿을 참고해 주길 바란다.

---

### Airflow DAG

가격 변동 추이 파악에 중요한 정보를 파악하기 위해 schedule_interval은 최대 6시간 이내로 설정되어 상품 정보는 하루에 최소 4회 기록되어야 한다.

DAG는 사이트 당 하나씩 생성되도록 지정하고 있다.  
Contributors가 크롤링하고자 하는 사이트를 PatTurning에서 이미 크롤링 중이라면 미리 개발된 DAG를 기반으로 기여해야 한다. 크롤링 할 웹사이트의 `robots.txt`를 확인하여 규칙을 꼭 준수하도록 한다.
새로운 사이트를 크롤링할 시 `contribute/*` 내 파일을 복사하여 각각의 용도에 맞는 디렉토리에서 개발한 뒤 PR해야 한다. 각 파일의 PR 위치는 다음과 같다.

- **crawl_template**: `airflow/requirements/`
- **DAG_template**: `airflow/`
- **mq_consumer_template**: `messagequeue/consumer/`
- **mq_producer_template**: `messagequeue/producer/`

`contribute/requirements.txt` 파일은 airflow 환경에 설치되어야 하는 가상환경 패키지이다. 테스트 환경에 필요하다면 참고하길 바란다.

DAG의 dag_id는 `{site_name}_Crawling_DAG` 형태로 설정해야 한다. 크롤링 외 기능의 DAG를 추가할 시 Issues에 요청 바란다.

Airflow DAG는 기본적으로 producer와 consumer가 병렬로 실행되도록 설계되어 있다.  
이미 정의된 `HomePlus_dag`의 경우 상품 약 600,000 개의 상품 데이터를 소비하는 데 3개의 consumer를 사용하여, 대략 12분이 소요된다.  
이를 참고하여 consumer 개수를 적절히 지정하길 바란다. 

(*Recommended*) 본 서비스는 DAG가 한 번 실행되고 나면 실행 성공/실패 여부를 메일로 전송한다.  
이를 통해 DAG 실패 시 즉각 조치할 수 있도록 한다.  
DAG 개발 시 필요한 기능이 포함된 task를 실행한 뒤 마지막 task로 메일을 전송하는 task를 포함하는 것을 권장한다.  
`airflow/requirements/modules.py` 파일에 존재하는 `collect_task_results()` 함수는 기본적으로 제공하고 있는 메일 전송 포맷이다.  
더욱 자세한 내용을 메일로 받아보고 싶으면 사용자 정의 함수를 정의하여 사용하길 바란다.

---

### How to Test your code

위 과정을 통해 Producer, DAG를 개발하면 `crawl_template.py` 의 `crawl()`  함수를 조건에 맞게 작성한 후 테스트 해 볼 수 있다.

#### 파이썬 가상환경 설정

권장 Python 버전은 `3.12`로, 해당 파이썬이 설치된 가상환경에 `airflow/requirements.txt` 파일을 설치한다.

```
$ pip install -r requirements.txt
```

#### RabbitMQ 설치 및 실행
rabbitMQ(>=3.11.2)를 설치한 뒤 실행한다.

- **Windows**
공식 사이트:  https://www.rabbitmq.com/docs/install-windows
    
```bash
$ rabbitmq-service start
```

- **macOS**
    
```bash
$ brew install rabbitmq
$ brew services start rabbitmq
```


#### RabbitMQ Queue 설정

1. RabbitMQ 관리 콘솔 접속 (http://localhost:15672) 
    
    username: `guest`, password: `guest`
    
2. 상단 `Queues and Streams` 메뉴에서 새로운 큐 `test.queue` 추가

#### 최종 테스트

1. RabbitMQ Consumer 실행
    
```bash
$ python mq_consumer_template.py
```
    
2. 크롤링 및 RabbitMQ로의 Produce
    
```bash
$ python crawl_template.py
```
    
위 과정이 정상적으로 수행되면, `output` 디렉토리 내부에 수집한 상품과 가격 정보가 담긴다.

---

### Model-학습-및-사용-방법

---

[eulneul/patturning-model · Hugging Face](https://huggingface.co/eulneul/patturning-model)
**GRU기반 다크패턴 탐지 모델**

 다크패턴 문구를 넣으면 어떤 다크패턴에 해당하는지 다중 분류를 수행하며, 새로운 다크패턴 데이터셋을 활용하여 모델을 추가적으로 학습시킬 수 있다.

#### [1] 필요한 라이브러리 설치
- python 3.9.6

```bash
$ pip install huggingface_hub
```

```
huggingface-hub==0.25.2
tensorflow==2.11.0
keras==2.11.0
```

#### [2] 모델 & 토크나이저 불러오기

- 모델 불러오기

 모델은 `huggingface_hub` 라이브러리의 `snapshot_download`를 이용해서 다운받을 수 있다. 혹은 레포지토리의 주소를 복사해서 다운로드도 가능하다.
`saved_model.pb` 파일과 `variables` 폴더가 포함된 모델 폴더 전체 경로를 다운받는 것이 권장된다.

```python
from huggingface_hub import snapshot_download

model_dir = snapshot_download(repo_id="eulneul/patturning-model")
model = tf.keras.models.load_model(model_dir)
```

- 토크나이저 불러오기

```python
tokenizer_path = hf_hub_download(repo_id="eulneul/patturning-model", filename="Tokenizer/tokenizer.json", repo_type="model")
with open(tokenizer_path, "r") as f:
    tokenizer_json = f.read()

tokenizer = tokenizer_from_json(tokenizer_json)
```

#### [3] 모델 추론하기

```python
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#데이터 예제
doc = ... #your text data

x = tokenizer.texts_to_sequences(doc)
padded_x = pad_sequences(x, 16)

prediction = model.predict(padded_x)
print(np.armax(prediction, axis=1))
```

모델이 분류하는 label은 다음과 같다.


**모델 라벨 목록**

| 번호 | 유형                    | 예시                                | 설명                                             |
|------|-------------------------|-------------------------------------|--------------------------------------------------|
| 0  | 다크패턴 아님           |                                     |                                                  |
| 1  | 오도형                  | 아니요, 정가를 지불하고 싶습니다     | 사용자를 혼란시키거나 헷갈리게 할 수 있어요       |
| 2  | 압박형 / 소비유도       | 20개 남음 / 함께할인 / 3개 담으면 2000원 할인 | 압박감을 주거나 소비를 유도해요 |
| 3  | 압박형 / 긴급성         | 기간 한정 세일, 품절 임박           | 결정을 빠르게 하도록 유도해요                     |
| 4  | 압박형 / 다른 소비자 행동 알림 | 100명이 보고있습니다, 300개 판매됨 | 다른 사용자의 행동을 따라하도록 유도해요         |


#### [4] 모델 학습하기

 새 데이터를 사용하여 모델을 추가로 훈련할 수 있다. 모델은 기본적으로 5개의 label을 분류한다. 다음은 추가적인 데이터로 학습시키는 예시이다.

```python
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

# Compile the model
model.compile(optimizer=Adam(learning_rate=1e-4), loss='categorical_crossentropy', metrics=['accuracy'])

# Example training data
X_train = ...  # Your input data
y_train = ...  # Your labels

x = tokenizer.texts_to_sequences(X_train)
padded_x = pad_sequences(x, 16)
y_train_one_hot = to_categorical(y_train, num_classes=5)

# Train the model
model.fit(X_train, y_train_one_hot, epochs=5, batch_size=32)
```

### * 추가 데이터 라벨링하기

원하는 사이트의 다크패턴에 대해 라벨링하여 새 데이터셋을 만들 수 있다.

1. 우선, 다음 과정들을 수행한다.

```bash
$ git clone https://github.com/HyejiYu/PatTuning.git
$ cd Patturning/contribute/model
```

2. `htmls`  디렉토리 내부에 원하는 사이트 이름의 디렉토리를 만들고,  파일을 `htmls/{site_name}` 디렉토리에 `{file_name}.html` 형식의 이름으로 저장한다.
3. `regexs_by_site.py` 파일을 아래와 같은 형식으로 수정한다.

```python
site_darkpatterns = {
	"{site_name}": {
		{num_label}: [
			"\d+개 남음",  # 다크 패턴을 정규 표현식 형태로 입력
			"품절 임박",
		],
	}
}
```

4. 다음 명령어를 수행하면 `labels`  디렉토리 내부에 라벨링 된 csv 파일이 저장된다.

```bash
$ python labeling.py
```
                """)






if selected == "Commit Convention":
    st.markdown("""
### Issue Templates
원하는 작업에 알맞은 템플릿을 사용해 이슈를 생성한다.
- Bug Report
- 기타 자유양식 템플릿
- 새로운 기능 요청 & 제안
- RabbitMQ Queue 생성 요청


### commit convention
commit message는 **[Emoji] Footer: Description** 형식으로 작성한다. 이모지는 [GitMoji](https://gitmoji.dev/)를 참고한다.

e.g.
```
[🐛] fix: fix a bug(what and where etc)
```

### Footer

| Type        | Description                             |
| ----------- | --------------------------------------- |
| `Feat`      | 새로운 기능 추가                               |
| `Design`    | CSS 등 사용자 UI 디자인 변경                     |
| `!HOTFIX`   | 급하게 **치명적인 버그**를 고쳐야 하는 경우              |
| `Comment`   | 필요한 **주석** 추가 및 변경                      |
| `Fix`       | **버그 수정**                               |
| `Update`    | 원래 정상적으로 동작했지만 **보완**의 개념               |
| `Add`       | **추가**                                  |
| `Remove`    | **파일을 삭제하는 작업**                         |
| `Refactor`  | **리팩토링**                                |
| `Simplify`  | 약한 수정, **코드 단순화**                       |
| `Improve`   | 호환성, 테스트 커버리지, 성능, 검증 기능, 접근성 등의 **향상** |
| `Implement` | 코드 추가보다 **큰 단위**의 구현                    |
| `Correct`   | 문법의 오류나 타입의 변경, 이름 변경 등                 |
| `Prevent`   | 특정 행동을 **방지**                           |
| `Avoid`     | **회피**                                  |
| `Move`      | 코드나 파일의 **이동**                          |
| `Rename`    | 이름 변경                                   |


### Pull Request
PR Request를 사용하며 PR title은 다음과 같이 정의한다.
`<type>([optional scope]) : <description>`

- `[optional scope]` : 추가 정보
- `<description>` : PR에 대한 설명

| Type | Description |
| --- | --- |
| **build** | Changes that affect the build system or external dependencies (dependencies update) |
| **docs** | **문서변경**: Documentation only changes |
| **feat** | **새로운 기능 추가**: A new feature  |
| **fix** | **버그 수정**: A bug fix  |
| **chore** | **기타 수정**: Changes which does not touch the code (ex. manual update of release notes). It will not generate release notes changes  |
| **refactor** | **리팩토링**: A code change that contains refactor  |
| **style** | **스타일 수정**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)  |
| **test** | **테스트 코드 추가, 수정, 삭제**: Adding missing tests or correcting existing tests and also changes for our test app  |
| **perf** | **성능 개선**: A code change that improves performance (I do not think we will use it) |



### Git Branch

- `dev`: 출시를 위해 개발하는 브랜치
- `feat/{기능명}`: 새로운 기능 개발하는 브랜치
- `refactor/{기능명}`: 개발된 기능을 리팩토링하는 브랜치
- `hotfix`: 출시 버전에서 발생한 버그를 수정하는 브랜치

e.g.

- main
- dev/feat/login
- dev/feat/register

""")


# Members 페이지
if selected == "Members":
    st.markdown("""
> **패터닝** 팀은 경희대학교 소프트웨어융합대학 학생 5명으로 구성되어 있습니다. 
> 저희 팀은 사용자의 합리적인 소비를 돕기 위해 다크패턴을 감지 및 필터링하는 서비스를 개발하고 있습니다. 
> 특히 정보 소외 계층에게 취약한 다크패턴의 사회적 문제점을 알리려 노력하고자 합니다.
""")