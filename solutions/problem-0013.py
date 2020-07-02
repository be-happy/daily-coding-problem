# Daily Coding Problem: Problem #13 [Hard]
# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

# Time: O(n)
# Space: O(k)

def longest_substring(s, k):
	h = {}
	start = 0
	max_len = 0
	for end in range(len(s)):
		c = s[end]

		if c in h:
			h[c] += 1
		else:
			while len(h) == k:
				a = s[start]
				start += 1
				h[a] -= 1
				if h[a] == 0:
					h.pop(a)

			h[c] = 1

		if max_len < end - start + 1:
			max_len = end - start + 1

	return max_len

assert longest_substring("abcbba", 2) == 4
assert longest_substring("abcba", 2) == 3
assert longest_substring("aaaaaabc"+"a"*15, 2) == 16
assert longest_substring("aabbcc", 3) == 6