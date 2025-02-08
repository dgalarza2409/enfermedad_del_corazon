import streamlit as st
import pandas as pd
import numpy as np 
import pickle

st.set_page_config(page_title="Prediccion",
                   page_icon="💓")

st.markdown("<h1 style='text-align: center;'>Diagnóstico 💓</h1>", unsafe_allow_html=True)


#with open('modelo_entrenado.pkl','rb') as f:
#    modelo = pickle.load(f)

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  font-weight: 200;
  color: blue;
}

div[class*="stNumberInput"] label {
  color: blue;
}
div[class*="stRadio"] label {
  color: blue;
}

</style>
"""


st.write(tabs_font_css, unsafe_allow_html=True)

col1, col2, col3= st.columns([0.6, 0.1, 0.3]) 


with open('modelo_entrenado.pkl', 'rb') as f:
     svm = pickle.load(f)
    

def get_user_input():

    with col1:
        st.markdown("<h3 style='text-align: center;'>Ingreso de características</h3>", unsafe_allow_html=True)
       # genre = st.radio("Sexo", ["Masculino", "***Femenino***"])
        edad = st.number_input('Edad', 15,100,30 )
        sexo = st.radio ('Sexo', ['Masculino','Femenino'], horizontal=True)
        cp = st.radio('CP: Dolor del pecho', ['Angina típica', 'Angina atípica','Espasmos esofágicos','Asintomático'], horizontal=True) 
        tresbps = st.number_input('TRESBPS: Presión arterial en reposo en mm Hg', 50, 200,80) 
        chol = st.number_input('CHOL: Colesterol sérico en mg/dl', 50,800,100)
        fbs = st.selectbox ('FBS:fasting blood sugar (azúcar en sangre en ayunas) > 120 mg/dl', ['Mayor a 120 mg/dl', 'Menor a 120 mg/dl']) 
        restecg =st.radio('RESTECG: Resultados electrocardiográficos en reposo', ['Nada que destacar','Anormalidad de la onda ST-T','Posible o definitiva hipertrofia ventricular izquierda'])
        thalach= st.number_input('THALACH: Frecuencia cardíaca máxima alcanzada', 50, 200, 100) 
        oldpeak = st.number_input('OLDPEAK: La depresión del segmento ST inducida por el ejercicio', 0,5,1)
        exang = st.radio('EXANG: Angina inducida por ejercicio',['SI','NO'], horizontal=True)  
        slope = st.radio('SLOPE: La pendiente del segmento ST del ejercicio máximo', ['Upsloping -Pendiente ascendente','Flatsloping - Pendiente plana','Downslopins- Pendiente descendente'])
        ca = st.radio('CA: Número de vasos principales (0-3) coloreados por fluorosopía', ["0","1","2","3"] , horizontal=True) 
        thal = st.selectbox('THAL:  Un desorden de sangre llamado thalassemia', ['Flujo sanguineo normal','No hay flujo en algna parte del corazon','Se observa un flujo sanguíneo pero no es normal'] )    

       
        datos={
            'age' : edad,
            'sex' : sexo,
            'cp' : cp,
            'tresbps' : tresbps,
            'chol' : chol,
            'fbs' : fbs,
            'restecg' : restecg,
            'thalach' : thalach,
            'oldpeak' : oldpeak,
            'exang' : exang,
            'slope' : slope,
            'ca' : ca,
            'thal' : thal 
        }

      

        return datos

datos = get_user_input()
datos_copia = datos.copy()

if datos["sex"]== "Femenino":
    datos["sex_0"]= 1
    datos["sex_1"] = 0
elif datos["sex"] == "Masculino": 
    datos["sex_0"] = 0
    datos["sex_1"] = 1
datos.pop("sex")


if datos["cp"] == "Angina típica":
    datos["cp_0"]=1
    datos["cp_1"]=0 
    datos["cp_2"]=0 
    datos["cp_3"]=0
elif datos["cp"] == "Angina atípica":
    datos["cp_0"]=0
    datos["cp_1"]=1
    datos["cp_2"]=0
    datos["cp_3"]=0
elif  datos["cp"] == "Espasmos esofágicos":
    datos["cp_0"]=0
    datos["cp_1"]=0
    datos["cp_2"]=1
    datos["cp_3"]=0
elif  datos["cp"] == "Asintomático":
     datos["cp_0"]=0
     datos["cp_1"]=0
     datos["cp_2"]=0
     datos["cp_3"]=1
datos.pop("cp")

if datos["fbs"]== "Mayor a 120 mg/dl":
    datos["fbs_0"] = 1
    datos["fbs_1"] = 0
elif datos["fbs"] == "Menor a 120 mg/dl":
    datos["fbs"] = 0
    datos["fbs_1"] = 1
datos.pop("fbs")

if datos["restecg"] == "Nada que destacar":
    datos["restecg_0"]=1
    datos["restecg_1"]=0
    datos["restecg_2"]=0
elif datos["restecg"] == "Anormalidad de la onda ST-T":
    datos["restecg_0"]=0
    datos["restecg_1"]=1
    datos["restecg_2"]=0
elif  datos["restecg"] == "Posible o definitiva hipertrofia ventricular izquierda":
    datos["restecg_0"]=0
    datos["restecg_1"]=0
    datos["restecg_2"]=1
datos.pop("restecg")

if datos["exang"]== "SI":
    datos["exang_0"] = 1
    datos["exang_1"] = 0
elif datos["exang"] == "NO":
    datos["exang_0"] = 0
    datos["exang_1"] = 1
datos.pop("exang")


if datos["slope"] == "Upsloping -Pendiente ascendente":
    datos["slope_0"]=1
    datos["slope_1"]=0
    datos["slope_2"]=0
elif datos["slope"] == "Flatsloping - Pendiente plana":
    datos["slope_0"]=0
    datos["slope_1"]=1
    datos["slope_2"]=0
elif  datos["slope"] == "Downslopins- Pendiente descendente":
    datos["slope_0"]=0
    datos["slope_1"]=0
    datos["slope_2"]=1
datos.pop("slope")

if datos["ca"] == "0":
    datos["ca_0"]=1
    datos["ca_1"]=0
    datos["ca_2"]=0
    datos["ca_3"]=0
elif datos["ca"] == "1":
    datos["ca_0"]=0
    datos["ca_1"]=1
    datos["ca_2"]=0
    datos["ca_3"]=0
elif  datos["ca"] == "2":
    datos["ca_0"]=0
    datos["ca_1"]=0
    datos["ca_2"]=1
    datos["ca_3"]=0
elif  datos["ca"] == "3":
    datos["ca_0"]=0
    datos["ca_1"]=0
    datos["ca_2"]=0
    datos["ca_3"]=1
datos.pop("ca")

if datos["thal"] == "Flujo sanguineo normal":
    datos["thal_1"]=1
    datos["thal_2"]=0
    datos["thal_3"]=0
elif datos["thal"] == "No hay flujo en algna parte del corazon":
    datos["thal_1"]=0
    datos["thal_2"]=1
    datos["thal_3"]=0
elif  datos["thal"] == "Se observa un flujo sanguíneo pero no es normal":
    datos["thal_1"]=0
    datos["thal_2"]=0
    datos["thal_3"]=1
datos.pop("thal")



st.sidebar.markdown("<h2 style='text-align: center;'>Diccionario de datos</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: center;'>(Guía abreviada)</h3>", unsafe_allow_html=True)
st.sidebar.markdown("""
  * cp - dolor de pecho
    * tipo de dolor del pecho
      * Typical angina: Dolor en el pecho relacionado con la disminución del suministro de sangre al corazón.
      * Atypical angina: Dolor del pecho no relacionado con el corazón.
      * Non-anginal pain: Espasmos esofágicos (no relacionados con el corazón)
      * Asymptomatic: Dolor del pecho que no muestra signos de enfermedad.
  * trestbps - presión arterial en reposo (en mm Hg a la admisión en hospital) cualquier valor sobre 130-140 suele ser motivo de preocupación.
  * chol - colesterol sérico en mg/dl
    * serum = LDL + HDL + .2 * trigliceridos
    * sobre 200 es motivo de preocupación.
  * fbs - (fasting blood sugar (azúcar en sangre en ayunas) > 120 mg/dl)
    * mayor que 120 mg/dL presume diabetes.
  * restecg - resultados electrocardiográficos en reposo
    * Anormalidad de la onda ST-T
      * Puede variar desde síntomas leves hasta problemas graves.
      * Señala latidos cardíacos anormales
    * Posible o definitiva hipertrofia ventricular izquierda.
      * Cámara de bombeo principal del corazón agrandada.
  * thalach - frecuencia cardíaca máxima alcanzada
  * exang - angina inducida por ejercicio 
  * oldpeak - La depresión del segmento ST inducida por el ejercicio en relación con el reposo analiza el estrés del corazón durante el ejercicio. Un corazón no saludable se estresará más.
  * slope - La pendiente del segmento ST del ejercicio máximo.
    * Upsloping -Pendiente ascendente: mejor frecuencia cardíaca con el ejercicio (poco común)
    * Flatsloping - Pendiente plana: cambio mínimo (corazón sano)
    * Downslopins- Pendiente descendente: signos de un corazón enfermo
  * ca - Número de vasos principales (0-3) coloreados por fluorosopía
    * El vaso coloreado significa que el médico puede ver la sangre que pasa a través de él. Cuanto más sangre se mueva, mejor (sin coágulos)
  * thal: A blood disorder called thalassemia
    * Valor 1: flujo sanguíneo normal
    * Valor 2: defecto fijo (no hay flujo sanguíneo en alguna parte del corazón)
    * Valor 3: defecto reversible (se observa un flujo sanguíneo pero no es normal)
