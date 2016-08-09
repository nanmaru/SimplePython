int sum  = 1;

def Factorial(int value)
{
  if(value < 0)
  {
     #throw error
  }
  
  if(value == 1)
  {
    return;
  }
  
  return value * Factorial(value - 1);
}