import math

def log_probability():
    p = 0.5
    n = 10000
    
    # 使用對數性質計算：log10(p^n) = n * log10(p)
    # 我們這裡使用以 10 為底的對數，方便直觀理解位數
    log10_prob = n * math.log10(p)
    
    print("--- 第二題：對數運算 ---")
    print(f"計算公式: log10({p}^{n}) = {n} * log10({p})")
    print(f"log10 的結果: {log10_prob:.4f}")
    
    # 還原成科學記號表示
    # 10^-3010.2999 = 10^0.7001 * 10^-3011
    mantissa = 10**(log10_prob - math.floor(log10_prob))
    exponent = math.floor(log10_prob)
    
    print(f"還原科學記號: {mantissa:.4f} * 10^{exponent}")

if __name__ == "__main__":
    log_probability()
