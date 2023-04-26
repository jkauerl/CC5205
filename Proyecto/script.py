import pandas as pd

PATH = r"C:\Users\kauer\OneDrive - Universidad de Chile\U\7mo Semestre\CC5205\proyecto\US_Accidents_Dec21_updated.csv"

df = pd.read_csv(PATH, memory_map= True)

df = df.drop(["End_Time", "Start_Lat","End_Lat", "End_Lng", "Distance(mi)", "Description", "Number", "Side", "County", "Zipcode", "Country", "Timezone", "Airport_Code", "Weather_Timestamp", 
              "Wind_Direction", "Amenity", "No_Exit","Roundabout","Station", "Traffic_Calming", "Turning_Loop", "Civil_Twilight", "Nautical_Twilight", "Astronomical_Twilight"], axis=1)

df = df.dropna(how="any", axis=0)

def mph_to_kmh(mph):
    kmh = mph*1.60934
    return kmh

def ftoc(f):
    c = (5/9)*(f-32)
    return c

def mitokm(mi):
    km = mi*1.60934
    return km

def intopa(inches):
    pa = inches*0.32201 
    return pa

df["Temperature(F)"] = df["Temperature(F)"].apply(ftoc)
df["Wind_Chill(F)"] = df["Wind_Chill(F)"].apply(ftoc)
df["Pressure(in)"] = df["Pressure(in)"].apply(intopa)
df["Visibility(mi)"] = df["Visibility(mi)"].apply(mitokm)
df["Wind_Speed(mph)"] = df["Wind_Speed(mph)"].apply(mph_to_kmh)
df["Precipitation(in)"] = df["Precipitation(in)"].apply(intopa)

df = df.rename(columns={"Temperature(F)": "Temperature(C)", "Wind_Chill(F)" :
                        "Wind_Chill(C)", "Pressure(in)" : "Pressure(pa)", 
                        "Visibility(mi)" : "Visibility(km)", "Wind_Speed(mph)" 
                        : "Wind_Speed(kmh)", "Precipitation(in)" : "Precipitation(pa)"})

df[['date', 'time']] = df['Start_Time'].str.split(' ', expand=True)
df["date"]= pd.to_datetime(df["date"])
df['year'] = df['date'].dt.year
df = df.drop("Start_Time", axis=1)

PATH1 = r"C:\Users\kauer\OneDrive - Universidad de Chile\U\7mo Semestre\CC5205\proyecto\datos_limpios.csv"

df.to_csv(PATH1, index=False)