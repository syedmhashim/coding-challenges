package main

import (
	"fmt"
	"strings"
	"unicode"
)

var (
	lowerCaseAlphabetsArray = [26]string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
	alphabetsToIndexMap     = map[string]int{
		"a": 0,
		"b": 1,
		"c": 2,
		"d": 3,
		"e": 4,
		"f": 5,
		"g": 6,
		"h": 7,
		"i": 8,
		"j": 9,
		"k": 10,
		"l": 11,
		"m": 12,
		"n": 13,
		"o": 14,
		"p": 15,
		"q": 16,
		"r": 17,
		"s": 18,
		"t": 19,
		"u": 20,
		"v": 21,
		"w": 22,
		"x": 23,
		"y": 24,
		"z": 25,
	}
)

func encryptText(s string, k int) string {
	encryptedText := ""
	for _, r := range s {
		if !unicode.IsLetter(r) {
			encryptedText += string(r)
			continue
		}
		alphabet := strings.ToLower(string(r))
		encryptedChar := lowerCaseAlphabetsArray[(alphabetsToIndexMap[alphabet]+k)%26]
		if unicode.IsUpper(r) {
			encryptedChar = strings.ToUpper(encryptedChar)
		}
		encryptedText += encryptedChar
	}
	return encryptedText
}

func main() {
	fmt.Println(encryptText("There's-a-starman-waiting-in-the-sky", 3))
}
