class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0

        for char in s:

            # If digit, build number
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            # Opening bracket
            elif char == '[':
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0

            # Closing bracket
            elif char == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string

            # Normal character
            else:
                current_string += char

        return current_string