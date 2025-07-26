main() {
  int result = 0;

  for(int x = 1, y = 2, temp = 0; x < 4_000_000; temp = x, x = y, y += temp) {
      if (x % 2 == 0) {
        result += x;
      }
  }

  print(result);
}
