def cluster(X: list[int], k: int):
    count = 0
    def dist(a,b):
        nonlocal count
        count += 1
        return abs(b-a)

    n = len(X)
    clusters = [[a] for a in X]
    for _ in range(n-k):
        cluster_dists = []
        for i, cluster_i in enumerate(clusters):
            for j in range(i+1, len(clusters)):
                cluster_j = clusters[j]
                min_dist = None
                for a in cluster_i:
                    for b in cluster_j:
                        dist_ab = dist(a,b)
                        if min_dist is None or dist_ab < min_dist:
                            min_dist = dist_ab
                cluster_dists.append((min_dist, i, j))
        min_dist, i, j = min(cluster_dists)
        clusters[i].extend(clusters[j])
        del clusters[j]

    return clusters, count

if __name__ == "__main__":
    X = [1] * 1000
    n = len(X)
    for k in range(1, n):
        clusters, count = cluster(X, k)
        est_count = int(((n - k) / 6) * ((2*(n**2)) - (3*n) - (k**2) + (2*k*n) + 1))
        diff = est_count - count
        print(f"n={n}, k={k}, count={count}, est_count={est_count}, diff={diff} clusters={clusters}")
