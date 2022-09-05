
import matplotlib.pyplot as plt
import pandas as pd

def stock_plot():
    bought = pd.read_csv('./data/bought.csv')
    x =  bought["product"]
    y = bought["amount"]
    plt.title( "in stock",fontdict={"fontname":"verdana","fontsize":20})
    plt.xlabel("Product",fontdict={"fontname":"verdana","fontsize":15})
    plt.ylabel("Amount",fontdict={"fontname":"verdana","fontsize":15})
    plt.bar (x, y, color = ['#d9ad4e','#d43550', '#338ee8',"#49c45f"])
    plt.figure(figsize = (6,4))
    plt.savefig("plotgraphic.png",dpi=300)
    plt.show()
    
