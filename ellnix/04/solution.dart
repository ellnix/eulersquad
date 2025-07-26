List<int> number_digits(int number) {
  final digits = <int>[];

  while (number > 0) {
    digits.add(number % 10);
    number ~/= 10;
  }

  return digits;
}

bool is_palindrome(int number) {
  final digits = number_digits(number);

  for(int i = 0; i < digits.length ~/ 2; i++) {
    if(digits[i] != digits[digits.length - i - 1]) {
      return false;
    }
  }

  return true;
}

main() {
  int highest = 0;

  for (int x = 100; x <= 999; x++) {
    for (int y = x; y <= 999; y++ ) {
      final product = x * y;
      if (product > highest && is_palindrome(product)) {
        highest = product;
      }
    }
  }

  print(highest);
}
