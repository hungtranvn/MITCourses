#ifndef _SEQ_INTERFACE_H_
#define _SEQ_INTERFACE_H_
#include <exception>
#include <iostream>

class Array_Seq
{
  int *_array;
  unsigned int _size;

  unsigned int _len() {return _size};
  void _copy_forward(unsigned int i, unsigned int n, Seq_Interface& A, unsigned int j);
  void _copy_backward(unsigned int i, unsigned int n, Seq_Interface& A, unsigned int j);

public:
  int get_at(size_t i) const { return _array[i] };
  void insert_at(size_t i, int x);
  int delete_at(size_t i);
  void insert_first(int i);
  void delete_first(void);
  void insert_last(int x);
  int delete_last(void);
  
  Array_Seq(unsigned int size = 0);
  virtual ~Array_Seq();
}

#endif
