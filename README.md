# EEG_RISK
EEFRISK_REVISED
以下為實驗參數調整
## 回合數調整
打開settings.py 修改roundnumfixed的參數 
該參數為回合數
目前最大值是63 若要修改可以從main game 的 NUM_ROUNDS修改 
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
並顯示報酬是0(後台的數字會是-1作為分辨)
答對則會進入練習環節與正式環節
設定答案在該app的init.py
目前所有的預設答案五題都是c
若要修改答案則去改quiz中before_next_page下面之if參數
對應到想要的選項
