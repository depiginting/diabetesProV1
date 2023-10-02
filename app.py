import pickle
import streamlit as st
import pandas as pd
import gspread #pip install gspread
# from openpyxl import load_workbook
from time import strftime
ct = strftime("%Y-%m-%d %H:%M:%S")
# wb_append = load_workbook("db.xlsx") 
# sheet = wb_append.active

data = (
    "nama","usia","gender","sering_kencing","sering_haus","bb_turun","lemas","sering_sariawan",
    "pandangan_kabur","gatal_kulit","cepat_marah","luka_lama_sembuh","otot_lemah","otot_kaku","rambut_rontok",
    "obesitas","metode","diabetes")
# sheet.append(data)
# wb_append.save('db.xlsx')


st.subheader("Prediksi Diabetes Algoritma kNN", divider="rainbow")
st.caption("Machine learning methode | Developer : Depi | Dataset : UCI Machine Learning Repository | Universitas Syiah Kuala 2023")
diabetes_model = pickle.load(open("knn.sav", "rb"))
dm = ""
# membagi kolom
# diabetes_model = st.radio(
#     "Akurasi Prediksi : Random Forest( 97% ) | Support Vector( 96% ) | kNN( 90% ) | Decision Tree( 90% )",
#     ["Random Forest", "Support Vector", "kNN", "Decision Tree"],
#     horizontal=True,
# )
# if diabetes_model == "kNN":
#     diabetes_model = pickle.load(open("knn.sav", "rb"))
#     dm = "kNN"
# elif diabetes_model == "Support Vector":
#     diabetes_model = pickle.load(open("svc.sav", "rb"))
#     dm = "support vector"
# elif diabetes_model == "Random Forest":
#     diabetes_model = pickle.load(open("rf.sav", "rb"))
#     dm = "random forest"
# else:
#     diabetes_model = pickle.load(open("decision.sav", "rb"))
#     dm = "decision tree"
# judul web
col1, col2, col3 = st.columns(3)
with col1:
    nama = st.text_input("Nama")
with col1:
    Age = st.number_input("Usia",value=20)
with col1:
    Gender = st.radio("Jenis Kelamin", ["Pria", "Wanita"],horizontal=True,)
    jk = ""
    if Gender == "Pria":
        Gender = 1
        jk = "laki-laki"
    else:
        Gender = 0
        jk = "perempuan"
with col1:
    Polyuria = st.toggle("Sering Kencing")
    pr = ""
    if Polyuria:
        Polyuria = 1
        pr = "ya"
    else:
        Polyuria = 0
        pr = "tidak"
with col1:
    Polydipsia = st.toggle("Sering Haus")
    if Polydipsia:
        pl = "ya"
        Polydipsia = 1
    else:
        Polydipsia = 0
        pl = "tidak"
with col2:
    sudden_weight_loss = st.toggle("Penurunan Berat Badan")
    if sudden_weight_loss:
        sudden_weight_loss = 1
        swl = "ya"
    else:
        sudden_weight_loss = 0
        swl = "tidak"
with col2:
    weakness = st.toggle("Tubuh Lemas")
    if weakness:
        weakness = 1
        ws = "ya"
    else:
        weakness = 0
        ws = "tidak"
with col2:
    Polyphagia = st.toggle("Sering Lapar")
    if Polyphagia:
        Polyphagia = 1
        pg = "ya"
    else:
        Polyphagia = 0
        pg = "tidak"
with col2:
    Genital_thrush = st.toggle("Sering Sariawan")
    if Genital_thrush:
        Genital_thrush = 1
        gt = "ya"
    else:
        Genital_thrush = 0
        gt = "tidak"
with col2:
    visual_blurring = st.toggle("Pandangan Sering Kabur")
    if visual_blurring:
        visual_blurring = 1
        vb = "ya"
    else:
        visual_blurring = 0
        vb = "tidak"
with col2:
    Itching = st.toggle("Gatal pada kulit")
    if Itching:
        Itching = 1
        ic = "ya"
    else:
        Itching = 0
        ic = "tidak"
with col2:
    Irritability = st.toggle("Cepat Marah")
    if Irritability:
        Irritability = 1
        ir = "ya"
    else:
        Irritability = 0
        ir = "tidak"
with col2:
    delayed_healing = st.toggle("Luka lama sembuh")
    if delayed_healing:
        delayed_healing = 1
        dh = "ya"
    else:
        delayed_healing = 0
        dh = "tidak"
with col3:
    partial_paresis = st.toggle("Otot lemah")
    if partial_paresis:
        partial_paresis = 1
        pp = "ya"
    else:
        partial_paresis = 0
        pp = "tidak"
with col3:
    muscle_stiffness = st.toggle("Otot kaku")
    if muscle_stiffness:
        muscle_stiffness = 1
        ms = "ya"
    else:
        muscle_stiffness = 0
        ms = "tidak"
with col3:
    Alopecia = st.toggle("Rambut Rontok")
    if Alopecia:
        Alopecia = 1
        al = "ya"
    else:
        Alopecia = 0
        al = "tidak"
with col3:
    Obesity = st.toggle("Kegemukan")
    if Obesity:
        Obesity = 1
        ob = "ya"
    else:
        Obesity = 0
        ob = "tidak"

# kode prediksi


# membuat tombol prediksi
with col3:
    diab_diagnosis = ""
    if st.button("Test Prediksi Diabetes"):
        diab_prediction = diabetes_model.predict(
            [
                [
                    ## Age,
                    ## Gender,
                    Polyuria,
                    Polydipsia,
                    sudden_weight_loss,
                    weakness,
                    Polyphagia,
                    Genital_thrush,
                    visual_blurring,
                    Itching,
                    Irritability,
                    delayed_healing,
                    partial_paresis,
                    muscle_stiffness,
                    Alopecia,
                    Obesity,
                ]
            ]
        )
        dbt = ""
        if diab_prediction[0] == 1:
            diab_diagnosis = st.warning("Peringatan ! Pasien Positif Diabetes, Segera hubungi dokter")
            dbt = "positif"
            dbtx = 1
        else:
            diab_diagnosis = st.success("Pasien Negatif Diabetes, tetap jaga kesehatan")
            dbt = "negatif"
            dbtx = 0
        newdata =(ct,nama,int(Age),jk,dm,dbt,pr,pl,swl,ws,gt,vb,ic,ir,dh,pp,ms,al,ob)
        newdatax =(ct,nama,int(Age),jk,dm,dbtx,Polyuria,Polydipsia,sudden_weight_loss,weakness,Genital_thrush,visual_blurring,Itching,Irritability,delayed_healing,partial_paresis,muscle_stiffness,Alopecia,Obesity)
       # for row in newdata:
       ########## Kirim data ke GoogleSheet ##############
        # sheet.append(newdata)
        cred_file = "keys.json"
        # cred_filex = "keys.json"
        gc = gspread.service_account(cred_file)
        # gcx = gspread.service_account(cred_filex)
        database = gc.open("biabet_db")
        # databasex = gcx.open("biabet_db")
        wks = database.worksheet("sample")
        wksx = database.worksheet("numeric")
        # list_wksx = databasex.worksheets()
        list_wks = database.worksheets()
        wks.append_row(newdata, table_range="A1:Z1") 
        wksx.append_row(newdatax, table_range="A1:Z1") 

        # wks.append_row(data, table_range="A1:Z1") 
        ############ Selesai ########################
        # wb_append.save('db.xlsx')
 
#Saving the data in our sample workbook/sheet


        