""")


with col3:
    st.markdown("<h3 style='text-align: center'>Predicción</h3>", unsafe_allow_html=True)
    


    def prepare_input(data, feature_list):
        input_data = {feature: data.get(feature, 0) for feature in feature_list}
        input_df = pd.DataFrame(input_data, index=[0])
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        columnas_a_escalar = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
        input_df[columnas_a_escalar] = sc.fit_transform(input_df[columnas_a_escalar])       
        return input_df
    
    features = [
        'age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'sex_0',
       'sex_1', 'cp_0', 'cp_1', 'cp_2', 'cp_3', 'fbs_0', 'fbs_1', 'restecg_0',
       'restecg_1', 'restecg_2', 'exang_0', 'exang_1', 'slope_0', 'slope_1',
       'slope_2', 'ca_0', 'ca_1', 'ca_2', 'ca_3', 'ca_4', 'thal_1', 'thal_2',
       'thal_3'
    ]

     # Predict button
    if st.button("Click para predecir", icon="🚀" ,type='primary'):
        df = prepare_input(datos, features)
        prediction = svm.predict(df)
        st.subheader("Diagnostico sugerido")
        if prediction[0] == 1:
            st.write("Por favor consulte a un doctor. Ud. tiene alta probabilidad de tener una enfermedad del corazon")
        elif prediction[0] == 0:
            st.write("Felicidades. Pese a los síntomas hay alta posibilidad de que Ud. NO tenga una enfermedad del corazón.")

      
