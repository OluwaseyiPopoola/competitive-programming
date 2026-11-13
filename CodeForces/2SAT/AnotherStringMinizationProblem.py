def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        a = list(map(int, input().split()))

        m_str = ['B']*m

        for i in range(n):
            m_idx = a[i] - 1
            if m_idx == m - m_idx - 1:
                m_str[m_idx] = 'A'

            else:
                fst = m_idx
                scnd = m - m_idx - 1 

                if scnd < fst:
                    fst, scnd = scnd, fst

                if m_str[fst] == "B":
                    m_str[fst] = "A"
                else:
                    m_str[scnd] = "A" 


        print("".join(m_str))

        


if __name__ == "__main__":
    main()