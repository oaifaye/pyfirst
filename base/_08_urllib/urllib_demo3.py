# request:GET
import urllib.request
import time
import _thread as thread
import random
import hashlib

total = 100000
t = time.time()
seed = '10cd3e37-1d1e-4a02-8ab8-7e9c2c974102'

contents = [
            '多线程类似于同时执行多个不同程序，多线程运行有如下优点.',
           '使用线程可以把占据长时间的程序中的任务放到后台去处理',
           '用户界面可以更加吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度',
           '线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。',
           '每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。',
    '其中thread模块需要避免的一个原因是：它不支持守护线程。当主线程退出时，所有的子线程不论它们是否还在工作，都会被强行退出。',
    '有时我们并不期望这种行为，这就引入了守护线程的概念。',
    ' Threading模块支持守护线程，它们工作流程如下：守护线程一般是一个等待客户请求的服务器，如果没有客户提出请求，它就在那等着。',
    '如果你设定一个线程为守护线程，就表示你在说这个线程是不重要的，在进程退出时，不用等待这个线程退出，正如网络编程中服务器线程运行在一个无限循环中，一般不会退出的。',
    '如果你的主线程要退出的时候，不用等待那些子线程完成，那就设定这些线程的daemon属性。即，线程开始（调用',
    '如果你想要等待子线程完成再退出，那就什么都不用做，或者显示地调用thread.setDaemon(False)以保证其daemon标志位False。',
    '新的子线程会继承其父线程的daemon标志，整个Python会在所有的非守护线程退出后才会结束，即进程中没有非守护线程存在的时候才结束。',
    'threading的Thread类是你主要的运行对象。它有很多thread模块里没有的函数。',
        'FindingTaskRelevantFeaturesforFewShotLearningbyCategoryTraversal',
        'EdgeLabelingGraphNeuralNetworkforFewShotLearning',
        'ATheoryofFermatPathsforNonLineofSightShapeReconstructionbyShumianXin,SotirisNousias,KyrosKutulakos,AswinSankaranarayanan,SrinivasaG.NarasimhanandIoannisGkioulekas.',
        'ReinforcedCrossModalMatchingandSelfSupervisedImitationLearningforVisionLanguageNavigationbyXinWang,QiuyuanHuang,AsliCelikyilmaz,JianfengGao,DinghanShen,YuanFangWang,WilliamYangWangandLeiZhang.',
        'AStyleBasedGeneratorArchitectureforGenerativeAdversarialNetworks',
        'NeuralRejuvenation:ImprovingDeepNetworkTrainingbyEnhancingComputationalResourceUtilization',
        'LearningLossforActiveLearning',
        'BADSLAM:BundleAdjustedDirectRGBDSLAM',
    'Deep Reinforcement Learning of Volume-Guided Progressive View Inpainting for 3D Point Scene Completion From a Single Depth Image',
    'Long-Term Feature Banks for Detailed Video Understanding',
    'Which Way Are You Going? Imitative Decision Learning for Path Forecasting in Dynamic Scenes',
    'MHP-VOS: Multiple Hypotheses Propagation for Video Object Segmentation',
    'Language-Driven Temporal Activity Localization: A Semantic Matching Reinforcement Learning Model',
    'Neural Rejuvenation: Improving Deep Network Training by Enhancing Computational Resource Utilization',
    'Structured Binary Neural Networks for Accurate Image Classification and Semantic Segmentation',
    'Spherical Fractal Convolutional Neural Networks for Point Cloud Recognition',
    'Scene Memory Transformer for Embodied Agents in Long-Horizon Tasks',
    'Generalized Intersection Over Union: A Metric and a Loss for Bounding Box Regression',
    '任务是指在真实的三维环境中让具有实体的智能体进行导航并完成自然语言指令。',
    '在这篇论文中，作者们研究了如何解决这个任务中的三个重点挑战',
    '跨模态参照，糟糕的反馈，以及泛化问题。作者们首先提出了一种新的强化跨模态匹配（RCM）方法，',
    '它可以通过强化学习的方式同时促进局部和全局的跨模态参照。',
           ]
domains = ['http://10.0.251.119:9090/enorth-chat/chatContent',
            # 'http://10.20.31.89/enorth-chat/r/api/chatContent/sendChatContent',
            # 'http://10.20.31.90/enorth-chat/r/api/chatContent/sendChatContent',
            ]
# domains = ['http://10.20.31.89/enorth-chat/r/api/chatContent/sendChatContent',
#             ]

# news_ids = ['035683650']
news_ids = ['035683687']


api_tokens = ['v~0d68e3e4-8fd6-4135-ad6d-3971207b1578~200529~-000000303740416~200529102901~0bb7408350a849c8fe771477ef2f047c',
            'v~04ea875dfa1a4e8c8d1302dbdc8a61af~200528~-000002020290411~200528163009~cb18f1ee591e7679bd4b14a1530e9905',
              'v~05bbf2f1-4910-4774-8f24-2bb9605b08e5~200529~-000000306302468~200529102902~656c5f5ccdfa12e7e0a713ae072233cf',
              'v~a2192019-7d79-42d3-85a1-1d2583629789~200529~-000001550114340~200529102838~c6ab07e8451a050dc8442541223a5a6e',
              'v~8eb7c1e6-ac80-453c-9c98-abd55f5ed0ea~200529~-000001046716598~200529102811~db539aeb60f2318aba7244199a1d0cca',
              'v~55f0a228-8ccb-4737-b932-ba09c41be8db~200529~-000001361086873~200529102704~4305f863c9733f27d8e5ceebf75c9450',
              'v~b9c02fd5-fcc2-4c67-9050-e4bd800f83d9~200415~-000000306139092~200529102902~925939aa086c8ed8e4db84be1156b731',
              'v~56742cbc-8baf-4acb-8043-08c596409086~200529~-000000307038897~200529102857~4a832c96442534c3889fb7851ca262ba',
              'v~2794c31d-9173-468b-8478-4600274dcd0d~200529~-000001705045467~200529102903~3f903b818944e48aed32d71bab4dc48c',
              'v~4b119bf0-ea56-4915-a95e-b7f18f17a4de~200525~-000000307994967~200529102904~f3731a709b1fd1d6f679581a353818c5',
        ]

def doGet(i):
    api_token = random.sample(api_tokens, 1)[0]
    content = random.sample(contents, 1)[0]
    news_id = random.sample(news_ids, 1)[0]
    check_sum = api_token + content + news_id + seed
    # print("check_sum___:", check_sum)
    check_sum = hashlib.md5(bytes(check_sum, encoding='utf-8')).hexdigest()
    # print('api_token:',api_token)
    # print('content:',content)
    # print('news_id:',news_id)
    # print('check_sum:',check_sum)
    # check_sum = hashlib.sha256(bytes(check_sum, encoding='utf-8')).hexdigest()
    url = random.sample(domains, 1)[0] + "?api_token=" + api_token + "&check_sum=" + check_sum \
          + '&content=' + urllib.parse.quote(content) + "&newsId=" + news_id
    # print(url)
    response = urllib.request.urlopen(url)
    # print('t:', time.time() - t)

i = 0
while True:
    for j in range(20):
        thread.start_new_thread(doGet, (i,))
        i += 1
    if i % 100 == 0:
        print(i)
        print('t:', time.time() - t)
    # if i >= total:
    #     break
    time.sleep(1)
print(time.time() - t)
time.sleep(2020)
print(time.time() - t)