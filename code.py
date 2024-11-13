import math

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (7, 8), (3, 5)]

# Öklid Mesafesi Fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)

