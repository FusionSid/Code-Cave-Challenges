#include <map>
#include <set>
#include <stack>
#include <vector>
#include <iostream>

using std::map, std::cout, std::vector, std::set, std::stack;
int find_groups(map<int, vector<int>> &graph)
{
    set<int> visited;
    stack<int> s;
    int friend_groups = 0;

    for (const auto &item : graph)
    {
        int start = item.first;
        if (visited.find(start) != visited.end())
        {
            continue;
        }

        s.push(start);

        vector<int> friends;
        while (!s.empty())
        {
            int vertex = s.top();
            s.pop();

            if (visited.find(vertex) != visited.end())
            {
                continue;
            }

            visited.insert(vertex);
            friends.push_back(vertex);

            for (int neighbour : graph[vertex])
                s.push(neighbour);
        }

        for (auto f : friends)
        {
            cout << f << " ";
        }
        cout << "\n";

        friend_groups++;
    }
    return friend_groups;
}

int main()
{
    map<int, vector<int>> graph = {
        {0, {1, 2}},
        {1, {0, 5}},
        {2, {0}},
        {3, {6}},
        {4, {}},
        {5, {1}},
        {6, {3}},
    };

    cout << "These are the following groups:\n";
    int friend_groups = find_groups(graph);
    cout << "In total there are " << friend_groups << " friend groups in the class\n";

    return 0;
}
