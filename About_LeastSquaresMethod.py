import numpy as np
from scipy.optimize import curve_fit

# 1. 모델 함수 정의
def spot_rate_model(x, a, b, c, d):
    return (a + b*x) * np.exp(-c*x) + d

# 2. 시장에서 관측한 실제 데이터 (예시)
x_data = np.array([1, 2, 5, 10]) # 만기
y_data = np.array([0.05, 0.058, 0.073, 0.087]) # 실제 관측된 Spot Rate

# 3. 최소제곱법으로 모수(a, b, c, d) 찾기
params, _ = curve_fit(spot_rate_model, x_data, y_data)
a_opt, b_opt, c_opt, d_opt = params

print(f"찾아낸 모수: a={a_opt}, b={b_opt}, c={c_opt}, d={d_opt}")

# 예: 1년차부터 5년차까지의 추정된 Spot Rate 출력
years = [1, 2, 3, 4, 5]

print("\n[추정된 모델 기반 Spot Rate 출력]")
for t in years:
    # 추정된 모수(a_opt, b_opt, c_opt, d_opt)를 함수에 대입
    estimated_rate = spot_rate_model(t, a_opt, b_opt, c_opt, d_opt)
    
    # 이자율 형식으로 출력 (소수점 4자리까지)
    print(f"{t}년차 추정 Spot Rate: {estimated_rate:.4f} ({estimated_rate*100:.2f}%)")