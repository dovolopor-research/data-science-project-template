# Data Science Project Template

ð§  **å¼ç®±å³ç¨**çãæ°æ®ç§å­¦é¡¹ç®æ¨¡æ¿ã

> ç¥åç¼ä¸¹å¸æäºï¼**åççãé¡¹ç®ç»æãæ¯æåçèµ·ç¹ï¼**

## 1 ç®å½ç®ä»

```
.
âââ README.md          # ç®ä»
âââ app                # åºç¨
â   âââ test.py
â   âââ train.py
âââ notebook           # äº¤äºï¼å¯éï¼
âââ model              # æ¨¡åï¼å¯éï¼
âââ data               # æ°æ®
âââ util               # è¾å©
â   âââ conf.py
â   âââ log.py
â   âââ data_model.py
â   âââ db.py
â   âââ data.py
âââ save               # ä¿å­
âââ conf               # éç½®
â   âââ default.prod.yml
â   âââ default.test.yml
â   âââ default.yml
âââ script             # èæ¬
â   âââ init_env.sh    # åå»º Conda ç¯å¢
âââ server             # é¨ç½²ï¼å¯éï¼
â   âââ app.py
âââ test               # æµè¯ï¼å¯éï¼
â   âââ function_test.py
â   âââ api_test.py
âââ doc                # ææ¡£ï¼å¯éï¼
âââ log                # æ¥å¿
âââ Dockerfile         # Docker æåéç½®ï¼å¯éï¼
âââ .dockerignore      # Docker å¿½ç¥éç½®ï¼å¯éï¼
âââ .gitignore         # Git å¿½ç¥éç½®
âââ requirements.txt   # ä¾èµï¼å¯éï¼
âââ LICENSE            # è®¸å¯
```

### 1.1 README.mdï¼ææ¡£ï¼

**ä¸ä¸ªè¯¦å°½çææ¡£æ¯ä»ä¹é½éè¦ï¼** ä»»ä½äººé½å¯ä»¥éè¿ææ¡£å¿«éä¸æãä¹è®¸ä½ ä¼è¯´ï¼æçä»£ç å°±æèªå·±çï¼ä¸åææ¡£ä¹ç¥éãå¯æ¯ä½ è½ä¿è¯ä¸ä¸ªæä»¥åï¼ä½ è¿è®°å¾ä½ å½ååçä»ä¹åï¼ï¼

ä¸ä¸ªå¥½çæ·±åº¦å­¦ä¹ é¡¹ç®ææ¡£åºè¯¥æ¯ææ ·çï¼

1. ç¯å¢ä¾èµè¯´æ
2. å¿«éè¿è¡èæ¬
3. ç±»ä¼¼é¡¹ç®æ¯è¾
4. æ§è½æµè¯ç»æ
5. ç»è´çæ¬è®°å½
6. ç¸å³åèèµæ

åèï¼

