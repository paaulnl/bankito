from main import Profile

def main():
    name = input("Ingrese su nombre:")
    rut = int(input("Ingrese su rut:"))
    mail = input("Ingrese su mail:")
    
    usuario = Profile(name,rut,mail)
    usuario.print()
    deposito = int(input("Si usted desea realizar un deposito ingrese 1, si no desea realizar deposito ingrese 2"))
    if (deposito == 1):
        ammount = int(input("Ingrese la cantidad a depositar"))
        usuario.deposit(ammount)
        usuario.print()
        
    elif(deposito == 2):
        print("Gracias por su preferencia! :)")
    else:
        print("El numero ingresado no corresponde")
        
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
    
    