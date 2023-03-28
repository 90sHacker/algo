def reverse(word):
  if word == "":
    return ""

  return reverse(word[1:]) + word[0]


if __name__ == '__main__':
  print(reverse("We will conquer COVID-19"))