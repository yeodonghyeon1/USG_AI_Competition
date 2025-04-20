# USG AI 경진대회 프로젝트

본 저장소는 USG AI 경진대회의 제조혁신 부문 참가 프로젝트를 담고 있습니다.

## 프로젝트 개요

### 초급 부문
- PCB 기판 이미지에서 불량 검출을 수행하는 이진 분류 모델
- CNN 기반의 딥러닝 모델을 사용하여 정상/불량 분류
- 입력 이미지 크기: 128x128x3 (RGB)
- 출력: 2개 클래스 (정상/불량)

### 중급 부문
- PCB 부품(IC, 커패시터, 저항) 분류 모델
- CNN 기반의 딥러닝 모델을 사용하여 3가지 부품 분류
- 입력: 부품 이미지
- 출력: 3개 클래스 (IC, 커패시터, 저항)

## 프로젝트 구조

```
.
├── 제조혁신대회_그냥해보는팀_중급/    # 중급 부문 프로젝트
│   ├── model/                    # 학습된 모델 저장
│   ├── picture/                  # 시각화 결과
│   ├── test_data/               # 테스트 데이터셋
│   ├── train_data/              # 학습 데이터셋
│   ├── train.ipynb              # 학습 코드
│   ├── test.ipynb               # 테스트 코드
│   ├── one.json                 # 설정 파일
│   └── answer_sample.json       # 제출 양식
└── 제조혁신대회_그냥해보는팀_초급/    # 초급 부문 프로젝트
    ├── model/                    # 학습된 모델 저장
    ├── test_npy/                # 테스트 데이터 (numpy 형식)
    ├── train_npy/               # 학습 데이터 (numpy 형식)
    ├── train_img5/              # 학습 이미지
    ├── test_img/                # 테스트 이미지
    ├── mis2/                    # 기타 데이터
    ├── train.ipynb              # 메인 학습 코드
    ├── train_test.ipynb         # 학습/테스트 통합 코드
    ├── spect.ipynb              # 데이터 분석 코드
    └── anwer_sample.csv         # 제출 양식
```

## 모델 구조

### 공통 CNN 구조
- 컨볼루션 레이어: 3x3 커널 사용
- 활성화 함수: ReLU
- 배치 정규화 적용
- Dropout(0.5) 사용하여 과적합 방지
- MaxPooling으로 특징 압축

### 초급 부문 모델
- 입력 채널: 3 (RGB)
- 출력 채널: [64, 128, 256, 512]
- 완전연결층: 65536 → 4096 → 1000 → 2
- CUDA GPU 사용하여 학습 수행

### 중급 부문 모델
- 입력 채널: 10
- 출력 채널: [64, 128, 256, 512]
- 완전연결층: 65536 → 4096 → 1000 → 3
- CUDA GPU 사용하여 학습 수행

## 기술 스택

- Python
- PyTorch
- NumPy
- OpenCV
- scikit-learn
- Matplotlib
- Pandas

## 언어 구성

- Jupyter Notebook: 94.6%
- Python: 5.4%

## 팀 정보

팀명: 그냥해보는팀

## 라이센스

이 프로젝트는 별도의 라이센스가 명시되어 있지 않습니다.

## 기여 방법

1. 이 저장소를 포크합니다
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성합니다