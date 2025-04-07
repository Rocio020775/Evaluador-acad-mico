import streamlit as st
import pandas as pd
import os

st.title("📚 Evaluador Académico")

# Entradas del usuario
nombre = st.text_input("¿Cómo te llamas?")
edad = st.number_input("¿Cuántos años tienes?", min_value=1, max_value=100)
carrera = st.text_input("¿Qué carrera estudias?")
promedio = st.number_input("¿Cuál es tu promedio?", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Evaluar"):
    st.subheader(f"Hola {nombre} 👋")
    st.write(f"Tienes {edad} años y estudias {carrera}.")
    st.write(f"Tu promedio es: {promedio}")

    # Evaluación del promedio
    if promedio >= 9:
        st.success("🎉 ¡Excelente trabajo! Vas muy bien.")
    elif promedio >= 8:
        st.info("✅ Muy bien, sigue así.")
    elif promedio >= 6:
        st.warning("⚠️ Vas bien, pero podrías mejorar.")
    else:
        st.error("❌ Necesitas esforzarte más. ¡Tú puedes!")

    # Aprobación
    if promedio >= 6:
        st.success("📘 Resultado: Aprobada ✅")
    else:
        st.error("📕 Resultado: Reprobada ❌")

    # 👇 Guardar los datos en CSV
    archivo = "registros.csv"
    nuevo_dato = {
        "Nombre": nombre,
        "Edad": edad,
        "Carrera": carrera,
        "Promedio": promedio
    }

    if os.path.exists(archivo):
        df = pd.read_csv(archivo)
        df = pd.concat([df, pd.DataFrame([nuevo_dato])], ignore_index=True)
    else:
        df = pd.DataFrame([nuevo_dato])

    df.to_csv(archivo, index=False)
    st.success("📁 Los datos se han guardado correctamente.")


  
