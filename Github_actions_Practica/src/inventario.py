"""Reglas de negocio de StockGuard: control de inventario de supermercados."""


def clasificar_stock(stock_actual: int, stock_minimo: int) -> str:
    """Clasifica el riesgo de inventario de un producto.

    Reglas (se evaluan en este orden):
    - stock_actual == 0                     -> AGOTADO
    - stock_actual <= 50 % del stock_minimo -> CRITICO
    - stock_actual <= stock_minimo          -> BAJO
    - cualquier otro caso                   -> NORMAL
    Valores negativos o stock_minimo <= 0 son invalidos.
    """
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if stock_minimo <= 0:
        raise ValueError("El stock minimo debe ser mayor que cero")
    if stock_actual == 0:
        return "AGOTADO"
    if stock_actual <= stock_minimo * 0.5:
        return "CRITICO"
    if stock_actual <= stock_minimo:
        return "BAJO"
    return "NORMAL"
