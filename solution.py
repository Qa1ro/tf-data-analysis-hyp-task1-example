import pandas as pd
import numpy as np


chat_id = 736941004 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
  control_proportion = x_success / x_cnt
  test_proportion = y_success / y_cnt
  p_pool = (x_success + y_success) / (x_cnt + y_cnt)
  z_score = (test_proportion - control_proportion) / ((p_pool * (1 - p_pool) * (1/x_cnt + 1/y_cnt))**(0.5))
  if z_score > 1.96 or z_score < -1.96:
      return 1
  else:
      return 0
