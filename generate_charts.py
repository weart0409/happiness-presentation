import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setup font and styling to match DESIGN.md (Starbucks inspired)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.facecolor'] = '#F2F0EB'  # Neutral Warm Canvas
plt.rcParams['axes.facecolor'] = '#FFFFFF'    # Card White
plt.rcParams['text.color'] = '#1E3932'        # House Green / Text Black
plt.rcParams['axes.labelcolor'] = '#1E3932'
plt.rcParams['xtick.color'] = '#33433D'       # Rewards Green
plt.rcParams['ytick.color'] = '#33433D'
plt.rcParams['grid.color'] = '#EDEBE9'        # Ceramic
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.8

os.makedirs('charts', exist_ok=True)
df = pd.read_csv('data/world_happiness_unified.csv')

# Colors from DESIGN.md
STARBUCKS_GREEN = '#006241'
GREEN_ACCENT = '#00754A'
HOUSE_GREEN = '#1E3932'
GREEN_UPLIFT = '#2B5148'
GREEN_LIGHT = '#D4E9E2'
GOLD = '#CBA258'
GOLD_LIGHT = '#DFC49D'
CERAMIC = '#EDEBE9'
RED_SEMANTIC = '#C82014'

# ==========================================
# Chart 1: Correlations
# ==========================================
corr = df[['score', 'gdp', 'life_expectancy', 'social_support', 'freedom', 'corruption', 'generosity']].corr()['score'].drop('score').sort_values(ascending=True)
labels_ko = {
    'gdp': '1인당 GDP (경제력)',
    'life_expectancy': '건강 기대수명 (보건)',
    'social_support': '사회적 지지 (복지/가족)',
    'freedom': '선택의 자유 (자율성)',
    'corruption': '정부 신뢰도 (청렴도)',
    'generosity': '사회적 관용 (기부)'
}
plot_labels = [labels_ko[k] for k in corr.index]

fig, ax = plt.subplots(figsize=(8.5, 4.6), dpi=300)
# Color tiering according to importance
bar_colors = [CERAMIC if v < 0.2 else GREEN_LIGHT if v < 0.5 else GREEN_ACCENT if v < 0.75 else STARBUCKS_GREEN for v in corr.values]
bars = ax.barh(plot_labels, corr.values, color=bar_colors, height=0.55, edgecolor=HOUSE_GREEN, linewidth=0.5)
ax.set_xlim(0, 1.0)
ax.set_title('행복 지수(Score)와 각 요인 간 상관계수 (2015-2019 종합)', fontsize=13, fontweight='bold', pad=15, color=STARBUCKS_GREEN)
ax.set_xlabel('피어슨 상관계수 (Pearson Correlation, r)', fontsize=10, fontweight='bold')

for bar in bars:
    w = bar.get_width()
    ax.text(w + 0.02, bar.get_y() + bar.get_height()/2, f'{w:.3f}', va='center', ha='left', fontsize=10.5, fontweight='bold', color=HOUSE_GREEN)

# Add gold badge for highest correlation
ax.text(0.79 + 0.12, 5, '★ 핵심 동인', va='center', fontsize=9.5, fontweight='bold', color=GOLD)

