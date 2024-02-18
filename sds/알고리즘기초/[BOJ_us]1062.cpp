#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;
bool alpha[26] = {false}; // 방문 배열 (각 알파벳 개수)
int ans = 0;
vector<string> v; // 단어 개수

void count_word()
{
    int cnt = 0;
    for (string elem : v)
    {
        bool flag = true;
        for (char ch : elem)
        { // 문자열의 각 문자마다 카운트 계산
            if (!alpha[ch - 'a'])
            {
                flag = false;
                break;
            }
        }
        if (flag)
            cnt++;
    }
    ans = max(ans, cnt);
}

void dfs(int idx, int remain)
{
    // 1. 체크인 (방문 시작)
    alpha[idx] = true;
    remain--;

    // 2. 목적지인가? (length = k)
    if (!remain)
    { // 순회 완료 -> 조건  파악
        count_word();
    }
    else
    {
        // 3. 연결된 곳을 순회
        for (int i = idx + 1; i < 26; i++)
        {
            // 4. 갈 수 있는가?
            if (alpha[i])
                continue;
            // 5. 간다
            dfs(i, remain);
        }
    }

    // 6. 체크아웃 (방문 완료)
    alpha[idx] = false;
    remain++;
    return;
}

int main()
{
    // 입력
    cin >> N >> K;
    string str;
    for (int i = 0; i < N; i++)
    {
        cin >> str;
        v.push_back(str.substr(4, str.length() - 8));
    }

    // 사전 종료 조건 (a,n,t,i,c도 만들 수 없는 경우)
    if (K < 5)
    {
        cout << 0 << '\n';
        return 0;
    }
    else if (K == 26)
    {
        cout << N << '\n';
        return 0;
    }
    else if (K == 5)
    {
        count_word();
        cout << ans;
        return 0;
    }

    // 필수 조건 추가 (a, n, t, i, c)
    alpha[0] = true;
    alpha[2] = true;
    alpha[8] = true;
    alpha[13] = true;
    alpha[19] = true;

    for (int i = 0; i < 25; i++) // A~Z까지 순회
    {
        if (alpha[i])
            continue;  // 갈 수 있는가?
        dfs(i, K - 5); // 5개의 문자 생략
    }

    // 출력
    cout << ans;

    return 0;
}