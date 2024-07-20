import matplotlib.pyplot as plt
views = [16500,11200,3300,9800]


labels = ['Facebook', 'Youtube', 'Linkedin', 'Instagram']
explore = [0,0,0.3,0]

plt.pie(views, 
        labels=labels, 
        explode=explore,
        autopct='%1.1f%%',
        wedgeprops={'width':0.3}
        )


plt.grid(True,
         linewidth='1',
         linestyle='-.'
         )
plt.title('Views Share by Social Profiles')

plt.show()