import pandas as pd
import matplotlib.pyplot as plt
import io
import numpy as np

def samples_per_class():
    df = pd.read_csv('train_users_2.csv')
    x = df["country_destination"].value_counts(sort=False)
    plt.bar(x.index, x.values)
    plt.xticks(rotation = 90)

    plt.title("Samples per class")
    
    #save image
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    plt.close()
    return bytes_image

def affiliate_channel_percentage():
    df = pd.read_csv('train_users_2.csv')
    x= df["affiliate_channel"].value_counts()
    x_percent = [num/np.sum(x.values) for num in x.values]
    plt.bar(x.index, x_percent)
    plt.xticks(rotation = 90)

    plt.ylabel("Percentage")
    plt.title("Affiliate channel percentage")

    #save image
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    plt.close()
    return bytes_image

def provider():
    df = pd.read_csv('train_users_2.csv')
    x= df["affiliate_provider"].value_counts()
    x_percent = [num/np.sum(x.values) for num in x.values]
    plt.bar(x.index, x_percent)
    plt.xticks(rotation = 90)

    plt.ylabel("Percentage")
    plt.title("Affiliate channel provider percentage")

    #save image
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    plt.close()
    return bytes_image

def signup_app_per_age():
    df = pd.read_csv('train_users_2.csv')
    x = df["signup_app"].value_counts()
    
    ages_labels = ['(id, 18 - 20)', '(id, 20 - 30)', '(id, 30 - 40)', '(id, 40 - 50)', '(id, 50 - 60)', '(id, 60 - 70)', '(id, 70+)']
    ages = pd.cut(df['age'], bins=[18, 20, 30, 40, 50, 60, 70, 100], labels=ages_labels)
    df["labeled_ages"] = ages
    arr = np.zeros((len(ages_labels), len(x.index)))
    arr = [(df[df['labeled_ages'] == age_label]['signup_app'].value_counts()).values for age_label in ages_labels]

    width = 0.1
    z = np.arange(len(x.index))
    plt.bar(z-0.3, arr[0], width)
    plt.bar(z-0.2, arr[1], width)
    plt.bar(z-0.1, arr[2], width)
    plt.bar(z, arr[3], width)
    plt.bar(z+0.1, arr[4], width)
    plt.bar(z+0.2, arr[5], width)
    plt.bar(z+0.3, arr[6], width)

    plt.xticks(z, x.index)
    plt.xticks(rotation = 90)

    plt.xlabel("signup_app")
    plt.ylabel("Number of users")
    plt.legend(ages_labels)
    plt.title("Signup app dist per age")

    #save image
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    plt.close()
    return bytes_image
