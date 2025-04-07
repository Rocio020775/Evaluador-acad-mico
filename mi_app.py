import streamlit as st
import pandas as pd
import os

st.title("📚 Evaluador Académico")

# FORMULARIO
nombre = st.text_input("¿Cómo te llamas?")
edad = st.number_input("¿Cuántos años tienes?", min_value=1, max_value=100)
carrera = st.text_input("¿Qué carrera estudias?")
promedio = st.number_input("¿Cuál es tu promedio?", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Evaluar"):
    st.subheader(f"Hola {nombre} 👋")
    st.write(f"Tienes {edad} años y estudias {carrera}.")
    st.write(f"Tu promedio es: {promedio}")

    # EVALUACIÓN
    if promedio >= 9:
        st.success("🎉 ¡Excelente trabajo! Vas muy bien.")
    elif promedio >= 8:
        st.info("✅ Muy bien, sigue así.")
    elif promedio >= 6:
        st.warning("⚠️ Vas bien, pero podrías mejorar.")
    else:
        st.error("❌ Necesitas esforzarte más. ¡Tú puedes!")

    # GUARDAR RESPUESTA EN CSV
    datos = pd.DataFrame({
        'Nombre': [nombre],
        'Edad': [edad],
        'Carrera': [carrera],
        'Promedio': [promedio]
    })

    archivo = "respuestas.csv"
    if os.path.exists(archivo):
        datos.to_csv(archivo, mode='a', header=False, index=False)
    else:
        datos.to_csv(archivo, index=False)

    st.success("✅ ¡Tus datos se guardaron en respuestas.csv!")

# 📋 MOSTRAR DATOS GUARDADOS
st.subheader("📊 Historial de respuestas:")
if os.path.exists("respuestas.csv"):
    df = pd.read_csv("respuestas.csv")
    st.dataframe(df)
else:
    st.info("Aún no hay respuestas registradas.")



  
