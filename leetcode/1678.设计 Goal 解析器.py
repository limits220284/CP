class Solution:
    def interpret(self, command: str) -> str:
        # 直接遍历
        return command.replace("()","o").replace("(al)","al")