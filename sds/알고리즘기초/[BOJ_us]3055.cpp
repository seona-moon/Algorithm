#include <iostream>
#include <queue>

using namespace std;

const int MAX = 50;

// 좌 우 위 아래
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

typedef struct point
{
    int x;
    int y;
    char type;
} point;

int R, C;
char map[MAX][MAX];
int dp[MAX][MAX] = {0};
queue<point> q;

int main()
{

    // 입력
    cin >> R >> C;

    // 지도 제작
    point s; // 도치
    point d; // 굴
    point w; // 물

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 'S')
                s = {i, j, 'S'};
            if (map[i][j] == 'D')
                d = {i, j, 'D'};
            if (map[i][j] == '*')
                w = {i, j, '*'};
        }
    }

    // 큐에 시작점을 넣을 때 물 -> 고슴도치 순으로 넣기
    q.push(w);
    q.push(s);

    bool flag = false;
    while (!q.empty())
    {
        // 1. 큐에서 꺼내옴
        point spot = q.front();
        q.pop();
        int x = spot.x;
        int y = spot.y;
        char type = spot.type;

        // 2. 목적지인가? (고슴도치)
        if (type == 'D')
        {
            cout << dp[x][y];
            flag = true;
            break;
        }

        // 3. 연결된 곳을 순회 (좌우위아래)
        for (int i = 0; i < 4; i++)
        {
            int mx = x + dx[i];
            int my = y + dy[i];

            // 4. 갈 수 있는가? (공통)
            if (mx >= R || mx < 0 || my >= C || my < 0)
                continue;
            if (type == 'S' || type == '.')
            {
                // 4. 갈 수 있는가? (고슴도치)
                // .이면서 굴인 곳 + 방문하지 않은 곳!!!
                if ((map[mx][my] == 'D' || map[mx][my] == '.') && dp[mx][my] == 0)
                {
                    // 5. 체크인 (고슴도치)
                    dp[mx][my] = dp[x][y]++;
                    // 6. 큐에 넣음
                    q.push({mx, my, map[mx][my]});
                }
            }
            else if (type == '*')
            {
                // 4. 갈 수 있는가? (물)
                if (map[mx][my] == '.' || map[mx][my] == 'S')
                {
                    // 5. 체크인 (물)
                    map[mx][my] = '*';
                    // 6. 큐에 넣음
                    q.push({mx, my, '*'});
                }
            }
        }
    }
    if (cout << "KAKTUS")
        ;
    return 0;
}