1. [å¦ä½åå¥½Githubä¸­çreadmeï¼](https://www.zhihu.com/question/29100816)
2. [å¦ä½ä¸ºä½ çå¼æºé¡¹ç®ç¼åå®ç¨çææ¡£](https://zhuanlan.zhihu.com/p/120399648)

### 1.2 appï¼åºç¨å¥å£ï¼

è¿éæ¯æ ¸å¿åºç¨çå¥å£ï¼æ¯å¦è®­ç»æä»¶ `train.py` åæµè¯æä»¶ `test.py`ï¼å½ç¶ä¹å¯ä»¥æä¸äºä¸­é´è¿ç¨æ¾å¨æ­¤å¤ï¼æ¯å¦æåç¹å¾ `extract_feature.py` ç­ã

æ¨èä½¿ç¨ `python -m app.train` è¿æ ·çæ¹å¼è¿è¡ï¼ä»¥é¿ååºç° package çå¼ç¨é®é¢ã

### 1.3 notebookï¼äº¤äºç¼ç¨ï½å¯éï¼

`jupyter notebook` æ¯ä¸ä¸ªéæäº `ipython` çå¯è§åäº¤äºä»£ç å·¥å·ï¼å¯ä»¥æ¹ä¾¿çæ¥çä¸­é´åéåè®°å½æ³æ³ï¼ç¹å«éååæ°æ®å¤çåæ°æ®å¯è§åã

> ç¥åç¼ä¸¹å¸æäºï¼ç¼ä¸¹å¸çå·¥ä½ååââã80% æ¸çæ°æ®ï¼20% è°èåæ°ã

æ°æ®ç§å­¦ä¸¤åå¼ââ`numpy` å `pandas` æ¯ä¸å¯æç¼ºçï¼å¨ notebook ä¸­ä¼å¤§éä½¿ç¨å°ï½

å¯¹äºå¤§è§æ¨¡æ°æ®ï¼å»ºè®®åè¯»åé¨åæ°æ®ï¼å¨ notebook ä¸ç¼åæ°æ®å¤çç®¡éï¼æåæ½è±¡æå½æ°æ¾å° app ç®å½ä¸è¿è¡ã

### 1.4 modelï¼ç®æ³æ¨¡åï½å¯éï¼

è¿éä¸è¬æ¾ãç¥ç»ç½ç»ãæèæ¯æºå¨å­¦ä¹ çç®æ³ç»æã

æ¯å¦åå« `torch.nn.Module` çæä»¶ã

### 1.5 dataï¼æ°æ®ï¼

ææçæ°æ®çå æ¾å¤ï¼æå¸¸è§çå°±æ¯ãæ°æ®éãã

å¦ææ°æ®éæ¯è¾å¤§ï¼å»ºè®®å¨ä¸é¨çç£çä¸­è¿è¡å­å¨ç®¡çï¼éè¿è½¯é¾æ¥çæ¹å¼æ å°å° ./data ç®å½ä¸é¢ã

```shell
ln -s /path/to/dataset ./data/dataset
```

> â ï¸ æ³¨æï¼
> å é¤è½¯é¾æ¥æ¯ `rm -rf ./data/dataset`ï¼
> èä¸æ¯ `rm -rf ./data/dataset/`ï¼
> ç¬¬äºå½ä»¤åæ³ä¼ææºæ°æ®å æï¼åè®°ï¼åè®°ï¼

### 1.6 utilï¼è¾å©å·¥å·ï¼

ä¸äºå¸¸è§çè¾å©å½æ°ï¼æ¯å¦ï¼

1. conf éç½®
2. data æ°æ®
3. data_model æ°æ®æ¨¡å
4. log æ¥å¿
5. db æ°æ®åº

### 1.7 saveï¼ç»æä¿å­ï¼

æ¨¡ååæ°ãæ§è½æµè¯ç»æç­...

### 1.8 confï¼éç½®ä¸­å¿ï¼

ææçéç½®é½æ¯ç¨ `YAML`ï¼å®æ¯ `json` æ´å¥½ç¨ï¼å¯ä»¥å¨éç½®ä¸­æ·»å æ³¨éï¼å¹¶ä¸åç°æ¹å¼ä¹æ´ä¸ºç´è§ï¼

éç½®æä»¶çä¸­é´åç§°æ¯ãç¯å¢åéãï¼æ¯å¦ ENV ä¸º `test` æ¶ï¼å°±ä¼è¯»å `default.test.yml` æä»¶ï¼ENV é»è®¤ä¸º `dev`ï¼ä¼è¯»å `default.yml`ï¼ã

å¦ä½ä½¿ç¨ç¯å¢åé ENV å¢ï¼åªéè¦å¨æ§è¡æ¶ï¼æ `ENV=test` æ·»å å°å½ä»¤çæåé¢ã

```
ENV=test python -m app.train
```

### 1.9 scriptï¼å®ç¨èæ¬ï¼

å¯¹äºä¸äºå¸¸è§çè¿ç»­å½ä»¤ï¼æä»¬å¯ä»¥æå®æ´çåºæ¥ï¼åæä¸ä¸ªèæ¬ï¼ä»¥ä¾¿å¿«éæ§è¡ï¼

æ¯å¦ `init_env.sh` å¯ä»¥è®©ä½ å¿«éåå»º conda èæç¯å¢ï¼

```shell
bash scripts/init_env.sh
```

### 1.10 serverï¼é¨ç½²ï½å¯éï¼

ä½¿ç¨ Web æå¡é¨ç½²å°çº¿ä¸ç¯å¢ï¼æ¨èä½¿ç¨ [Sanic](https://sanic.dev/zh/)ã

```
ENV=prod python -m server.main
```

### 1.11 testï¼æµè¯ï½å¯éï¼

ä¸æ¨¡åçæµè¯ä¸åï¼è¿éä¸»è¦ä¸ºä»£ç çååæµè¯ `UnitTest`ã

`function_test.py` éé¢æ¼ç¤ºäºå¦ä½åä¸ä¸ªæç®åçååæµè¯ã

```shell
# æ¹æ³1ï¼ä½¿ç¨ python æ§è¡
python -m test.function_test
# æ¹æ³ï¼ä½¿ç¨ pytest æ§è¡ï¼pytest è½å¤èªå¨æ¾å°å½åæä»¶å¤¹çæææµè¯æä»¶
pytest
```

`api_test.py` æ¯å¯¹ API æ¥å£è¿è¡ååæµè¯ï¼å¾å° QPSï¼æ¯ç§è¯·æ±æ°ï¼ã

`Locust` æ¯ä¸ä¸ªéå¸¸å¥½ç¨çæµè¯å·¥å·ï¼å®éå¸¦ä¸ä¸ª WEB çé¢ï¼éå¸¸æ¹ä¾¿å°å¨æµè§å¨ä¸­è¿è¡åæµã

```shell
locust -f test/api_test.py -u 10 -r 1
```

å¨æµè§å¨ä¸­æå¼ `http://127.0.0.1:8089`ï¼ç¹å» `Start swarming` æé®ï¼å°±å¯ä»¥å¼å§åæµäºï¼

åèï¼
1. [Python unittest: ååæµè¯æ¡æ¶](https://docs.python.org/zh-cn/3/library/unittest.html)
2. [Locust: An open source load testing tool.](https://locust.io)

### 1.12 docï¼ææ¡£ï½å¯éï¼

å¦æé¡¹ç®æ¯è¾å¤æï¼å¯ä»¥å°ææ¡£æ´çå½çº³å°è¿éã

### 1.13 logï¼æ¥å¿ï¼

`util/log.py` ä¼å°æ¥å¿æå¤©è®°å½å°è¿éã

### 1.14 requirements.txt ï¼ä¾èµï¼

é¡¹ç®æéè¦çä¾èµï¼æ¹ä¾¿ä¸é®å®è£ã

```shell
pip install -r requirements.txt
```

### 1.15 LICENSEï¼è®¸å¯ï½å¯éï¼

å¦ææ¯å¼æºé¡¹ç®ï¼éè¦æ·»å è®¸å¯è¯ã

åèï¼

1. [ä¸æçæå¼æºè®¸å¯è¯ä¸¨å¼æºç¥è¯ç§æ®](https://pingcap.com/zh/blog/introduction-of-open-source-license)
2. [å¦ä½éæ©å¼æºè®¸å¯è¯ï¼](https://www.ruanyifeng.com/blog/2011/05/how_to_choose_free_software_licenses.html)

## 2 ç¯å¢åå¤

- Ubuntu 18.04 LTS+
- Python 3.7+
- Anaconda 3

> äººçè¦ç­ï¼å¿«ç¨ `*NIX` ï¼

## 3 TODO

- [ ] dspt init èæ¬
- [ ] script ä¸­æ·»å ä¸äºå¸¸ç¨èæ¬

## 4 åè

- [Ubuntu ç³»ç»éåä¸è½½](https://cn.ubuntu.com/download)
- [Anaconda ä¸ªäººç](https://www.anaconda.com/products/individual#)
- [TUNA æ¸åå¤§å­¦å¼æºè½¯ä»¶éåç«](https://mirrors.tuna.tsinghua.edu.cn/)

## 5 è®¸å¯è¯

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
