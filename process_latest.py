import pandas as pd

df = pd.read_csv('data/2024.csv')
print("Columns in 2024 dataset:")
print(df.columns[:14].tolist())

korea = df[df['Country name'].str.contains('Korea|South Korea', case=False, na=False)].sort_values('Year')
print("\n=== SOUTH KOREA TREND (2015 - 2024) ===")
for idx, row in korea[korea['Year'] >= 2015].iterrows():
    print(f"Year {int(row['Year'])}: Rank {row['Rank']}, Score {row['Ladder score']:.3f}")

print("\n=== 2024 TOP 10 COUNTRIES ===")
top2024 = df[df['Year'] == 2024].sort_values('Rank').head(10)
for idx, row in top2024.iterrows():
    print(f"Rank {int(row['Rank'])}: {row['Country name']} - {row['Ladder score']:.3f}")

print("\n=== 2024 EAST ASIA COMPARISON ===")
east_asia_countries = ['Taiwan', 'South Korea', 'Japan', 'Hong Kong', 'Mongolia', 'China']
ea_2024 = df[(df['Year'] == 2024) & (df['Country name'].isin(east_asia_countries))].sort_values('Rank')
for idx, row in ea_2024.iterrows():
    print(f"Rank {int(row['Rank'])}: {row['Country name']} - {row['Ladder score']:.3f}")

print("\n=== 2024 BOTTOM 5 COUNTRIES ===")
bottom2024 = df[df['Year'] == 2024].sort_values('Rank', ascending=False).head(5)
for idx, row in bottom2024.iterrows():
    print(f"Rank {int(row['Rank'])}: {row['Country name']} - {row['Ladder score']:.3f}")
