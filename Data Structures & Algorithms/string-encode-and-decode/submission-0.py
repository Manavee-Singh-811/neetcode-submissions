class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = "_".join(strs)

        return encoded_string


    def decode(self, s: str) -> List[str]:

        decoded_string = s.split("_")

        return decoded_string
