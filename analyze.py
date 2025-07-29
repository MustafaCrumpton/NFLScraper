import matplotlib.pyplot as plt

# Assuming 'top10' DataFrame is already defined with 'Player' and 'Yards' columns
plt.figure(figsize=(10,6))  # Optional: adjust figure size for readability

bars = plt.bar(top10['Player'], top10['Yards'])

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha='right')

# Add a title
plt.title('Top 10 NFL Players by Passing Yards')

# Add labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x position: center of each bar
        height,                             # y position: top of each bar
        f'{int(height)}',                   # label text: convert to int to remove decimal if not needed
        ha='center',                        # horizontal alignment
        va='bottom'                         # vertical alignment
    )

plt.tight_layout()

# Save plot as an image
plt.savefig('data/top10_passing_yards.png')

# Show plot
plt.show()