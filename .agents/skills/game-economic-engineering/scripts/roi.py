
def calculate_roi(investment, total_returns):
    if investment <= 0:
        raise ValueError("O investimento deve ser maior que zero.")

    roi = ((total_returns - investment) / investment) * 100
    return roi


if __name__ == "__main__":
    investimento = 10800.00
    retorno = 14700.00

    resultado = calculate_roi(investimento, retorno)

    print("========== RETORNO SOBRE INVESTIMENTO ==========")
    print(f"Investimento: R$ {investimento:.2f}")
    print(f"Retorno líquido disponível: R$ {retorno:.2f}")
    print(f"ROI: {resultado:.2f}%")
