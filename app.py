import streamlit as st

st.title("🚌 Fechamento de Caixa em")

# --- SEÇÃO 1: RELATÓRIOS E VALES ---
st.header("Relatórios e Vales")
col1, col2 = st.columns(2)

with col1:
    relatorios_texto = st.text_area("Valores dos Relatórios (um por linha)", value="0.0")
    # Transforma o texto em lista de números
    valores = [float(x) for x in relatorios_texto.split() if x.strip()]
    total_r = sum(valores)
    st.metric("Total Relatórios", f"R$ {total_r:.2f}")

with col2:
    vales_texto = st.text_area("Vales (um por linha)", value="0.0")
    vales = [float(x) for x in vales_texto.split() if x.strip()]
    total_v = sum(vales)
    st.metric("Total Vales ", f"R$ {total_v:.2f}")

# Cálculo do Total Líquido (Linha 5)
total_caixa_esperado = total_r - total_v
st.subheader(f"Total Esperado no Caixa: R$ {total_caixa_esperado:.2f}")

st.divider()

# --- SEÇÃO 2: CONTAGEM DE NOTAS ---
st.header("Contagem de Notas ")
notas = [100, 50, 20, 10, 5, 2]
total_notas_fisicas = 0.0

# Criando colunas para as notas ficarem organizadas
cols_notas = st.columns(3)
for i, nota in enumerate(notas):
    with cols_notas[i % 3]:
        qtd = st.number_input(f"Notas de R$ {nota}", min_value=0, step=1, key=f"nota_{nota}")
        subtotal_nota = nota * qtd
        total_notas_fisicas += subtotal_nota
        st.caption(f"Subtotal: R$ {subtotal_nota:.2f}")

# --- SEÇÃO 3: RESULTADO FINAL ---
st.divider()
diferenca = total_notas_fisicas - total_caixa_esperado

c1, c2 = st.columns(2)
c1.metric("Total em Notas ", f"R$ {total_notas_fisicas:.2f}")
c2.metric("Diferença ", f"R$ {diferenca:.2f}", delta=diferenca)

if diferenca == 0:
    st.success("O caixa bateu perfeitamente!")
elif diferenca > 0:
    st.warning(f"Sobra de R$ {diferenca:.2f}")
else:
    st.error(f"Falta de R$ {abs(diferenca):.2f}")
