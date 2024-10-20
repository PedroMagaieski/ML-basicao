from sklearn import tree

lisa = 1
irregular = 0
maça = 1
laranja = 0

pomar = [[150, lisa],[130, lisa],[180, irregular],[160, irregular]]

resultado = [maça, maça, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = input("Entre com o peso: ")
superficie = input("Entre com a superficie(1 para lisa e 0 irregular): ")

resultadoUsuario = clf.predict([[peso, superficie]])

if resultadoUsuario == 1:
    print("é uma maça")
else:
    print("é uma laranja")
