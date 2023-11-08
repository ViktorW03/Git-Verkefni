def main():
    n = int(input())
    views_dict = {}

    for _ in range(n):
        name, views = input().split()
        views = int(views)

        if name in views_dict:
            views_dict[name] += views
        else:
            views_dict[name] = views

    most_popular = max(views_dict, key=views_dict.get)
    print(most_popular)

if __name__ == "__main__":
    main()

