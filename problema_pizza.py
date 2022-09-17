class Pizza:
    subprecio = 0
    precio = 0

    def __init__(self, tamanio, ingredientes, num):
        self.tamanio = tamanio
        self.ingredientes = ingredientes
        self.num = num
        self.subprecio = Pizza.subprecio
        self.precio = Pizza.precio

    def agregar_ingredientes(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def tamanio_pizza(self):
        if self.tamanio == 1:
            print('tamaño grande \n')
            self.subprecio = 100
        elif self.tamanio == 2:
            print('tamano mediano \n')
            self.subprecio = 75
        elif self.tamanio == 3:
            print('tamaño chica \n')
            self.subprecio = 50

    def orden(self):
        self.precio = (self.precio + self.subprecio)*self.num
        print(f'los ingrdientes de la pizza son: {self.ingredientes} \n')
        print(f'el precio de la  pizza es {self.subprecio} \n')
        print(f'el precio total de las pizzas es {self.precio} \n')


if __name__ == '__main__':

    tama = int(input('de que tamanio va a ser su pizza?\n 1.- grande\n 2.- mediana\n 3.- chica: '))
    numero = int(input('cuantas pizzas desea: '))
    todos_los_ingredientes = ('peperoni','anchoas','queso','champiniones','salsa extra')
    pizza1 = Pizza(tama, todos_los_ingredientes, numero)
    pizza1.tamanio_pizza()
    pizza1.orden()
