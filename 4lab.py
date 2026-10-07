import pandas as pd
df = pd.read_csv(r"C:\Users\user\Desktop\4lab\titanic.csv")
print(df.shape); print(df.head()); df.info(); print(df.describe())
kids = df[df['age'] < 12]
print(len(kids), kids['survived'].mean())
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df = df.drop(columns=['deck'])
print(df.isna().sum())
print(df.groupby('sex')['survived'].mean())
print(df.groupby('pclass')['survived'].mean())
print(df.groupby(['pclass', 'sex'])['age'].mean().round(1))
import matplotlib.pyplot as plt, seaborn as sns
fig, ax = plt.subplots(1, 3, figsize=(13, 3.5))
ax[0].hist(df['age'], bins=30); ax[0].set_title('Возраст')
sns.boxplot(x='pclass', y='fare', data=df, ax=ax[1]); ax[1].set_title('Цена по классу')
sns.barplot(x='sex', y='survived', data=df, ax=ax[2]); ax[2].set_title('Выживаемость')
fig.tight_layout(); fig.savefig('titanic.png', dpi=120)
plt.show()
df['Family'] = df['sibsp'] + df['parch']
df['Sex_num'] = df['sex'].map({'Female': 1, 'Male': 0})
df.to_csv(r'C:\clean.csv', index=False)
df_clean = pd.read_csv(r"C:\Users\user\Desktop\3-isip-3k kot\3 laba\clean.csv")
print(df_clean[["age", "embarked"]].isna().sum())
df = pd.read_csv;("clean.csv")
ax = sns.histplot(
    data=df,
    x="fare",
    hue="survived",
    multiple="fill",  
    bins=15, 
    stat="probability",  
)
plt.xlabel("Цена")
plt.ylabel("Процент выживаемости ")
plt.legend(title="Статус", labels=["Выжил", "Погиб"])
plt.savefig("fare_homework.png")
plt.show()