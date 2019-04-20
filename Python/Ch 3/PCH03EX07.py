import time

fseconds = time.time()


print("현재시간 (영국 그리니치 시간) :", (fseconds % 60) / 60)
