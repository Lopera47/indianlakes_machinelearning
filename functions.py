# In this notebook I'll write the different useful functions
def detect_outliers(Datos,x): # function to detect outliers
    Q3 = Datos[x].quantile(0.75)
    Q1 = Datos[x].quantile(0.25)
    IQR = Q3 - Q1
    superior = Q3 + (1.5 * IQR)
    inferior = Q1 - (1.5 * IQR)
    out_sup = Datos[Datos[x] > superior].index
    out_inf = Datos[Datos[x] < inferior].index
    outliers = []
    for i in out_sup:
        outliers.append(i)
        for j in out_inf:
            outliers.append(j)
    
    size = len(outliers)
    size2 = len(Datos[x])
    percentage = (size/size2)*100

    return f'There are {size} outliers in variable {x} ({percentage}%), and correspond to the indixes: {outliers}'