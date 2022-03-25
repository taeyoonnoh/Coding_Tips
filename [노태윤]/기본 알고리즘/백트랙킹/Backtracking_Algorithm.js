void checknode (node v)
{
  node u;
  if (promising(v))
    if (v에 해답이 있으면)
      해답을 출력;
    else
      for (v의 모든 자식 노드 u에 대해서)
        checknode(u);
}
