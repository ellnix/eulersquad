const DIVISORS = [11, 12, 13, 14, 15, 16, 17, 18, 19];

bool is_divisible(int n) {
  for (final d in DIVISORS) {
    if(n % d > 0) {
      return false;
    }
  }

  return true;
}

main() {
  int n = 20;
  for(; !is_divisible(n); n += 20) {}
  print(n);
}