plt.tight_layout()
plt.savefig('charts/chart1_correlations.png', facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

# ==========================================
# Chart 2: Korea 5-Year Trend
# ==========================================
korea_df = df[df['country'] == 'South Korea'].sort_values('year')
fig, ax1 = plt.subplots(figsize=(8.5, 4.6), dpi=300)

ax1.plot(korea_df['year'], korea_df['score'], marker='o', linewidth=3, markersize=8, color=STARBUCKS_GREEN, label='행복 점수 (Score)')
ax1.set_ylim(5.5, 6.3)
ax1.set_ylabel('행복 점수 (10점 만점)', color=STARBUCKS_GREEN, fontsize=11, fontweight='bold')
ax1.tick_params(axis='y', labelcolor=STARBUCKS_GREEN)
ax1.set_xticks(korea_df['year'])
for _, row in korea_df.iterrows():
    ax1.annotate(f"{row['score']:.3f}점", (row['year'], row['score']), textcoords='offset points', xytext=(0, 10), ha='center', fontsize=10, fontweight='bold', color=STARBUCKS_GREEN)

ax2 = ax1.twinx()
ax2.plot(korea_df['year'], korea_df['rank'], marker='s', linewidth=2.5, markersize=8, color=GOLD, linestyle='--', label='글로벌 순위 (Rank)')
ax2.set_ylim(65, 40)
ax2.set_ylabel('글로벌 순위 (낮을수록 상위)', color=GOLD, fontsize=11, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=GOLD)
ax2.grid(False)
for _, row in korea_df.iterrows():
    ax2.annotate(f"{int(row['rank'])}위", (row['year'], row['rank']), textcoords='offset points', xytext=(0, -18), ha='center', fontsize=10, fontweight='bold', color=GOLD)

plt.title('대한민국(South Korea) 5개년 순위 및 행복 점수 추이', fontsize=13, fontweight='bold', pad=15, color=STARBUCKS_GREEN)
plt.tight_layout()
plt.savefig('charts/chart2_korea_trend.png', facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

# ==========================================
# Chart 3: East Asia comparison 2019
# ==========================================
d15 = pd.read_csv('data/2015.csv')
region_map = dict(zip(d15['Country'], d15['Region']))
df19 = df[df['year'] == 2019].copy()
df19['region'] = df19['country'].map(region_map)
ea_df = df19[df19['region'] == 'Eastern Asia'].sort_values('score', ascending=True)

fig, ax = plt.subplots(figsize=(8.5, 4.6), dpi=300)
colors_ea = [STARBUCKS_GREEN if c == 'South Korea' else GOLD if c == 'Taiwan' else CERAMIC for c in ea_df['country']]
bars = ax.barh(ea_df['country'], ea_df['score'], color=colors_ea, height=0.55, edgecolor=HOUSE_GREEN, linewidth=0.5)
ax.set_xlim(0, 8.0)
ax.set_title('2019 동아시아 주요국 행복 점수 비교', fontsize=13, fontweight='bold', pad=15, color=STARBUCKS_GREEN)
ax.set_xlabel('행복 점수 (Score)', fontsize=10, fontweight='bold')

for bar, rank, c in zip(bars, ea_df['rank'], ea_df['country']):
    w = bar.get_width()
    highlight = STARBUCKS_GREEN if c == 'South Korea' else GOLD if c == 'Taiwan' else HOUSE_GREEN
    ax.text(w + 0.12, bar.get_y() + bar.get_height()/2, f"{w:.3f}점 (세계 {int(rank)}위)", va='center', ha='left', fontsize=10, fontweight='bold', color=highlight)

plt.tight_layout()
plt.savefig('charts/chart3_east_asia.png', facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

# ==========================================
# Chart 4: Korea factor comparison with Top 10 avg
# ==========================================
top10_19 = df19.sort_values('rank').head(10)
factors = ['gdp', 'social_support', 'life_expectancy', 'freedom', 'corruption', 'generosity']
factor_names = ['1인당 GDP', '사회적 지지', '건강 기대수명', '선택의 자유', '정부 신뢰도', '사회적 관용']
korea_factors = df19[df19['country']=='South Korea'][factors].values[0]
top10_factors = top10_19[factors].mean().values

x = np.arange(len(factor_names))
width = 0.35

fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)
rects1 = ax.bar(x - width/2, korea_factors, width, label='대한민국 (Korea)', color=STARBUCKS_GREEN, edgecolor=HOUSE_GREEN, linewidth=0.5)
rects2 = ax.bar(x + width/2, top10_factors, width, label='글로벌 Top 10 평균', color=GOLD_LIGHT, edgecolor=GOLD, linewidth=0.5)

ax.set_ylabel('요인별 기여 점수', fontsize=10, fontweight='bold')
ax.set_title('대한민국 vs 글로벌 Top 10 세부 지표별 기여도 비교 (2019)', fontsize=13, fontweight='bold', pad=15, color=STARBUCKS_GREEN)
ax.set_xticks(x)
ax.set_xticklabels(factor_names, fontsize=10, fontweight='bold')
ax.legend(fontsize=10.5, frameon=True, facecolor='#FFFFFF', edgecolor=CERAMIC)
ax.set_ylim(0, 1.8)

for bar in rects1:
    h = bar.get_height()
    ax.annotate(f'{h:.2f}', xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=9, fontweight='bold', color=STARBUCKS_GREEN)
for bar in rects2:
    h = bar.get_height()
    ax.annotate(f'{h:.2f}', xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=9, fontweight='bold', color='#7B5E28')

plt.tight_layout()
plt.savefig('charts/chart4_korea_vs_top10.png', facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

print('All 4 Starbucks-themed charts successfully regenerated!')
