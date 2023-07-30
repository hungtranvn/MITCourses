#include <iostream>

class Array_Seq:
{
 private:
  std::array<int> A;
  size_t size = 0;
  
  int _len() { return size;}
  int _iter() { for (auto i : A) return }
}
