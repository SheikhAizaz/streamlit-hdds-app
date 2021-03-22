import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from PIL import Image
import streamlit.components.v1 as components
def main():
    st.title("Heart Disease Detection System")
    menu = ["Home","Login"]
    submenu = ["Diets","Hospitals","Predictions"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Home")
        page_bg_img = '''
        <style>
        body {
        background-image: url("https://cutewallpaper.org/21/white-texture-background-hd/White-Texture-HD-Backgrounds-5-transparent-OUT-OF-FOCUS-TV.png");
        background-size: cover;
        }
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.markdown('Please Must be **Login**. User Name **test**. Password **test**. ')
        image = Image.open('./image/image1.jpg')
        st.image(image, caption="Simple", use_column_width=True)
        components.html(
            """ 
        <script src="http://maps.google.com/maps/api/js?sensor=false"></script>
        <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.10.1.min.js"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>       
         
        <div class="jumbotron bg-dark">
        <h1 class="display-5 text-white">Hello, People!</h1>
        <p class="lead text-white">
        I've developed a web app for heart disease detection system using Machine Learning based on the Kaggle Datasets.
        </p>
        <p  class="text-white">
        Developed by <strong>Aizaz Rafiq</strong>,<strong>Mohammad Azhar</strong>,<strong>Mohammad Khubaib</strong>
        </p>
        <p class="lead">
        <a class="btn btn-info btn-lg" href="https://github.com/SheikhAizaz" target="_blank" role="button">View on GitHub</a>
        </p>
        <hr />
                <p class="lead text-white">
                  Heart disease is one of the biggest cause for morbidity and
                  mortality among the population of the world. Prediction of
                  cardiovascular disease is regarded as one of the most
                  important subject in the section of clinical data analysis.
                  The amount of data in the healthcare industry is huge. Data
                  mining turns the large collection of raw healthcare data into
                  information that can help to make informed decision and
                  prediction.
                </p>
               
            </div>  
            """,
                height=500,
                )


    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password",type='password')
        page_bg_img = '''
        <style>
        body {
        background-image: url("https://cdn3.vectorstock.com/i/1000x1000/40/67/light-grey-network-web-texture-seamless-pattern-vector-22984067.jpg");
        background-size: cover;
        }
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
        if st.sidebar.checkbox("Login"):
            if password == "test":
                st.success("Welcome {}".format(username))

                activity = st.selectbox("Activity",submenu)
                if activity == "Diets":
                    st.subheader("DIET CHARTS")
                    image = Image.open('./image/diet.jpg')
                    st.image(image, caption="Simple", use_column_width=True)
                    st.write('Diet in which (200%-600%DV) Vitamin-K Available one time eat')
                    data = [['Boiled Spinach', '1/2 Cup', '560%DV'], ['Boiled Turnip', '1/2 Cup', '530%DV'],
                            ['Arbi Leaf', '1/2 Cup', '520%DV'], ['Beetroot Leaf', '1/2 Cup', '360%DV'],
                            ['Sarso Saag', '1/2 Cup', '260%DV']]
                    df = pd.DataFrame(data, columns=['Diet', 'Quantity', 'Vitamin-K Defiency'])
                    st.write(df)

                    st.write('Diet in which (60%-200%DV) Vitamin-K Available three time eat')
                    data = [['Boiled Cabbage', '1/2 Cup', '190%DV'], ['Kacha Spinach', '1/2 Cup', '180%DV'],
                            ['Kacha Turnip', '1 Cup', '170%DV'], ['Kacha Salad', '1 Cup', '70%DV']]
                    df = pd.DataFrame(data, columns=['Diet', 'Quantity', 'Vitamin-K Defiency'])
                    st.write(df)

                    st.write('Diet in which Vitamin-K least Available (Vegetables)')
                    data = [['Turnip', '1 Cup', '0%DV'], ['Beatroot', '1 Cup', '0%DV'], ['Corn', '1 Cup', '1%DV'],
                            ['Kacha Onion', '1half Cup', '1%DV'], ['kacha Tomato', '1 Cup', '8%DV'],
                            ['Cucumber', '1 Cup', '21%DV']]
                    df = pd.DataFrame(data, columns=['Diet', 'Quantity', 'Vitamin-K Defiency'])
                    st.write(df)

                    st.write('Diet in which Vitamin-K least Available (Fruits)')
                    data = [['Orange', '1half Cup', '0%DV'], ['Watermelon', '1 Cup', '0%DV'],
                            ['Banana', '1half Cup', '1%DV'], ['Pineapple', '1half Cup', '1%DV'],
                            ['Apple', '1half Cup', '5%DV'], ['Strawberry', '1 Cup', '4%DV'],
                            ['Peach', '1half Cup', '5%DV']]
                    df = pd.DataFrame(data, columns=['Diet', 'Quantity', 'Vitamin-K Defiency'])
                    st.write(df)
                elif activity == "Hospitals":
                    st.subheader("HOSPITAL DOCTOR DETAILS")
                    components.html(
                        """
                        <!DOCTYPE html>
                        <html> 
                        <head> 
                       <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
                       <title>Google Maps Multiple Markers</title> 
                       <script src="http://maps.google.com/maps/api/js?sensor=false"></script>
                       <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.10.1.min.js"></script>
                       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                       <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                       <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                       </head> 
                       <body>
                            <div class="row">
                            <div class="col-sm-6">
                            <div class="card bg-dark">
                            <div class="card-body">
                            <h5 class="card-title text-white">GENERAL OPD SCHEDULES</h5>
                            <p class="card-text text-white">MORNING OPD[08:00AM - 01:00PM] , EVENING OPD [03:00PM - 06:00PM]</p>
                            <p class="card-text text-white">Further Details Click Below</p>
                            <a href="https://www.lnh.edu.pk/schedule/opdschedule" target="_blank" class="btn btn-primary">LNH HOSPITAL</a>
                            </div>
                            </div>
                            </div>
                            <div class="col-sm-6">
                            <div class="card bg-dark">
                            <div class="card-body">
                            <h5 class="card-title text-white">GENERAL OPD SCHEDULES</h5>
                            <p class="card-text text-white">MORNING OPD[08:00AM - 01:00PM] , EVENING OPD [03:00PM - 06:00PM]</p>
                            <p class="card-text text-white">Further Details Click Below</p>
                            <a href="http://nicvd.org/opd-schedule/" target="_blank" class="btn btn-primary">NICVD HOSPITAL</a>
                            </div>
                            </div>
                            </div>
                            <div class="col-sm-6">
                            <div class="card bg-dark">
                            <div class="card-body">
                            <h5 class="card-title text-white">GENERAL OPD SCHEDULES</h5>
                            <p class="card-text text-white">MORNING OPD[08:00AM - 01:00PM] , EVENING OPD [03:00PM - 06:00PM]</p>
                            <p class="card-text text-white">Further Details Click Below</p>
                            <a href="https://tabbaheart.org/clinic-schedule/" target="_blank" class="btn btn-primary">THI HOSPITAL</a>
                            </div>
                            </div>
                            </div>
                            <div class="col-sm-6">
                            <div class="card bg-dark">
                            <div class="card-body">
                            <h5 class="card-title text-white">GENERAL OPD SCHEDULES</h5>
                            <p class="card-text text-white">MORNING OPD[08:00AM - 01:00PM] , EVENING OPD [03:00PM - 06:00PM]</p>
                            <p class="card-text text-white">Further Details Click Below</p>
                            <a href="https://indushospital.org.pk/" target="_blank" class="btn btn-primary">IH HOSPITAL</a>
                            </div>
                            </div>
                            </div>
                            <div id="map" style="width: 100%; height: 850px; margin-top: 30px;"></div>
                            <script type="text/javascript">

                              var locations = [
                                  ['National Institute of Cardiovascular Diseases (NICVD)', 24.853595969835162, 67.03653989340512],
                                  ['Liaquat National Hospital And Medical College، National Stadium Rd',24.89144835408584, 67.06812141176573],
                                  ['Tabba Heart Institute,, Karachi Federal B Area',24.918914514814766, 67.0638268049106],
                                  ['Indus Hospital Korangi Crossing',24.816991432664054, 67.11190285292255] 
                                  
                                 ];
                             
                                 var map = new google.maps.Map(document.getElementById('map'), {
                                   zoom: 10,
                                   center: new google.maps.LatLng(51.530616, -0.123125),
                                   mapTypeId: google.maps.MapTypeId.ROADMAP
                                 });
                             
                                 var infowindow = new google.maps.InfoWindow();
                             
                                 var marker, i;
                                 var markers = new Array();

                                for (i = 0; i < locations.length; i++) {  
                                  marker = new google.maps.Marker({
                                    position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                                    map: map,
                                    icon: 'https://img.icons8.com/color/48/000000/marker--v2.png'
                                  });
                            
                                  markers.push(marker);
                            
                                  google.maps.event.addListener(marker, 'click', (function(marker, i) {
                                    return function() {
                                      infowindow.setContent(locations[i][0]);
                                      infowindow.open(map, marker);
                                    }
                                  })(marker, i));
                                }
                            
                                function AutoCenter() {
                                  //  Create a new viewpoint bound
                                var bounds = new google.maps.LatLngBounds();
                                //  Go through each...
                                $.each(markers, function (index, marker) {
                                bounds.extend(marker.position);
                                });
                                //  Fit these bounds to the map
                                map.fitBounds(bounds);
                                }
                                AutoCenter();

                                </script>
                                </body>
                                </html>     
                        """,
                    height = 900,
                    )

                elif activity == "Predictions":
                    st.subheader("Analysis")
                    age = st.number_input("Age", 10, 100)
                    options = ("0", "1")
                    sex = st.radio("Sex", options)
                    if(sex == "1"):
                      st.success("Male")
                    else:
                      st.success("Female")
                    cpt = ("0","1","2","3")   
                    cp = st.radio("Chest Pain Type", cpt)
                    if(cp == "0"):
                      st.success("Typical Angina")
                    elif(cp == "1"):
                      st.success("Atypical Angina")
                    elif(cp == "2"):
                      st.success("Non-Anginal")
                    else:
                      st.success("Asymptomatic")
                    trestbps = st.number_input("Resting Blood Pressure",1, 200)
                    chol = st.number_input("Cholestrol",1, 420)
                    ftb = ("0","1")
                    fbs = st.radio("Fasting Blood Sugar", ftb)
                    if(fbs == "1"):
                      st.success("True")
                    else:
                      st.success("False")
                    rte = ("0","1")  
                    restecg = st.radio("Resting Electrocardiographic",  rte)
                    if(restecg == "1"):
                      st.success("ST-T wave abnormality")
                    else:
                      st.success("Normal")
                    thalach = st.number_input("Maximum Heart Rate", 1, 200)
                    ia = ("0","1")
                    exang = st.radio("Exercise Induced Angina", ia)
                    if(exang == "1"):
                      st.success("Yes")
                    else:
                      st.success("No")
                    oldpeak = st.number_input("ST Depression", 0.0, 6.5)
                    stp = ("0","1","2")
                    slope = st.radio("Slope of the Peak", stp)
                    if(slope == "0"):
                      st.success("Upsloping")
                    elif(slope == "1"):
                      st.success("Flat")
                    else:
                      st.success("Downsloping")
                    mv = ("0","1","2","3")   
                    ca = st.selectbox("Major Vessels", mv)
                    if(ca == "0"):
                      st.success("Major Vessels 0")
                    elif(ca == "1"):
                      st.success("Major Vessels 1")
                    elif(ca == "2"):
                      st.success("Major Vessels 2")
                    else:
                      st.success("Major Vessels 3")
                    tal = ("0","1","2","3")
                    thal = st.selectbox("Thalassemia", tal)
                    data = {'Age': age,
                            'Sex': sex,
                            'Chest Pain Type': cp,
                            'Resting Blood Pressure': trestbps,
                            'Cholestrol': chol,
                            'Fasting Blood Sugar': fbs,
                            'Resting Electrocardiographic': restecg,
                            'Maximum Heart Rate': thalach,
                            'Exercise Induced Angina': exang,
                            'ST Depression': oldpeak,
                            'Slope of the Peak': slope,
                            'Major Vessels': ca,
                            'Thalassemia': thal}

                    features = pd.DataFrame(data, index=[0])
                    st.subheader('List Input parameters')
                    st.write(features)
                    filename = 'classifier.pkl'
                    clf = pickle.load(open(filename, 'rb'))
                    prediction = clf.predict(features)
                    prediction_proba = clf.predict_proba(features)
                    mapping = {0: 'No', 1: 'Yes'}
                    st.subheader('Prediction')
                    st.write(mapping[prediction[0]])
                    st.subheader('Prediction Probability')
                    st.write(prediction_proba)
                    


            else:
                st.warning("Incorrect Username or Password")





if __name__ == '__main__':
    main()
