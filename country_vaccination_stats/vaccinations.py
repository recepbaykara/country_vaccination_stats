#csv dosyasındaki verilerin okunması için pandas import edilir
#import pandas to read the data in the csv file
import pandas as p 

#csv dosyasındaki veriler okunur
#read the data in csv
data = p.read_csv("country_vaccination_stats.csv")

#dataFrame oluşturulur
#create the dataFrame
df = p.DataFrame(data)


#görevi yapacak fonkisyona dataFrame eklenir
#add the dataFrame to the function that performs the task
def impute_vaccinations(df):
    
    #ülke olarak grupla
    #group by country 
    grouped = df.groupby('country')
    
    #minimum değer uygulanır
    #apply the minimum values 
    df['daily_vaccinations'] = grouped['daily_vaccinations'].transform(
        lambda x: x.fillna(x.min() if x.min() > 0 else 0)
    )
    
    #dataFrame geri dondürülür
    #return the dataFrame
    return df

#fonkisyon uygulanır
#applying the function
df = impute_vaccinations(df)

#elde edilen veriler yeni bir csv dosyası olarak kaydedilir
#the data saved as a  new csv file 
output_file = 'imputed_vaccinations.csv'
df.to_csv(output_file, index=False)


print(f"Data has been saved to {output_file}")