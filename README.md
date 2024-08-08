<div align="center">
    <h1>KMeans Visualization</h1>
</div>

***Project Overview***

This project provides a visual demonstration of the KMeans clustering algorithm using Pygame. It allows users to interactively explore how the KMeans algorithm works by enabling them to add data points, adjust the number of clusters, and visualize the clustering process and results in real-time.

***Key Features***

1. **Interactive Point Addition**: Users can click on the panel to add data points, which will be used in the clustering process. This interactivity helps in understanding how different point distributions affect the clustering outcome.

2. **Cluster Adjustment**: The program allows users to dynamically increase or decrease the number of clusters (K). This is crucial for observing how the algorithm performs with different values of K and how it influences the grouping of data points.

3. **Algorithm Execution**: Users can run the KMeans algorithm in two different ways:

- **Custom Implementation**: This involves a detailed, manually coded execution of the KMeans algorithm. Users can initialize cluster centers randomly and label each point to the nearest center by calculating Euclidean distances. The cluster centers are then recalculated as the average position of all assigned points. This process repeats iteratively, allowing users to observe the convergence and refinement of clusters, providing a deep understanding of the KMeans algorithm's mechanics.

- **Scikit-learn Implementation**: Utilizes the efficient and optimized KMeans implementation from the Scikit-learn library, providing a comparison to the custom implementation.

4. **Random Cluster Initialization**: The program can initialize cluster centers randomly, allowing users to observe how initial cluster positions affect the final clusters.

5. **Reset Functionality**: Provides an option to reset the panel, clearing all points and cluster centers, enabling users to start a new clustering experiment from scratch.

6. **Real-time Error Calculation**: Displays the total error (sum of distances from points to their respective cluster centers) for the current clustering configuration, giving users an insight into the clustering performance.

***Learning Outcomes***

This project is designed to help users:

- Understand the KMeans clustering algorithm through hands-on interaction.

- Observe the effects of different K values and initial cluster positions.

- Compare the custom algorithm execution with the library-provided solution.

- Visualize the clustering process and the convergence of cluster centers.

By offering an interactive and visual approach, this project aims to make the KMeans clustering algorithm more accessible and comprehensible to learners and enthusiasts.

***Requirements***

- Python 3.x

- Pygame

- Scikit-learn

***Run the Application***

After installing the necessary libraries, you can run the application using the following command:

```bash
python KMeans_Visualization.py
```
