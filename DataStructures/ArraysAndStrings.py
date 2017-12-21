import unittest


# Question 1
def all_unique(str):
    if len(set(str)) == len(str):
        return True
    return False


# Question 2
def reverse_string(str):
    return str[::-1]


# Question 3
def remove_index(i, str):
    return str[:i] + str[i + 1:]


def remove_duplicates(str):
    for i in range(len(str) - 1):
        current = str[i]
        j = i + 1
        while j < len(str):
            if str[j] == current:
                str = remove_index(j, str)
            else:
                j += 1

        if i == len(str) - 1:
            break

    return str


# Question 4
def is_anagram(str, str1):
    return sorted(str) == sorted(str1)


# Question 5
def replace_space(str):
    return str.replace(" ", "%20")


# Question 6
def rotate_matrix(mat):
    rotation_func = lambda matrix: zip(*matrix[::-1])

    return map(lambda x: list(x), rotation_func(mat))


# Question 7
def isSubstring(s1, s2):
    return s1 in s2


def is_a_rotation(s1, s2):
    return s1 in s2 + s2


# tests
class MyTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(all_unique("abc"))
        self.assertFalse(all_unique("abcc"))

    def test2(self):
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertNotEqual(reverse_string("abc"), "abc")

    def test3(self):
        self.assertEqual(remove_duplicates("abcc"), "abc")
        self.assertNotEqual(remove_duplicates("bbbbbbbbc"), "abc")
        self.assertEqual(remove_duplicates("bbbbbbbbc"), "bc")

    def test4(self):
        self.assertTrue(is_anagram("cab", "abc"))
        self.assertFalse(is_anagram("bbc", "abc"))

    def test5(self):
        self.assertEqual(replace_space("cab abc"), "cab%20abc")
        self.assertEqual(replace_space(" "), "%20")
        self.assertNotEqual(replace_space("abc"), "abc%20")

    def test6(self):
        mat = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]

        required = [[6, 3, 0],
                    [7, 4, 1],
                    [8, 5, 2]]

        self.assertEqual(rotate_matrix(mat), required)

    def test7(self):
        self.assertTrue(is_a_rotation('waterbottle', 'erbottlewat'))
        self.assertFalse(is_a_rotation('awaterbottle', 'erbottlewat'))
