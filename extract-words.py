import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the data
data = pd.read_csv('data/Texas Last Statement - CSV.csv', encoding = 'ISO-8859-1')
last_statments = data['LastStatement'].tolist()
last_statments_string = '\n'.join(last_statments)

# Generate WordCloud
wordcloud = WordCloud(max_font_size=80).generate(last_statments_string)

# Show Image
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
