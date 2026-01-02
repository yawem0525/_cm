def direct_probability():
    p = 0.5
    n = 10000
    
    # 直接進行次方運算
    prob = p ** n
    
    print("--- 第一題：直接計算 ---")
    print(f"計算公式: {p}^{n}")
    print(f"計算結果: {prob}")
    
    if prob == 0:
        print("說明：結果為 0 是因為數值太小，超出了電腦雙精度浮點數的處理極限 (約 10^-308)。")

if __name__ == "__main__":
    direct_probability()
