def darcy_rate(K, A, dP, U, L):
    cf = 0.001127
    q = (cf * K * A * dP) / (U * L)
    return round(q, 2)
