{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPH+SnZiD3Jh+nyQPhWHYBW"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["N × M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된\n","다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한\n","다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성\n","하시오. 다음의 4 × 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다\n"],"metadata":{"id":"Hy1l9QH7BFz-"}},{"cell_type":"code","execution_count":null,"metadata":{"id":"tjkStCir_o8Q"},"outputs":[],"source":["# 15,14\n","n, m = map(int, input().split())\n","\n","graph = []\n","for i in range(n):\n","  graph.append(list(map(int, input())))"]},{"cell_type":"code","source":["def dfs(x,y):\n","  if x<=1 or x>=n or y<=-1 or y>=m:\n","    return False\n","  if graph[x][y] == 0:\n","    # 방문처리 : 1\n","    graph[x][y] = 1\n","    # 상하좌우 재귀적으로 확인\n","    dfs(x-1, y)\n","    dfs(x, y-1)\n","    dfs(x+1, y)\n","    dfs(x, y+1)\n","    return True\n","  return False"],"metadata":{"id":"3W3wYm-VAgz0","executionInfo":{"status":"ok","timestamp":1678678153374,"user_tz":-540,"elapsed":2,"user":{"displayName":"김지원, ITM전공(학부)","userId":"09097702196948395611"}}},"execution_count":2,"outputs":[]},{"cell_type":"code","source":["result = 0\n","for i in range(n):\n","  for j in range(m):\n","    if dfs(i,j)==True:\n","      result += 1\n","\n","print(result)"],"metadata":{"id":"M1CPILg-APvR"},"execution_count":null,"outputs":[]}]}