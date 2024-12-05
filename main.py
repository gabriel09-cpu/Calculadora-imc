import streamlit as st 

with st.sidebar:
    
    st.write("""
    - **Abaixo do peso**: IMC menor que 18.5
    - **Peso ideal**: IMC entre 18.5 e 24.9
    - **Sobrepeso**: IMC entre 25 e 29.9
    - **Obesidade**: IMC entre 30 e 39.9
    - **Obesidade mórbida**: IMC acima de 40          
    """)
st.title("Calculadora IMC")

#Entrada de Dados = peso
peso = st.number_input(label="Informe seu peso", min_value=0.0, step=0.10, format="%.1f")
altura = st.number_input(label="Informe a sua altura (em metros)", min_value=0.0, step=0.10, format="%.2f")

if st.button("Calcular"):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        imc_ideal = 21.7
        imc_delta = imc - imc_ideal
        
        if imc < 18.5:
            classe = "Abaixo do Peso"
        elif imc < 24.9:
            classe = "Peso ideal"
        elif imc < 29:
             classe = "Sobrepeso"
        elif imc < 39.9:
            classe = "Obesidade"
        else:
            classe = "Obesidade mórbida"
        st.success("Cálculo ralizado com sucesso")
        #Escrever os valores
        st.write(f"Seu IMC é: {imc:.2f}")
        st.write(f"Classificação: {classe}")
        st.write(f"Comparação co IMC ideal (21.7): **{imc_delta:.2f}**")
        
#criar linha
        st.image("./imc.webp")
    else:
        #Mostrar mensagem
        st.error("Por favor, insira os valores pedidos")
        