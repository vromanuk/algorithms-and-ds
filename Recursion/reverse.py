def reverse(string: str) -> str:
    if string:
        return reverse(string[1:]) + string[0]
    else:
        return string


if __name__ == '__main__':
    assert reverse('kayak') == 'kayak'
    assert reverse('l') == 'l'
    assert reverse('follow') == 'wollof'
    assert reverse('') == ''
