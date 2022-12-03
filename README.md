# EEG_RISK
EEFRISK_REVISED
以下為實驗參數調整
## 回合數調整
打開settings.py 修改roundnumfixed的參數 為回合數 
本處會連動guide中的回合數
## 第一頁的空白
已經留白第一頁
可以接上所需要的簡介語
## 移除 next 按鍵
將guide中的案件移除
## 增加題目
選項可以於html內修改 目前預設是五題 回答後會回傳到後端
需要每一題都回答才可以進入下一階段
若是答錯任何一題，下一頁結束後將會直接跳到payoff_info頁面
答對才會進入練習環節與正式環節
設定答案在該app的init.py
目前所有的預設答案五題都是c
