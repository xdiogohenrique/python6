def calculaIMC(peso,alt):
    
    imc = peso/(alt*alt)
    
    print("O valor seu IMC é: %.2f"% imc)
        
    
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc <= 24.9:
        print("Peso ideal (Parabéns)")
    elif imc <= 29.9:
        print("Levemente acima do peso")
    elif imc <= 34.9:
        print("Obesidade grau I") 
    elif imc <= 39.9:
        print("Obesidade grau II (Severa)") 
    else:
        print("Obesidade III (Morbida)")

alt = float(input("Insira o valor da sua altura: "))
peso = float (input("Insira o valor do seu peso: "))

imc = calculaIMC(peso,alt)
    
