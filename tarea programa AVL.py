class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

def altura(nodo):
    if not nodo:
        return 0
    return nodo.altura

def get_balance(nodo):
    if not nodo:
        return 0
    return altura(nodo.izq) - altura(nodo.der)

def rotar_derecha(y):
    x = y.izq
    T2 = x.der
    x.der = y
    y.izq = T2
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    return x

def rotar_izquierda(x):
    y = x.der
    T2 = y.izq
    y.izq = x
    x.der = T2
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    return y

def insertar(nodo, valor):
    if not nodo:
        return NodoAVL(valor)
    if valor < nodo.valor:
        nodo.izq = insertar(nodo.izq, valor)
    else:
        nodo.der = insertar(nodo.der, valor)

    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))
    balance = get_balance(nodo)

    # rotaciones
    if balance > 1 and valor < nodo.izq.valor:
        return rotar_derecha(nodo)
    if balance < -1 and valor > nodo.der.valor:
        return rotar_izquierda(nodo)
    if balance > 1 and valor > nodo.izq.valor:
        nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)
    if balance < -1 and valor < nodo.der.valor:
        nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)

    return nodo

def min_valor_nodo(nodo):
    actual = nodo
    while actual.izq:
        actual = actual.izq
    return actual

def eliminar(nodo, valor):
    if not nodo:
        return nodo
    if valor < nodo.valor:
        nodo.izq = eliminar(nodo.izq, valor)
    elif valor > nodo.valor:
        nodo.der = eliminar(nodo.der, valor)
    else:
        if not nodo.izq:
            return nodo.der
        elif not nodo.der:
            return nodo.izq
        temp = min_valor_nodo(nodo.der)
        nodo.valor = temp.valor
        nodo.der = eliminar(nodo.der, temp.valor)

    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))
    balance = get_balance(nodo)

    # rotaciones tras eliminacion
    if balance > 1 and get_balance(nodo.izq) >= 0:
        return rotar_derecha(nodo)
    if balance > 1 and get_balance(nodo.izq) < 0:
        nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)
    if balance < -1 and get_balance(nodo.der) <= 0:
        return rotar_izquierda(nodo)
    if balance < -1 and get_balance(nodo.der) > 0:
        nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)

    return nodo

def in_orden(nodo):
    if nodo:
        in_orden(nodo.izq)
        print(nodo.valor, end=' ')
        in_orden(nodo.der)

def imprimir_balances(nodo):
    if nodo:
        imprimir_balances(nodo.izq)
        print(f"Valor: {nodo.valor}, Balance: {get_balance(nodo)}")
        imprimir_balances(nodo.der)

# Prueba arbol AVL
raiz = None
valores = [10, 20, 30, 40, 50, 25]
print("Insertando valores:", valores)
for v in valores:
    raiz = insertar(raiz, v)

print("\n--- Después de inserciones ---")
in_orden(raiz)
print("\n\n balances de los nodos:")
imprimir_balances(raiz)

print("\n eliminando valor 30...")
raiz = eliminar(raiz, 30)

print("\n--- Despues de eliminar 30 ---")
in_orden(raiz)
print("\n\nBalances actualizados:")
imprimir_balances(raiz)
