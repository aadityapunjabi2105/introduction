import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
appname=['Angry Bird','Marvel Comics','ColorMe','Crazy Taxi']
price=[75,190,245,55]
do=[197000,41400,196000,311000]
dtf=pd.DataFrame({'AppName':appname,'AppPrice':price,'TotalDownload':do})
plt.plot(dtf['AppName'],dtf['AppPrice'],color='b',label='price',marker='s',markerfacecolor='orange',markersize=7)
plt.xlabel('Name Of Apps:-',fontsize=18)
plt.ylabel('Price Of Apps:-',fontsize=18)
plt.title('AppPrice',fontsize=22)
plt.legend(loc=2)
plt.xticks(dtf['AppName'],fontsize=10,fontname='Lucida Handwriting')
plt.savefig('Q1(a).jpg')
plt.show()
