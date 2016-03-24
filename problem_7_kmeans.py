"""Implementation for simple K-means clustering."""

# Calculate the mean for a cluster
def mean(cluster):
    total = sum([item for item in cluster])
    return total / float(len(cluster))

# Calculate the Manhattan distance from a data point to the cluster's centroid
def manhattan(item, centroid):
    return abs(item - centroid)

# Cluster the input data
def kmeans(data):
    # Initialize cluster's centroids
    m1 = data[0]
    m2 = data[1]

    # temp1 & temp2 are used to store previous centroid values
    # for the purpose of exitting clustering process
    temp1 = temp2 = -9999

    # Continue until centroids do not change
    while True:
        # Initialize clusters in each iteration
        cluster1 = []
        cluster2 = []

        # Create clusters based on distance b/w each data point
        # and the cluster's centroid
        for item in data:
            if manhattan(item, m1) <= manhattan(item, m2):
                cluster1.append(item)
            else:
                cluster2.append(item)

        # Update centroid's values
        m1 = mean(cluster1)
        m2 = mean(cluster2)

        # if centroids do not change, exit
        if m1 == temp1 and m2 == temp2:
            break
        # otherwise, store old centroids and continue
        else:
            temp1 = m1
            temp2 = m2

    return (cluster1, cluster2)

if __name__ == '__main__':
    input_data = [2, 4, 10, 12, 3, 20, 30, 11, 25]
    cluster1, cluster2 = kmeans(input_data)
    print "Input data: ", input_data
    print "Cluster 1: ", cluster1
    print "Cluster 2: ", cluster2
