import 'dart:math';

bool is_prime(int n) {
  for(int i = 2; i <= sqrt(n).toInt(); i++) {
    if (n % i == 0) {
      return false;
    }
  }

  return true;
}

main() {
  int input = 600_851_475_143;

  for (int i = sqrt(input).toInt(); i > 0; i--) {
    if (input % i == 0 && is_prime(i)) {
      print(i);
      break;
    }
  }
}
